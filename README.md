# line-chatbot

## Table of Content
- [About](#about)
- [Installing](#installing)
- [Support](#support)
- [Latest Version of README](#latest-version-of-readme)

---

## About
  -

## Installing
เริ่มต้นจากการติดตั้งไลบรารี่ที่จำเป็นต่อการทำงานโดยใช้คำสั่งต่อไปนี้
```
git clone https://github.com/mahitriphop/line-chatbot.git
```
หลังจากนั้นให้เข้าไปยังโฟลเดอร์
```
cd ./line-chatbot
```
สุดท้ายติดติ้งไลบรารี่ทั้งหมดที่จำเป็น
```
pip install -r requirements.txt
```

## Installing Model
เราต้องไปติดตั้งจาก https://ollama.com/ หรือ https://ollama.com/download หลังจากติดตั้งตัวโปรแกรม ollama จะสามารถติดตั้งโมเดลได้โดยใช้คำสั่งดังต่อไปนี้
"โดยใช้คำสั่ง pull : Pull a model from a registry"

```
ollama pull llama3.2
```
หากเราติดตั้งสำเร็จเราสามารถทดสอบการทำงานของโมเดลโดยให้รัน cmd หรือ Terminal
```
ollama run llama3.2
```
---
## Output (New)

เรามีการเอกสารใช้ .pdf หรือ .png/.jpg โดยเรานำไปแปลงเป็นตาราง (table) เช่น .csv, .xlsm เป็นต้นโดยที่ในตอนนี้เราใช้วิธีการแปลงผ่านเว็บไซต์ `https://www.extracttable.com/` แล้วนำขอมูลที่ได้มา .csv นำไปใช้งานต่อ function ที่สร้างขึ้น `trans_table2vector.py` เพื่อทำการแปลงข้อมูลที่เป็น .csv ไปเป็น text แล้วจึงแปลงเป็นเวกเตอร์ (vector) สุดท้ายนำข้อมูลไปใช้งานบน vector database โดยใช้ embeddings model และนำไปใช้เป็นฐานข้อมูลให้ Chatbot อ้างอิงจาก context เหล่านี้     

**[ใช้งานได้]**   Q: สำหรับอายุ 31-35* แผน 15M เพศ M ค่าเบี้ยประกันเป็นเท่าใด  
A: 'ค่าเบี้ยประกันสำหรับอายุ 31-35* แผน 15M เพศ M คือ 29,400 บาท' 

**[ใช้งานไม่ได้]**   Q: เบี้ยประกันภัยมาตรฐานรายปี ของ Health Happy Kids เพศ M อายุ 31-35* แผน 15M ราคากี่บาท   
  A: 'จากข้อมูลที่ให้ไว้ เบี้ยประกันภัยมาตรฐานรายปี ของ AIA Health Happy Kids ยิ่งคิดส์ ยิ่งคุ้ม สำหรับอายุ 31-35* แผน 15M เพศ M ค่าเบี้ยประกัน 37,800 บาท'


**[ใช้งานได้]**   Q: เพศ M อายุ 31 แผน 15M ราคาเท่าไหร่  
  A: 'เราสามารถดูจากข้อมูลที่ให้มาได้ว่าค่าเบี้ยประกันภัยสำหรับวัยและแผนการอื่นๆ ของเพศ M ได้ดังนี้\n\n- แผน 15M เพศ M อายุ 31-35* ค่าเบี้ยประกัน 29,400 บาท\n- แผน 15M เพศ M อายุ 41-45* ค่าเบี้ยประกัน 36,000 บาท'
อาจเพราะ Data เป็นแบบนี้ด้วยครับ อันนี้พยายามสร้างเป็น text แล้วให้มันเรียนรู้ แต่ pattern มันคล้ายกันหมดเลยทำยาก


## Output (Old)

Data     : C:\Users\USERNAME\line-chatbot\demo\Files\Testing\pdf\medium.pdf  
Question : standardization คืออะไร

`'ขั้นตอนแรกของการวิเคราะห์ PCA คือการ Standardization เพื่อให้แต่ละตัวแปรมีผลต่อการวิเคราะห์เท่าๆ กัน โดยทำโดยลบค่าเฉลี่ยออกจากแต่ละตัวแปรแล้วหารด้วยมาตรฐานความผิดพลาด (Standard Deviation)'
`


---

## Latest Version of README
version 0.0.1 (6/12/25)
version 0.0.0 (6/9/25)
