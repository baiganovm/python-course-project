
class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        f = None
        try:
            res = ""
            f = open(self.path, 'r')
            for line in f:
                res += line
            f.close()
            return res
        except IOError:
            if f is not None:
                f.close()
            return ""


if __name__ == "__main__":
    reader = FileReader("example.txt")
    print(reader.read())
