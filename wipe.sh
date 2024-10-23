#!/bin/bash

msg="testing ig"
token=$(cat token.txt)

echo "$token" | gh auth login --with-token
#git remote set-url origin "$url"

for y in {0..9}; do
  for x in {0..19..5}; do
  
    python3 ~/dominate-place/replace.py $x $y
    
    cd ..
    cd amPlace_contribution
   
    git add .
    git commit -m "$msg"
    git push
    
    gh pr create --title "If this works" --body "testing testing"
    
    cd ..
    cd dominate-place
    
    sleep 1
  done
done

