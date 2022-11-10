from PIL import Image, ImageDraw
import random
mode = int(input('mode: ')) 
image = Image.open('temp.jpg') 
draw = ImageDraw.Draw(image) 
width = image.size[0] 
height = image.size[1] 
pix = image.load() 

if mode == 0: 
    for i in range(width): 
        for j in range(height): 
            a = pix[i,j][0] 
            b = pix[i,j][1] 
            c = pix[i,j][2] 
            S = (a+b+c)//3 
            draw.point((i,j),(S,S,S)) 
if mode == 1: 
    depth = int(input('depth: ')) 
    for i in range(width): 
        for j in range(height): 
            a = pix[i,j][0] 
            b = pix[i,j][1] 
            c = pix[i,j][2] 
            S = (a+b+c)//3 
            a = S+ depth 
            b = S+2*depth 
            c = S 
            draw.point((i,j),(a,b,c))

if mode == 2: 
    for i in range(width): 
        for j in range(height): 
            a = pix[i,j][0] 
            b = pix[i,j][1] 
            c = pix[i,j][2]  
            draw.point((i,j),(255-a,255-b,255-c))

if mode == 3:
    for i in range(width): 
        for j in range(height):
            rand=random.randrange (-100,100)

            a = pix[i,j][0] + rand
            b = pix[i,j][1] + rand
            c = pix[i,j][2] + rand
            if a > 255:
                a=255
            if b > 255:
                b=255
            if c > 255:
                c=255
            if a < 0:
                a=255
            if b < 0:
                b=255
            if c < 0:
                c=255
            draw.point((i,j),(255-a,255-b,255-c))

if mode == 4:
    for i in range(width): 
        for j in range(height):
            rand=random.randrange (-100,100)

            a = pix[i,j][0] + rand
            b = pix[i,j][1] * rand
            c = pix[i,j][2] - rand
            if a > 255:
                a=255
            if b > 255:
                b=255
            if c > 255:
                c=255
            if a < 0:
                a=255
            if b < 0:
                b=255
            if c < 0:
                c=255
            draw.point((i,j),(255-a,255-b,255-c)) 



image.save('ans.jpg', "JPEG") 
del draw
