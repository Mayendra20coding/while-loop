n=int(input('please enter a number'))
sum=0
temp=n
while temp >0:
 digit=temp%10
 sum+=digit**4
 temp//=10
if n==sum:
 print('this is a armstrong number')
else:
 print('this is not a armstrong number')