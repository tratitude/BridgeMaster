# !/usr/bin/python 
# coding:utf-8 
import time
import sys
import os
from datetime import datetime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_SSD1306

FONT_SIZE = 14

def getCPUTemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace('\'',chr(0xB0)).replace("\n",""))

disp = Adafruit_SSD1306.SSD1306_128_64(rst=0)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

font=ImageFont.truetype("./ARIALUNI.TTF", FONT_SIZE)  #注意字型路徑是否正確

try:
	print('按下 Ctrl-C 可停止程式')
	while True:
		load = os.getloadavg()

		draw.rectangle((0, 0, width, height), outline=0, fill=0)
		draw.text((0, 0), '日期: {}'.format(time.strftime("%Y/%m/%d")),  font=font, fill=255)
		draw.text((0, FONT_SIZE-1), '時間: {}'.format(time.strftime("%H:%M:%S")), font=font, fill=255)
		draw.text((0, 2*FONT_SIZE-1), '系統負載: {}, {}, {}'.format(load[0], load[1], load[2]),  font=font, fill=255)
		draw.text((0, 3*FONT_SIZE-1), 'CPU溫度: {}'.format(getCPUTemperature()),  font=font, fill=255)
		draw.text((0, 4*FONT_SIZE-1), '--------',  font=font, fill=255)
		disp.image(image)
		disp.display()
		time.sleep(0.2)
except KeyboardInterrupt:
	print('關閉程式')
finally:
	disp.clear()
	disp.display()