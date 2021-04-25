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
		echo "The flag is $encoded_string";;

        h) echo "Usage: rotate_base64 -f FILENAME";;		  
		
	*) echo "Usage: rotate_base64 -f FILENAME";;
    esac
done
