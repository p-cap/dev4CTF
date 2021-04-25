# PhaseStream1

### Challenge
Decode ```2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904```
The a 5-byte XOR key was used to create the ciphertext. The clue was the flag format (CHTB{....})

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

