import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path
        try:
            self._file = open(path, 'r')
        except FileNotFoundError:
            self._file = None

    def write(self, message):
        with open(self.path, 'w+') as f:
            f.write(message)

    def _append(self, message):
        with open(self.path, 'a+') as f:
            f.write(message)

    def __add__(self, other):
        d = tempfile.gettempdir()
        path = os.path.join(d, "res123.txt")
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')

        temp = File(path)
        try:
            with open(self.path, 'r') as f:
                temp._append(f.read())
        except FileNotFoundError:
            temp._append('')
        try:
            with open(other.path, 'r') as f:
                temp._append(f.read())
        except FileNotFoundError:
            temp._append('')

        return temp

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        if self._file is None:
            raise StopIteration
        res = self._file.readline()
        if res == '':
            raise StopIteration
        return res


if __name__ == "__main__":
    o = File("1.txt")
    print(o)

    obj2 = File("2.txt")

    obj3 = o + obj2

    print(obj3)

    for m in obj3:
        print(m)
