#!/usr/bin/env python3
from modules.TableToContext import TableToContext
from modules.PDFBuilder import PDFBuilder
import pandas as pd

filepath = 'g_testing\Testing\data\csv\eng_test.csv'
template = "อายุ {year} แผน {Class} เพศ {gender} เบี้ยประกัน {Value:,.0f} บาท"
font_path = 'modules\THSarabunNew.ttf'
# สร้าง object ผ่าน class TableToContext
table = TableToContext(filepath)

# หากต้องการดูข้อมูลที่เป็น DataFrame สามารถเรียกใช้ method ToDataFrame
table = table.ToDataFrame(filepath=filepath) 

#lines = table.Table2Context(template)

#print(table.to_csv('out.csv', index=False))


# export (pdf)

# version 0.0.1

#(PDFBuilder(font_path=font_path)
#    .setup()
#    .add_lines(lines=lines)
#    .save("test.pdf")
#    .execute())

# version 0.0.0

# PDF = PDFBuilder(font_path=font_path)
# SETUP = PDF.setup()
# add_line = PDF.add_lines(lines=lines)
# output = PDF.save(filename='test.pdf')

