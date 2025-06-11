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

Data     : C:\Users\USERNAME\line-chatbot\demo\Files\Testing\pdf\medium.pdf
Question : standardization คืออะไร

`'ขั้นตอนแรกของการวิเคราะห์ PCA คือการ Standardization เพื่อให้แต่ละตัวแปรมีผลต่อการวิเคราะห์เท่าๆ กัน โดยทำโดยลบค่าเฉลี่ยออกจากแต่ละตัวแปรแล้วหารด้วยมาตรฐานความผิดพลาด (Standard Deviation)'
`

---

## Latest Version of README

version 0.0.0
