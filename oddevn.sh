echo "this script will check even and odd numbers from 0 to 10"
for (( i=0;i<10;i++ ))
do
if [ $(($i%2)) -eq 0 ]
then
echo "$i is even number"
else
echo "$i is odd number"
fi
Done
