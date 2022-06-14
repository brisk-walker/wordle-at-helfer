#!/usr/bin/python3

# main.py

import config
from wordlist import WordList
from guimain import GUIMain

def main():
	config.WORDLIST = WordList(config.ASSETS_DIR, config.WORDLIST_FILE)
	GUIMain(config.APP_TITLE, config.ASSETS_DIR, config.ICON_FILE)
	config.TKROOT.mainloop()

if __name__ == "__main__":
	main()
