from math import sqrt
from sys import stdout

letters=" .-:=+*#@"
letters= " .`-_':,;^=+/\"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q"
letters= " .-',^\|\<)vxls*I![te7juTJwy2F6qgV4gPZYO&U@HBNRQ"
letters=" ~=@#"
letters=".=#"


print(letters)

from PIL import Image
im = Image.open("photo.png")
size=im.size
data=list(im.getdata())
print((size,len(data)))

m=[99999,0]

for yy in range(0,size[1]):
    for xx in range(0,size[0]):
        #print(xx,yy)
        r,g,b=data[yy*size[0]+xx]
        l=sqrt(r*r+g*g+b*b)
        if l>m[1]: m[1]=l
        if l<m[0]: m[0]=l
        #print letters[l],
    
        
        
def outprint(thing,nospace=False):
        for t in thing:
            if nospace==False: stdout.write(t+" ")
            else: stdout.write(t)
    
#stdout.write=newthing        

outprint("     ",nospace=True)
outprint("00000000001111111111222222222233333333334444444444555555555566666666667777777777\n")
outprint("    ",nospace=True)
outprint("01234567890123456789012345678901234567890123456789012345678901234567890123456789\n")

for yy in range(0,size[1]):

    outprint("{:0>3d} ".format(yy),nospace=True)
    for xx in range(0,size[0]):
        #print(xx,yy)
        r,g,b=data[yy*size[0]+xx]
        l=sqrt(r*r+g*g+b*b)
        l2=(l-m[0])/(m[1]-m[0])
        #print letters[l],
        t=int(len(letters)*l2)
        if t<0: t=0
        if t>=len(letters): t=len(letters)-1
        outprint( str(letters[t]) )
    
    outprint("\n")
    #print()
        