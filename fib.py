for i in range (100,1000):
 ori=i
 rev=0
while (i>0):
 digit=i%10
rev=rev*10+digit
i=i//10
if(rev==ori):
  print(ori)
