import contextlib
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk

from utils import log

onMsg = "Jetzt aber wirklich!"
offMsg = "Erstmal testen"
phases = ("Namen überprüfen", "Nicht einverstandene löschen",
          "Änderungen übernehmen")


class TxtWriter:
    def __init__(self, targ, tk):
        self.txt = targ

    def write(self, s):
        self.txt.insert("end", s)


class FileSelector(Frame):
    def __init__(self, master, labeltext, **kw):
        super().__init__(master)
        self.labeltext = labeltext
        self.label = Label(self, text=labeltext, width="15")
        self.svar = StringVar()
        self.entry = Entry(self, textvariable=self.svar,
                           width=50, borderwidth=2, **kw)
        self.btn = Button(self, text="Wählen",
                          command=self.selectFile, padx="10")
        # self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=0, column=1, sticky="we", padx=5, pady=5)
        self.btn.grid(row=0, column=2, sticky="e")

    def get(self):
        return self.svar.get()

    def set(self, s):
        return self.svar.set(s)

    def selectFile(self):
        if self.labeltext == "Ausgabedatei":
            self.fileName = asksaveasfilename(
                title="Datei auswählen",
                defaultextension=".csv", filetypes=[("CSV", ".csv")])
        else:
            self.fileName = askopenfilename(
                title="Datei auswählen",
                defaultextension=".csv", filetypes=[("CSV", ".csv")])
        self.svar.set(self.fileName)


class Gui:
    def __init__(self, task):
        root = Tk()
        self.root = root
        self.task = task
        self.cont = False
        self.logName = "csvmerge"
        # root = customtkinter.CTk()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        c = ttk.Frame(root, padding=(3, 6),
                      borderwidth=3, relief="solid")
        c.grid(column=0, row=0, sticky=(N, W, E, S))
        c.rowconfigure(0, weight=1)
        c.rowconfigure(1, weight=1)
        c.columnconfigure(0, weight=1)

        self.fs1 = FileSelector(c, "Datei 1")
        self.fs2 = FileSelector(c, "Datei 2")
        self.fsOut = FileSelector(c, "Ausgabedatei")
        self.fs1.grid(column=0, row=0, sticky="we")
        self.fs2.grid(column=0, row=1, sticky="we")
        self.fsOut.grid(column=0, row=2, sticky="we")

        self.fs1.set(
            "C:/Users/Michael/PythonProjects/csvmerge/Heruntergeladen Hauptmitglieder.csv")
        self.fs2.set(
            "C:/Users/Michael/PythonProjects/csvmerge/Heruntergeladen Familienmitglieder.csv")
        self.fsOut.set("out.csv")

        btn1 = Button(c, text="Start", command=lambda: self.run(), bg="red")
        btn1.grid(column=0, row=3, columnspan=3, pady=10)
        self.btn = btn1

        textContainer = ttk.Frame(root, borderwidth=2, relief="sunken")
        text = Text(textContainer, wrap="none", borderwidth=0,
                    cursor="arrow")  # width=100, height=40,
        self.text = text
        textVsb = Scrollbar(textContainer, orient="vertical",
                            command=text.yview)
        textHsb = Scrollbar(textContainer, orient="horizontal",
                            command=text.xview)
        text.configure(yscrollcommand=textVsb.set,
                       xscrollcommand=textHsb.set)
        textContainer.grid(row=5, columnspan=2, padx=5, pady=2, sticky="nsew")
        text.grid(row=0, column=0, sticky="nsew")
        textVsb.grid(row=0, column=1, sticky="ns")
        textHsb.grid(row=1, column=0, sticky="ew")
        textContainer.rowconfigure(0, weight=1)
        textContainer.columnconfigure(0, weight=1)

    def startGui(self):
        self.text.delete("1.0", END)
        txtWriter = TxtWriter(self.text, self.root)
        with contextlib.redirect_stdout(txtWriter):
            self.root.mainloop()
        # self.root.mainloop()

    def step(self):
        self.cont = self.task.step()
        if self.cont:
            self.root.after(0, lambda: self.step())
        else:
            log(self.logName, self.msgs)
            print("msgs", self.msgs)
            self.btn.configure(state=NORMAL, background="red")
            print("Fertig!")

    def run(self):
        try:
            self.text.delete("1.0", END)
            self.btn.configure(state=DISABLED, background="white")
            self.msgs = "???"
            self.task.setFiles(
                self.fs1.get(), self.fs2.get(), self.fsOut.get())
            self.step()
        except Exception as e:
            print("Exception", e)
