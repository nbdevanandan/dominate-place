#!/bin/bash

msg="testing ig"
token=$(cat token.txt)

echo "$token" | gh auth login --with-token


for y in {0..39}; do
  for x in {0..69..5}; do
  
    python3 ~/dominate-place/replace.py $x $y
    
    cd ..
    cd amPlace_contribution
   
    git add .
    git commit -m "$msg"
    git push
    
    sleep 1
    gh pr create --title "If this works ${x}${y}" --body "testing testing "
    
    cd ..
    cd dominate-place
    
  done
done

