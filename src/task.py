from csvRW import *


def name(row):
    return row["VORNAME"] + " " + row["NAME"] + ", " + row["MITGLIEDSNR"]


def toHNr(s):
    if len(s) > 2:
        return s[0:len(s)-2] + "00"
    return s


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
        self.hmap = {}

    def setFiles(self, fileHPath, fileFPath, fileOutPath):
        self.fileHPath = fileHPath
        self.fileFPath = fileFPath
        self.fileOutPath = fileOutPath

    def setMode(self, mode):
        self.mode = mode

    def stepi(self, curr):
        if curr == 0:
            with open(self.fileHPath, "r", encoding="utf-8-sig") as csvHfile:
                csvReader = CsvReader(csvHfile)
                self.fileHRows = csvReader.read()
            for row in self.fileHRows:
                self.hmap[row["MITGLIEDSNR"]] = row
            print("Hauptmitglieder:", len(self.fileHRows), "Einträge gelesen")
            return
        if curr == 1:
            with open(self.fileFPath, "r", encoding="utf-8-sig") as csvFfile:
                csvReader = CsvReader(csvFfile)
                self.fileFRows = csvReader.read()
            print("Familienmitglieder:", len(
                self.fileFRows), "Einträge gelesen")
            return
        if curr == 2:
            with open(self.fileOutPath, "w", encoding="utf-8-sig") as csvOutfile:
                csvWriter = CsvWriter(csvOutfile)
                if self.mode == "h":
                    rows = self.hrows()
                else:
                    rows = self.frows()
                for row in rows:
                    csvWriter.write(row)
            print("Ausgabedatei geschrieben, ", len(rows), "Einträge")
            return

    def hrows(self):
        for hrow in self.fileHRows:
            hrow["@MH@MF"] = ""
            if not hrow["EMAIL"]:
                hrow["MITGLIEDSNR"] += " @H"
                hrow["@MH@MF"] += "@H"
        for frow in self.fileFRows:
            if not frow["EMAIL"]:
                hnr = toHNr(frow["MITGLIEDSNR"])
                hrow = self.hmap.get(hnr)
                if not hrow:
                    print("Kein Hauptmitglied für ", name(frow))
                    continue
                if "@F" not in hrow["MITGLIEDSNR"]:
                    hrow["MITGLIEDSNR"] += " @F"
                    hrow["@MH@MF"] += "@F"
        return self.fileHRows

    def frows(self):
        for frow in self.fileFRows:
            frow["@MH@MF"] = ""
            if not frow["EMAIL"]:
                hnr = toHNr(frow["MITGLIEDSNR"])
                hrow = self.hmap.get(hnr)
                if not hrow:
                    print("Kein Hauptmitglied für ", name(frow))
                    frow["@MH@MF"] = "@HM-ERROR"
                    continue
                if hrow["EMAIL"]:
                    frow["EMAIL2"] = hrow["EMAIL"]
        return self.fileFRows
