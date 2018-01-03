import asyncio


def valid_command(data):
    arr = data.split(" ")
    if arr[0] in ['put', 'get']:
        return True
    else:
        return False


def _generate_response(key, value_tur):
    return "{} {} {}\n".format(key, value_tur[1], value_tur[0])


class ClientServerProtocol(asyncio.Protocol):
    metrics = {}

    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, data):
        result_message = "ok\n"
        if not valid_command(data):
            return "error\nwrong command\n\n"
        arr = data.split(" ")
        if arr[0] == 'put':
            val = self.metrics.setdefault(arr[1], [])
            val.append((int(arr[3]), float(arr[2])))
            result_message += "\n"
        elif arr[0] == 'get':
            key = arr[1].replace('\n', '')

            if key == '*':
                for metric, list_value in self.metrics.items():
                    for item in list_value:
                        result_message += _generate_response(metric, item)
            elif key in self.metrics:
                for item in self.metrics.get(key):
                    result_message += _generate_response(key, item)

            result_message += "\n"

        return result_message

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server("127.0.0.1", 10001)
