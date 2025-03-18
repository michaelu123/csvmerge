import csv

from utils import log


class excel2(csv.Dialect):
    """Describe the usual properties of Excel-generated CSV files."""
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL


class CsvReader:
    def __init__(self, f):
        csv.register_dialect("excel2", excel2)
        self.reader = csv.DictReader(f, dialect="excel2")

    def read(self):
        rows = []
        for row in self.reader:
            rows.append(row)
        return rows


class CsvWriter:
    def __init__(self, f):
        self.fieldNames = [
            "MITGLIEDSNR",
            "@MH@MF",
            "TITEL",
            "VORNAME",
            "ADEL",
            "NAME",
            "NAMENSZUSATZ",
            "BRIEFANREDE",
            "BRIEFANREDE2",
            "STRASSE",
            "PLZ",
            "ORT",
            "TELEFON1",
            "TELEFON2",
            "MOBIL",
            "EMAIL",
            "EMAIL2",
            "LV",
            "KV",
            "OG",
            "ANZAHL_MF"
        ]

        csv.register_dialect("excel2", excel2)
        self.writer = csv.DictWriter(
            f, self.fieldNames, dialect="excel2", extrasaction="ignore")
        self.writer.writeheader()

    def write(self, entry):
        row = entry
        # row = {
        # "Typ": "Radtour", "Titel": titel, "Nummer": tourNummer,
        # "Radtyp": radTyp, "Tourtyp": kategorie,
        # "Datum": datum, "Endedatum": enddatum,
        # "Tourlänge": strecke, "Schwierigkeit": schwierigkeit,
        # "Höhenmeter": hoehenmeter, "Anstiege": anstiege, "Charakter": character,
        # "Abfahrten": abfahrten, "Kurzbeschreibung": kurzbeschreibung,
        # "Beschreibung": beschreibung,
        # "ZusatzInfo": zusatzinfo, "Tourleiter": tourLeiter
        # }
        self.writer.writerow(row)
