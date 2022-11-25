if [ $1 == am ]
  then 
    git add .
    git commit -m 'Upgrade: add insertion in AVL tree'
fi
# stands for push 
if [ $2 == p ]
  then
    git push origin 
fi