import socket


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, metric):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(("get {}\n".format(metric)).encode("utf8"))
                res = sock.recv(1024)
                while "\n\n" not in res.decode("utf8"):
                    res += sock.recv(1024)
                res = res.decode("utf8").split('\n')
                if res[0] == 'error':
                    raise ClientError

                result = {}
                for item in res:
                    if item != 'ok' and item != '':
                        arr = item.split(' ')
                        result.setdefault(arr[0], []).append((int(arr[2]), float(arr[1])))
                        result.setdefault(arr[0], []).sort(key=lambda metric: metric[0])

                return result
            except socket.timeout:
                raise ClientError
            except socket.error as ex:
                raise ClientError

    def put(self, metric, value, timestamp):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(("put {} {} {}\n".format(metric, value, timestamp)).encode("utf8"))
                res = sock.recv(1024)
                while "\n\n" not in res.decode("utf8"):
                    res += sock.recv(1024)
                res = res.decode("utf8").split('\n')
                if res[0] == 'error':
                    raise ClientError

            except socket.timeout:
                raise ClientError
            except socket.error as ex:
                raise ClientError


class ClientError(Exception):
    """Class to raise exception from client """
