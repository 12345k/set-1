year = int(input())

if(year%4==0 & year%100==0 & year%400):
    print("leap year")
else:
    print("not")