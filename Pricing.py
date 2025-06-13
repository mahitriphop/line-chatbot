#!/usr/bin/env python3
import pandas as pd
from modules.PricingEngine import PricingEngine
df = pd.read_csv('out.csv')
engine = PricingEngine(df)

orders = [
        {'age': 15, 'Class': '15M', 'gender': 'M', 'qty': 1},
        {'age': 15, 'Class': '1M',  'gender': 'F', 'qty': 3},
        {'age': 18, 'Class': '15M', 'gender': 'F', 'qty': 2},
    ]

# รอแก้ไข เพราะ ไม่เป็นสิ่งที่ทั่วไป 
def age_to_range(age: int) -> str:
    if 11 <= age <= 15:
        return '11 ถึง15'
    elif 16 <= age <= 20:
        return '16 ถึง20'
    else:
        raise ValueError(f"age {age} ไม่อยู่ในช่วงที่รองรับ")
result = engine.calc_orders(orders, age_to_range)



print(result.to_string(index=False))
print(f"\nยอดรวมทั้งหมด: {result['cost'].sum():,.2f} บาท")