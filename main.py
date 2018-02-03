import qrcode
import random
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

# how many to generate?
COUNT = 10

URL = 'https://mgo2.18jian.cn/index.php/Wechat/Drivers/goto_store?driver_code='
NUMBER_MIN = 10000000
NUMBER_MAX = 99999999
OUTPUT_DIR_NAME = 'output'
NUMBER_OFFSET_X = 195
NUMBER_OFFSET_Y = 457
NUMBER_SIZE = 25
FONT_FILE = "Helvetica.dfont"
CORRECT = qrcode.constants.ERROR_CORRECT_L
QRCODE_VERSION=1
QRCODE_BOX_SIZE=5
QRCODE_BORDER=12

# create dir
OUTPUT_DIR_FULL_PATH = os.path.join(FILE_PATH, OUTPUT_DIR_NAME)
try:
	os.mkdir(OUTPUT_DIR_FULL_PATH)
except OSError:
	pass

for i in range(10):
	# first image path, to check exists
	img_path = None
	randnum = 0

	# random number generate
	while True:
		randnum = random.randint(NUMBER_MIN, NUMBER_MAX)
		qr = qrcode.QRCode(
			version=QRCODE_VERSION,
			error_correction=CORRECT,
			box_size=QRCODE_BOX_SIZE,
			border=QRCODE_BORDER)
		qr.add_data(URL + str(randnum))
		qr.make(fit=True)
		img_path = os.path.join(OUTPUT_DIR_FULL_PATH, 'img_' + str(randnum) + '.png')
		
		# file not exist, random number ok
		if not os.path.isfile(img_path):
			break

	img = qr.make_image()
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(FONT_FILE, NUMBER_SIZE)
	draw.text((NUMBER_OFFSET_X, NUMBER_OFFSET_Y), str(randnum), font=font)

	print 'Output Number:%s to "%s"' % (randnum, img_path)
	img.save(img_path)


