if [ $1 == am ]
  then 
    git add .
    git commit -m 'Upgrade: add sorting selection, insertion and bubble methods'
fi
# stands for push 
if [ $2 == p ]
  then
    git push origin 
fi