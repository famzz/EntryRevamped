import tkinter as tk

from EntryRevamped import EntryRevamped


class Main:

    def __init__(self):
        self._entry = None

    def onchange(self, varname, elementname, mode):
        text = self._entry.gettext()[-1]
        print("User wrote " + text)

    def main(self, master):
        self._entry = EntryRevamped(master, listener=self.onchange)
        self._entry.pack()

if __name__ in '__main__':
    root = tk.Tk()
    Main().main(root)
    root.mainloop()
