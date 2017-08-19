num=2520;
for x in range(11,21):
    if(num%x==0):
        continue;
    else:
        div=num;
        sub=x;
        re=0;
        while(True):
            re=div%sub;
            if(re==0):
                break;
            else:
                div=sub;
                sub=re;
        multi=x/sub;
        num=num*multi;
print(num);
