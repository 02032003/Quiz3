def main():
fac1=int(input())
fac2=int(input())
cont=0

if(fac1>0):
    if(fac2%2!=0):
        cont=cont+fac1
        print(fac1,fac2)
    else:
        print(fac1,fac2)
    while(fac2!=1):
        fac1*=2
        fac2=fac2//2
        if(fac2%2!=0):
            cont=cont+fac1
        print(fac1,fac2)
    print(cont)
else:
    print(0)


if __name__=='__main__':
    main()
