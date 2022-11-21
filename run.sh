if [ $1 == am ]
  then 
    git add .
    git commit -m 'Upgrade: add more methods to binary search tree'
fi
# stands for push 
if [ $2 == p ]
  then
    git push origin 
fi