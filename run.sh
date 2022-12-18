if [ $1 == am ]
  then 
    git add .
    git commit -m 'Upgrade: update sliding window algorithm'
fi
# stands for push 
if [ $2 == p ]
  then
    git push origin 
fi