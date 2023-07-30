import base64, os, sys
import urllib.request as ur

f = ur.urlopen("https://raw.githubusercontent.com/EmanuelLopesS2/chuu-meme-nuke/main/chuu_image_b64")
chuu64 = f.read()

path= os.path.expanduser('~')

path = path+"\\Desktop\\chuuNuke\\ "

try:
    os.mkdir(path[:-1])
    
except:
    pass

try:
    os.mkdir(path)
    
except:
    pass

try:
    os.system("attrib +h "+path)
except:
    pass

chuunuke = base64.b64decode((chuu64))

loop=int(sys.argv[1])
print(loop)

for i in range(loop):
    with open(path+f"\chuu_{i}.jpg", "wb") as chuu:
        chuu.write(chuunuke)
        print(f"chuu_meme_{i} created")
print(f"{loop} of chuu meme photos created")
