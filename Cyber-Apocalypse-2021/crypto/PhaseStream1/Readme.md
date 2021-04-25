# PhaseStream1

### Challenge
Decode ```2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904```
The a 5-byte XOR key was used to create the ciphertext. The clue was the flag format (CHTB{....})

### Analysis
- The ciphertext was identified as hexadecimal
- Using the flag format and the ciphertext, I made a relation between the two to produce the key
- CipherText and Flag format table
  
| CipherText | Flag Format |
| -----------| ------------|
|     2e     |      C      |
|     31     |      H      |
|     3f     |      T      |
|     27     |      B      |
|     02     |      {      |

