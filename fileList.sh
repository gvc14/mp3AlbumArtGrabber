#!/bin/sh
rm -f names.txt
fileType=$1
find . -type f -name "*.$1" > list.txt
while read j; do
name=$(basename -s .$1 "$j")
#python2 img.py --search "$name" --directory "." -nm "$name"
echo $name>>names.txt
done < list.txt
