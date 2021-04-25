# Nintendo Base64

### Challenge Description
Aliens are trying to cause great misery for the human race by using our own cryptographic technology to encrypt all our games.
Fortunately, the aliens haven't played CryptoHack so they're making several noob mistakes. Therefore they've given us a chance to recover our games and find their flags. 
They've tried to scramble data on an N64 but don't seem to understand that encoding and ASCII art are not valid types of encryption!
This challenge will raise 33 euros for a good cause

### output.txt => file downloaded from the CTF challenge
```
            Vm                                                   0w               eE5GbFdWW         GhT            V0d4VVYwZ
            G9              XV                                   mx              yWk    ZOV       1JteD           BaV     WRH
                            YW                                   xa             c1              NsWl dS   M1   JQ WV       d4
S2RHVkljRm  Rp UjJoMlZrZH plRmRHV m5WaVJtUl hUVEZLZVZk   V1VrZFpWMU  pHVDFaV1Z  tSkdXazlXYW   twdl   Yx    Wm Fj  bHBFVWxWTlZ
Xdz     BWa 2M xVT     FSc  1d   uTl     hi R2h     XWW taS     1dG VXh     XbU ZTT     VdS elYy     cz     FWM    kY2VmtwV2
JU       RX dZ ak       Zr  U0   ZOc2JGWmlS a3       BY V1       d0 YV       lV MH       hj RVpYYlVaVFRWW  mF lV  mt       3V
lR       GV 01 ER       kh  Zak  5rVj   JFe VR       Ya Fdha   3BIV mpGU   2NtR kdX     bWx          oT   TB   KW VYxW   lNSM
Wx       XW kV kV       mJ  GWlRZ bXMxY2xWc 1V       sZ  FRiR1J5VjJ  0a1YySkdj   RVpWVmxKV           1V            GRTlQUT09
```
### Analysis
- Looking at the ASCII art saying "nintendo64x8", the characters are based64 encoded. 
- "x8" meant that the encoded text was encoded 8 times
- Below, I created a bash script that decodes the text inside the ```output.txt``` 
```
#!/bin/bash

if [[ -z $1 ]] 
then
	echo "Usage: rotate_base64 -f FILENAME"
	echo "== Decodes base64 encoded string 8 times =="
fi

while getopts f:h flag
do
    case "${flag}" in
        f) filename=${OPTARG}
            encoded_string=$(cat $filename)
	for d in {1..8}
	do 
	encoded_string=$(echo $encoded_string | base64 -d)
	done
	echo "The flag is $encoded_string"
	;;

        h) echo "Usage: rotate_base64 -f FILENAME";;		  
		
        *) echo "Usage: rotate_base64 -f FILENAME";;
    esac
done
```
