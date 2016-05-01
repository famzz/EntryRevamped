import tkinter as tk
import sys
from ArrayElementVar import ArrayElementVar


class ArrayVar(tk.Variable):
    """A variable that works as a Tcl array variable"""

    _default = {}
    _elementvars = {}
    _name = None
    _master = None

    def __del__(self):
        self._tk.globalunsetvar(self._name)
        for elementvar in self._elementvars:
            del elementvar

    def __setitem__(self, elementname, value):
        if elementname not in self._elementvars:
            v = ArrayElementVar(varname=self._name, elementname=elementname, master=self._master)
            self._elementvars[elementname] = v
        self._elementvars[elementname].set(value)

    def __getitem__(self, name):
        if name in self._elementvars:
            return self._elementvars[name].get()
        return None

    def __call__(self, elementname, name, master):
        """Create a new StringVar as an element in the array"""
        self._name = name
        self._master = master
        if elementname not in self._elementvars:
            v = ArrayElementVar(varname=self._name, elementname=elementname, master=self._master)
            self._elementvars[elementname] = v
        return self._elementvars[elementname]

    def set(self, dictvalue):
        # this establishes the variable as an array
        # as far as the Tcl interpreter is concerned
        self._master.eval("array set {%s} {}" % self._name)

        for (k, v) in dictvalue.items():
            self._tk.call("array", "set", self._name, k, v)

    def get(self):
        """Return a dictionary that represents the Tcl array"""
        value = {}
        for (elementname, elementvar) in self._elementvars.items():
            value[elementname] = elementvar.get()
        return value

    def _report_exception(self):
        """Internal function."""
        exc, val, tb = sys.exc_info()
        root = self._master
        root.report_callback_exception(exc, val, tb)
