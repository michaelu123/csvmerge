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
            "ANREDE",
            "TITEL",
            "VORNAME",
            "ADEL",
            "NAME",
            "NAMENSZUSATZ",
            "BRIEFANREDE",
            "BRIEFANREDE2",
            "ORGANISATION1",
            "ORGANISATION2",
            "ORGANISATION3",
            "ADRESSZUSATZ",
            "ABTEILUNG",
            "FUNKTION",
            "STRASSE",
            "PLZ",
            "ORT",
            "POSTFACH",
            "PPLZ",
            "PORT",
            "BUNDESLAND",
            "STAAT",
            "TELEFON1",
            "TELEFON2",
            "MOBIL",
            "Fax",
            "EMAIL",
            "EMAIL2",
            "SKYPE",
            "Homepage",
            "DEAKTIV",
            "DEAKTIVGRUND",
            "GEBURTSDATUM",
            "GEBURTSJAHR",
            "BERUF",
            "EINTRITT",
            "AUSTRITT",
            "KUENDIGUNG_AM",
            "AUSTRITTSGRUND",
            "STATUS",
            "AKTIONSCODE",
            "BEITRAGSSCHLUESSEL",
            "BEITRAG",
            "FAELLIG_AM",
            "DAUERSPENDE",
            "ZAHLART",
            "MAHNUNG1",
            "MAHNUNG2",
            "LV",
            "KV",
            "OG",
            "WUNSCH_GL",
            "ZUZUG_LV",
            "ZUZUG_KV",
            "ANZAHL_MF",
            "RUECKLAUF1",
            "RUECKLAUF2",
            "ANZAHL_RW",
            "NOTIZ",
            "BV_NOTIZEN",
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
