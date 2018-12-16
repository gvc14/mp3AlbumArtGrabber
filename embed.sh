#!/bin/bash
IFS=$'\n'
while read imagename; do
  #statements
  base=$(basename -s .mp3 $imagename)
  newbase=${imagename%".mp3"}
  echo $newbase
  eyeD3 $imagename --add-image=$base.jpg:FRONT_COVER
  rm $base.jpg
done < list.txt
