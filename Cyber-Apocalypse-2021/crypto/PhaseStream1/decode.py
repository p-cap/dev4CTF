# Assigned the ciphertext and the key to a constat
ciphertext = "2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904"
key = "mykey"

# temp is used to store the characters from the ciphertext that are equivalent to 2 characters or 8-bytes
# Keep in mind, we have a hexadecimal encoded ciphertext
temp = ""

# flag is used to store the xor'd results from the ciphertext and key
flag = []

# single assists in iterating through the key
single = 0

# calculates how many times the key is repeated 
repititions = len(ciphertext) / 2 / len(key) 

# this stores the repeated key so we can XOR it against the ciphertext
key  = key * int(repititions) + (key[:int(len(ciphertext) / 2 % len(key))]) 

# iterates through each character in the ciphertext
for i in ciphertext:
	temp += i
	# the condition only stores 1 byte (or 2 character) from the ciphertext
	if len(temp) == 2:
		
		# stores the XOR'd results
		flag.append(int(temp, 16) ^ ord(key[single]))
		single += 1
		temp = ''
		continue

# prints the decoded text all in one line
for j in flag:
	print(chr(j), end="")
