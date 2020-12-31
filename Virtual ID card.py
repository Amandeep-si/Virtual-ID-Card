import random

import datetime
import qrcode

from PIL import Image, ImageDraw, ImageFont
import os

image = Image.new('RGB', (2300, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

os.system("Title: ID CARD Generator by Amandeep Singh")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
(x, y) = (250, 50)
company = 'KALEEN BHAIYA CARPET BUSINESS'

color = 'rgb(0, 151, 0)' # parrot color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), company, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (50, 250)
idno = random.randint(1000000000, 9000000000)
message = str('ID: ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

# For the Name
(x, y) = (50, 350)
name = input('Enter Your Full Name(In CAPITAL): ')

fname = str('Name: ' + str(name))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), fname, fill=color, font=font)
'''
# For the gender
(x, y) = (50, 350)
gender = input('Enter Your Gender: ')
fgender = str('Gender: ' + str(gender))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fgender, fill=color, font=font)

# For the Age
(x, y) = (400, 350)
age = int(input('Enter Your Age: '))
fage = str('Age: ' + str(age))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fage, fill=color, font=font)
'''
# For the DOB
(x, y) = (50, 450)
dob = input('Enter Your Date Of Birth(DD/MM/YYYY): ')
fdob = str('Date of Birth: ' + str(dob))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fdob, fill=color, font=font)

# For the Blood Group
(x, y) = (50, 550)
blood_group= input('Enter Your Blood Group: ')
flood_group = str('Blood Group: ' + str(blood_group))
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), flood_group, fill=color, font=font)

# For the Mob No
(x, y) = (50, 650)
No = int(input('Enter Your Mobile Number: '))

fNo = str('Mobile Number: ' + str(No))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fNo, fill=color, font=font)

# For the Address
(x, y) = (50, 750)
address = input('Enter Your Address: ')
faddress = str('Address: ' + str(address))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), faddress, fill=color, font=font)

# save the edited image

image.save(str(name) + '.png')


QR = qrcode.make(fname+'\n' +str('ID: ' + str(idno))+'\n'+ str('Date of Birth: ' + str(dob))+'\n'+flood_group+'\n'+fNo+'\n'+faddress)  # this info. is added in QR code, also add other things
QR.save(str(idno) + '.bmp')


ID = Image.open(name + '.png')
QR = Image.open(str(idno) + '.bmp')  # 25x25
dp = input('Enter Your Image name(It must be in png form and less than 180 x 180(horizontal and vertical): \n')
ID2 =Image.open(dp + '.png')
ID.paste(QR, (850, 150))
ID.paste(ID2, (1500,150))
ID.save(name + '.png')

print(('\nYour ID Card Successfully created in a PNG file ' + name + '.png'))