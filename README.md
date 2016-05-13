# EntryRevamped

## What is EntryRevamped?

EntryRevamped is a way for python developers that use tkinter as their GUI toolkit to add a listener function to their entries. This means that the user can create a function that is called everytime the user types something into the entry widget. 

An example of a way to use EntryRevamped is:

```python
from EntryRevamped import EntryRevamped

def onchange(varname, elementname, mode):
	print("User typed " + entry.gettext()[:-1] + " in " + entry.getparam("name"))
	
def main():
	entry = EntryRevamped(listener=onchange)
	entry.pack()
	entry.addparam("name", "entry1")
	
if __name__ in '__main__':
	main()
```


