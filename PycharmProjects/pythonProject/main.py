print("hello")
i=int(input("enter numbers to check"))
max=0
imax=0
bmax=0
ibmax=0
mone=0
while i!=0:
    mone+=1
    if i>max:
        bmax=max
        ibmax=imax
        max=i
        imax=mone
    if i>bmax and i<max:
        bmax=i
        ibmax=mone
    i = int(input("enter numbers to check"))

print("before max:",bmax)
print("place before max:", ibmax)
































