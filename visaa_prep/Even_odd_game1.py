a=input().strip()
s=0
temp=(int(a))
for i in range(len(a)):
    r=temp%10
    s=s+r
    temp=temp//10
if (s%2==0):
    print("Vignesh")
else:
    print("Charan")
