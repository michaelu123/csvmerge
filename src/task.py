from csvRW import *


class Task:
    def __init__(self, stop):
        self.start = 0
        self.stop = stop
        self.curr = 0

    def stepi(self, i):
        print("step", i)

    def step(self):
        self.stepi(self.curr)
        self.curr += 1
        if self.curr != self.stop:
            return True
        self.curr = self.start
        return False


class CsvTask(Task):
    def __init__(self):
        super().__init__(3)

    def setFiles(self, file1Path, file2Path, fileOutPath):
        self.file1Path = file1Path
        self.file2Path = file2Path
        self.fileOutPath = fileOutPath

    def stepi(self, curr):
        if curr == 0:
            with open(self.file1Path, "r", encoding="utf-8-sig") as csv1file:
                csvReader = CsvReader(csv1file)
                self.file1Rows = csvReader.read()
            print("File1 gelesen:", len(self.file1Rows), "Einträge gelesen")
            return
        if curr == 1:
            with open(self.file2Path, "r", encoding="utf-8-sig") as csv2file:
                csvReader = CsvReader(csv2file)
                self.file2Rows = csvReader.read()
            print("File2 gelesen:", len(self.file2Rows), "Einträge gelesen")
            return
        if curr == 2:
            print("File1", self.file1Rows)
            print("File2", self.file2Rows)
            with open(self.fileOutPath, "w", encoding="utf-8-sig") as csvOutfile:
                csvWriter = CsvWriter(csvOutfile)
                csvWriter.write(self.file1Rows[0])
                csvWriter.write(self.file2Rows[0])
            print("FileOut geschrieben")
            return
