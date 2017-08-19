a=1;

b=1;

sum=0;

while (b<4000000):
    c=b;
    b=a+b;
    a=b;
    if(b%2==0):
        sum=sum+b;

print (sum);
