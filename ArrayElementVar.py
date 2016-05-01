import tkinter as tk


class ArrayElementVar(tk.StringVar):
    '''A StringVar that represents an element of an array'''
    _default = ""

    def __init__(self, varname, elementname, master):
        self._master = master
        self._tk = master.tk
        self._name = "%s(%s)" % (varname, elementname)
        self.set(self._default)

    def __del__(self):
        """Unset the variable in Tcl."""
        self._tk.globalunsetvar(self._name)