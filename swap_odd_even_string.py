print("Enter the string : ")
string = str(input())
l=list(string)
s=""
for i in range(len(l)):
    if(i % 2 == 0):
        if(i+1<len(l)):
            s = s+l[i+1]
    else:
        s =s + l[i-1]
if(len(l)%2!=0):
    s=s+l[len(l)-1]
print(s)