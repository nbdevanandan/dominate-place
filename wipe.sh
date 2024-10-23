#!/bin/bash

msg="testing ig"
token=$(cat token.txt)
url="https://${token}@github.com/nbdevanandan/amPlace_contribution.git"

echo "$token" | gh auth login --with-token
#git remote set-url origin "$url"

for y in {0..9}; do
  for x in {0..19..5}; do
  
    python3 ~/dominate-place/replace.py $x $y
    
    cd ..
    cd amPlace_contribution
    ls
   
    git add .
    git commit -m "$msg"
    git push $url main
    
    gh pr create --base main --head main --title "If this works" --body "testing testing"
    
    cd ..
    cd dominate-place
    
    sleep 5
  done
done

