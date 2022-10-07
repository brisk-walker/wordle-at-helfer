# gui_main.py

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import os
import utils
import config

class GUIMain:

	def __init__(self, title:str, dir:str, iconfilename:str):
		root = Tk()
		config.TKROOT = root
		root.title(title)
		root.resizable(False, False)
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		root.iconphoto(False, PhotoImage(file=os.path.join(os.getcwd(), dir, iconfilename)))
		mainframe = ttk.Frame(root, padding=(5))
		mainframe.grid(column=0, row=0, sticky=(N,W,E,S), padx=5, pady=5)
		# Zeile 0
		ttk.Label(mainframe, text="Nicht Vorkommende (grau):").grid(column=0, row=0, sticky=E, padx=5, pady=5)
		self.knvletters = StringVar(name='K')
		self.firstentry = ttk.Entry(mainframe, width=20, textvariable=self.knvletters)
		self.firstentry.grid(column=1, row=0, columnspan=5, sticky=(W,E), pady=5)
		self.knvletters.trace_add('write', self.trace_knvletters)
		# Zeile 1
		ttk.Label(mainframe, text="Buchstabe Nr.:").grid(column=0, row=1, sticky=E, padx=5, pady=5)
		for i in range(5):
			ttk.Label(mainframe, text=str(i+1), anchor="center").grid(column=i+1, row=1, sticky=(W), pady=5)
		# Zeile 2
		ttk.Label(mainframe, text="An richtiger Position (grün/rot):").grid(column=0, row=2, sticky=E, padx=5, pady=5)
		self.cletter = []
		for i in range(5):
			self.cletter.append(StringVar(name='C'+str(i)))
			ttk.Entry(mainframe, width=2, textvariable=self.cletter[i]).grid(column=i+1, row=2, sticky=(W), pady=5)
			self.cletter[i].trace_add('write', self.trace_cletter)
		# Zeile 3
		ttk.Label(mainframe, text="An falscher Position (gelb/blau):").grid(column=0, row=3, sticky=E, padx=5, pady=5)
		self.fletters = []
		for i in range(5):
			self.fletters.append(StringVar(name='F'+str(i)))
			ttk.Entry(mainframe, width=4, textvariable=self.fletters[i]).grid(column=i+1, row=3, sticky=(W,E), pady=5)
			self.fletters[i].trace_add('write', self.trace_fletters)
		# Zeile 4
		ttk.Button(mainframe, text="NEU", command=self.click_neu).grid(column=0, row=4, sticky=(W,E), padx=5, pady=5)
		ttk.Button(mainframe, text="START", command=self.click_start).grid(column=1, row=4, columnspan=5, sticky=(W,E), pady=5)
		# Zeile 5
		ttk.Label(mainframe, text="Lösungsvorschläge:", anchor="center").grid(column=0, row=5, columnspan=6, sticky=(W,E))
		# Zeile 6
		self.textbox = scrolledtext.ScrolledText(mainframe, width=40, height=10, wrap='word')
		self.textbox.grid(column=0, row=6, columnspan=6, sticky=(W,E), pady=5)
		self.textbox['state'] = 'disabled'
		root.bind("<Return>", self.click_start)
		self.firstentry.focus()

	def click_start(self, *args):
		# Suche
		searchresult = config.WORDLIST.dosearch(self.get_knvletters(), 
			self.get_cletter_array(), self.get_fletters_array(), self.get_unique_fletters_array())
		# Ergebnis anzeigen
		self.textbox['state'] = 'normal'
		self.textbox.delete("1.0","end") 
		self.textbox.insert("1.0",searchresult)
		self.textbox['state'] = 'disabled'
		self.firstentry.focus()

	def click_neu(self, *args):
		# Alle Felder löschen
		self.knvletters.set("")
		for i in range(5):
			self.cletter[i].set("")
			self.fletters[i].set("")
		self.textbox['state'] = 'normal'
		self.textbox.delete("1.0","end")
		self.textbox['state'] = 'disabled'
		self.firstentry.focus()

	def trace_cletter(self, *args):
		index = int(args[0][1:])
		if len(self.cletter[index].get()) > 0:
			self.cletter[index].set(utils.remove_non_alpha(self.cletter[index].get().upper()[0]))

	def trace_fletters(self, *args):
		index = int(args[0][1:])
		self.fletters[index].set(utils.remove_non_alpha(utils.unique_str(self.fletters[index].get().upper())))

	def trace_knvletters(self, *args):
		self.knvletters.set(utils.remove_non_alpha(utils.unique_str(self.knvletters.get().upper())))

	def get_fletters_array(self) -> list:
		# Liste der (ggf. mehreren) Buchstaben "an falscher Pos."
		r = []
		for i in range(5):
			r.append(self.fletters[i].get())
		return r

	def get_cletter_array(self) -> list:
		# Liste der bislang vorhandenen Lösungen
		r = []
		for i in range(5):
			r.append(self.cletter[i].get())
		return r

	def get_unique_fletters_array(self) -> list:
		# Eindeutige Liste aller "an falscher Pos."
		list1 = []
		for i in range(5):
			if len(self.fletters[i].get()) > 0:
				for c in [*(self.fletters[i].get())]:
					list1.append(c)
		r = []
		for x in list1:
			if x not in r:
				r.append(x)
		return r
	
	def get_knvletters(self) -> str:
		# Alle "nicht vorkommenden" Buchstaben, aber 
		# entferne vorher ggf. vorhandene "an falscher Pos."
		return ''.join(set(self.knvletters.get()) - set(self.get_unique_fletters_array()))
