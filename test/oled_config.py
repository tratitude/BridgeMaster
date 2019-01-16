import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

left = 1    #x 
top=1       #y
FONT_SIZE=15
RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font=ImageFont.truetype("./DejaVuSansMono-Bold.ttf", FONT_SIZE)  #set font

def clsr(): #清空螢幕
    disp.begin()
    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
def partial_clsr(x,y):#部分清空 X=第幾個字 Y=第幾行
    if x>=14 :
        raise ValueError("x should <14")
    if y>=4 :
        raise ValueError("y should <4")
    x=left+(x*9)
    y=top+(FONT_SIZE*y)
    #draw.rectangle((left+(x*9),left+(x*9)+FONT_SIZE),(top+(16*y),top+(16*y)+FONT_SIZE), fill=0)
    draw.rectangle((x,y,x+9,y+FONT_SIZE), outline=0, fill=0)
    disp.image(image)
    disp.display()
    
def fline_print(x,y,string): #正常顏色  xy同上
    if (type(x) is not int) or (type(y) is not int):
        raise TypeError("x/y should be int")
    if x>=14 :
        raise ValueError("x should <14")
    if y>=4 :
        raise ValueError("y should <4")
    if type(string) is not str:
        raise TypeError ("should be string")
    x=left+(x*9)
    y=top+(FONT_SIZE*y)
    draw.text((x, y),string,font=font,fill=255)
    disp.image(image)
    disp.display()

def fline_reverse(x,y,string): #反白 xy同上
    if type(x) is not int:
        raise TypeError("x should be int")
    if x>=14:
        raise ValueError("x should <=14")
    if y>=4 :
        raise ValueError("y should <4")    
    if type(string) is not str:
        raise TypeError ("should be string")
    x=left+(x*9)
    y=top+(FONT_SIZE*y)
    draw.rectangle ([x,y,x+9,y+FONT_SIZE], fill=255,outline=None)   #上底色
    draw.text((x, y),string,font=font,fill=0)
    disp.image(image)
    disp.display()