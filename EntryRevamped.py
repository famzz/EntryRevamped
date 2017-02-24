import tkinter as tk

from ArrayVar import ArrayVar


class EntryRevamped(tk.Entry):
    """
    A revamped version of the default Entry widget in tkinter that adds a new 'listener' keyword that can be assigned to
    be called whenever the entry box is written to by the user.
    Your listener function will have the following arguments passed to it by default by EntryRevamped:

        :param varname: The name of the variable, assigned automatically by EntryRevamped.
        :param elementname: The name of the entry in Tcl, assigned automatically by EntryRevamped.
        :param mode: The mode passed to the Tcl trace function.

        NOTE: Your listener function must list these parameters. You need not worry about the value of these parameters
        (they are handled by EntryRevamped). They are listed here for debugging purposes. You CANNOT list any other
        parameters.
        To use parameters in your listener then use the addparam, removeparam, getparam, getparams and setparams methods
        that come with EntryRevamped. These convenience functions modify a dictionary that will live as long as the
        entry widget to allow the user to pass around parameters for their listener.
    Example:
        def onchange(varname, elementname, mode):
            name = self.entry.getparam("name")
            print(name)
            The console will output "Entry1".
            Do whatever you wish here.

        self.entry = EntryRevamped(master, listener=onchange).pack()
        self.entry.addparam("name", "Entry1")
    """

    def __init__(self, master, *args, **kwargs):
        """
        Intialise a new EntryRevamped widget.
            :type self: EntryRevamped.EntryRevamped
            :param master: The parent tkinter toplevel that will hold the entry widget.
            :param args: Default arguments that entry normally accepts.
            :param kwargs: Default keywords that entry normally accepts, includes the new 'listener' keyword.
            :keyword listener: A new keyword argument that accepts a function as its argument. Called when the entry box
             is modified.
        """
        self.arrayvar = ArrayVar()
        self.params = {}

        listener = kwargs['listener']
        kwargs.pop('listener')

        entries = len(self.arrayvar.get().keys())
        self.name = "EntryRevamped " + str(entries)

        textvariable = self.arrayvar(master=master, name=self.name, elementname=self.name)

        kwargs['textvariable'] = textvariable

        tk.Entry.__init__(self, master, *args, **kwargs)

        self.arrayvar.trace(mode='w', callback=listener)

    def setlistener(self, listener):
        """
        Set a new listener function.
        """
        self.arrayvar.trace(mode='w', callback=listener)

    def removelistener(self):
        """
        Unset the current listener.
        """
        self.arrayvar.__del__()

    def gettext(self):
        """
        Get the current text in the entry.
        :return: The text.
        """
        return self.arrayvar.__getitem__(self.name)

    def settext(self, text):
        """
        Set the text in the entry to 'text'.
        :param text: The new text value.
        """
        self.arrayvar.__setitem__(self.name, text)

    def addparam(self, key, value):
        """
        A mechanism to pass around parameters that are needed for the listener.
        :param key: The key of the parameter.
        :param value: The parameter itself. Can be any type.
        """
        self.params[key] = value

    def removeparam(self, key):
        """
        Remove the parameter stored at index.
        :param key: The key of the parameter to remove.
        """
        self.params.pop(key)

    def getparam(self, key):
        """
        Get the parameter stored at index.
        :param key: The key of the parameter to return.
        :return: The corresponding parameter.
        """
        return self.params[key]

    def getparams(self):
        """
        Get the dictionary of currently stored parameters.
        :return: Parameters as a dictionary.
        """
        return self.params

    def setparams(self, params):
        """
        Set a new list of parameters. Shouldn't really be needed.
        :param params: The new dictionary of parameters.
        """
        self.params = params
