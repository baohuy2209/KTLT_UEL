class FileFactory:
    def readData(self, filename, mode_file):
        with open(filename, mode_file) as file:
            data = file.read()
        return data
    def writeData(self, filename, data):
        with open(filename, "w") as file:
            file.write(data)
