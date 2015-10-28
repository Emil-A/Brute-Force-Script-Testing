import itertools

def check_password(password):
	if ''.join(password) == "monkey03":
		return True
	else: return False

password_length = 6
characters = "abcdefghijklmnopqrstuvwxyz_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(3,10):
	gen = itertools.combinations_with_replacement(characters,i) 
	for password in gen: 
		print ''.join(password)                                                    
		if check_password(password):
			break