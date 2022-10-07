# utils.py

from collections import OrderedDict
import re

def unique_str(s) -> str:
	return ''.join(OrderedDict.fromkeys(s).keys())

def remove_non_alpha(s) -> str:
	return re.sub(r'[^A-Z]', '', s)

if __name__ == "__main__":
	assert unique_str("aJDHJNDE1R1aUEJSBNNGDGaGa") == "aJDHNE1RUSBG"
	assert remove_non_alpha("1212.,-öoksuejJI-H8H00DööR!Jsjskljß") == "JIHHDRJ"
	assert unique_str(remove_non_alpha("1212.,-öoksuejJI-H8H00DööR!Jsjskljß")) == "JIHDR"
	print("Test ended ok.")
