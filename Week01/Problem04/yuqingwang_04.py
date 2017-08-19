def find():
    first=999;
    second=999;
    palin=0;
    fir=0;
    sec=0;
    while(second>sec and second>99):
        while(second>sec and second>99):
            product=first*second;
            if(str(product)==str(product)[::-1]):
                if(palin<product):
                    palin=product;
                    fir=first;
                    sec=second;
                    break;
            second=second-1;
        first=first-1;
        second=first;
        if(first*second<=palin):
            break;
    print(palin,"=",fir,'*',sec);
    return;
find();
