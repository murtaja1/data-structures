if [ $1 == am ]
  then 
    git add .
    git commit -m 'Upgrade: update Linked list Tree and add another tree using python list'
fi
# stands for push 
if [ $2 == p ]
  then
    git push origin 
fi