#!/bin/bash

for y in {0..39..1}
do
  for x in {0..69..5}
  do
    echo $x $y
    python3 replace.py
  done
done