if [ "$1" == am ]
  then 
    git add .
    git commit -m 'Upgrade: add Linear and binary search'
  fi
# stands for push 
if [ "$2" == p ]
  then
    git push origin 
  fi