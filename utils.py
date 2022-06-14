# utils.py

def unique_str(s) -> str:
	r = '';
	for c in [*s]:
		if c not in r:
			r = r + c
	return r

def remove_non_alpha(s) -> str:
	r = ''
	for c in s:
		if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			r = r + c
	return r
