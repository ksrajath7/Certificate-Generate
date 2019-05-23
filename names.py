import xlrd

from PIL import Image, ImageDraw, ImageFont

file_location="names.xlsx"

font_type= ImageFont.truetype('arial.ttf',70)
#add ttf files in '.fonts' folder

workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
#sheet1

for i in range(sheet.nrows):
    name=sheet.cell_value(i,0)
    #names should be in first column
    name=name.capitalize()
    w,h=font_type.getsize(name)
    image= Image.open("template.jpg")
    draw=ImageDraw.Draw(image)
    draw.text(xy=((910),((1250-h)/2)),text=name,fill="#000000",font=font_type)

    image.save('foldername/{}.jpg'.format(name))
