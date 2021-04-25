# PhaseStream1

### Challenge
Decode ```2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904```  
The a 5-byte XOR key was used to create the ciphertext  
The clue was the flag format (CHTB{....})

### Analysis
- The ciphertext was identified as hexadecimal
- CipherText and Flag format table layouts the relationship between characters 
  
| CipherText | Flag Format |
| -----------| ------------|
|     2e     |      C      |
|     31     |      H      |
|     3f     |      T      |
|     27     |      B      |
|     02     |      {      |

### Using python terminal to test the XOR relationship between the two
```
>>> chr(int("2e", 16) ^ ord("C"))
'm'
>>> chr(int("31", 16) ^ ord("H"))
'y'
>>> chr(int("3f", 16) ^ ord("T"))
'k'
>>> chr(int("27", 16) ^ ord("B"))
'e'
>>> chr(int("2", 16) ^ ord("{"))
'y'
```
- int("2e", 16) => 2e is set to base16
- ord("C") => decimal value of the ASCII character
- int("2e", 16) ^ ord("C") => XOR'd both output from the operations above
- chr(int("2e", 16) ^ ord("C")) => returns the character from the XOR result 
### python script to decrypt the entire encoded string
### NOTE: Make you run your script with python3 because python2 does not accept the ```print(chr(j), end='')``` syntax 
```
decode.py

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


```


