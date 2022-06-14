# config.py

from tkinter import Tk
from wordlist import WordList

# Konstanten
ASSETS_DIR:str = "assets"
ICON_FILE:str = "icon.png"
WORDLIST_FILE:str = "wordlist.txt"
APP_TITLE:str = "Der kleine WÖRDL-[wordle.at]-Helfer"
DEBUG:bool = False

# Globale Variablen
TKROOT:Tk = None
WORDLIST:WordList = None
