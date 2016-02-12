from math import sqrt
from sys import stdout, argv

letters=" .-:=+*#@"
letters= " .`-_':,;^=+/\"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q"
letters= " .-',^\|\<)vxls*I![te7juTJwy2F6qgV4gPZYO&U@HBNRQ"
letters=" ~=@#"
letters="-+#"

WIDTH_LIMIT=80


from PIL import Image
im = Image.open(argv[1])
oldsize=im.size

if len(argv)==2: ratio=1.0
else: ratio=float(argv[2])

size=[int(float(oldsize[0])*ratio),int(float(oldsize[1])*ratio)]

im=im.resize(size, Image.ANTIALIAS)

#for d in dir(im):
#    print((d,getattr(im,d)))



data=list(im.getdata())

print("picture      :", argv[1])
print("scale        :", str(ratio))
print("original size:", oldsize)
print("new size     :", size)
print("total pixels :", len(data))
print("letters      :", letters)

print()


m=[99999,0]

##calculate luminosity

for yy in range(0,size[1]):
    for xx in range(0,size[0]):
        #print(xx,yy)
        i=yy*size[0]+xx
        #print(i)
        r,g,b=data[i]
        l=sqrt(r*r+g*g+b*b)
        if l>m[1]: m[1]=l
        if l<m[0]: m[0]=l
        #print letters[l],
    
##overblown print function        
        
def outprint(thing,nospace=False):
        for t in thing:
            if nospace==False: stdout.write(t+" ")
            else: stdout.write(t)
    
#stdout.write=newthing        
##function for printing using rows and columns includes column break and row breaking

def draw_columns(start=0,end=80,rowbreak=80,**kwargs):

    num_breaks=0
    

    for yy in range(0,HEIGHT):
    
        if yy%rowbreak==0:
        
            num_breaks+=1
            
            ##rulers
            
            stdout.write("\n")
            stdout.write("PAGEBREAK")                
                
            stdout.write("\n")
            stdout.write("Columns "+str(start+1)+" to "+str(end)+" top row is "+str(yy+1)+" rowbreak: "+str(num_breaks))
            
            if "pagenum" in kwargs:
                stdout.write("\n")
                stdout.write("Page - "+str(kwargs.get("pagenum")))
                
            stdout.write("\n")
            stdout.write("\n")
            outprint("      ",nospace=True)
            for a in range(start,end): b=a+1; outprint(str(int(b/100)%100))
            stdout.write("\n")
            outprint("      ",nospace=True)
            for a in range(start,end): b=a+1; outprint(str(int(b/10)%10))
            stdout.write("\n")
            outprint("      ",nospace=True)
            for a in range(start,end): b=a+1; outprint(str(int(b)%10))
            stdout.write("\n ")
            outprint("    ",nospace=True)
            outprint("/         /         /         /         /         /         /         /         /         /         /         /         /         /         /         /         /         "[start:end])
            stdout.write("\n ")
            ##adapted for width chopping
    
    
        outprint("{:0>3d} ".format(yy+1),nospace=True)
        if yy%2==0: stdout.write(" ")
        
        for xx in range(start,end):
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
        

WIDTH_LIMIT=80
ROW_BREAK=45

if size[0]<=WIDTH_LIMIT: WIDTH_LIMIT=size[0]
HEIGHT=size[1]

start=0
end=WIDTH_LIMIT
if size[0]<WIDTH_LIMIT: end=size[0]

p=0

while (start<size[0]):

    p+=1
    draw_columns(start=start,end=end,rowbreak=ROW_BREAK,pagenum=p) ##pagenum is a kwarg - aarrrrgh!
    end+=WIDTH_LIMIT
    if end>size[0]: end=size[0]
    start+=WIDTH_LIMIT
    

