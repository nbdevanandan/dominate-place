#!/bin/bash

msg="testing ig"
token=$(cat token.txt)
url="https://${token}@github.com/nbdevanandan/dominate-place.git"

echo "$token" | gh auth login --with-token
git remote set-url origin "$url"

for y in {0..9}; do
  for x in {0..19..5}; do
    python3 replace.py $x $y
    
    cd amPlace_contribution
    
    git add .
    git commit -m "$msg"
    git push $url main
    gh pr create --base main --head main --title "If this works" --body "testing testing"
    
    cd ..
    
    sleep 5
  done
done

