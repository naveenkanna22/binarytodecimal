a=int(input())
bin1=0
pv=1
while(a>0):
    n=a%2
    bin1=n*pv+bin1
    pv=pv*10
    a=a//2
print(bin1)
