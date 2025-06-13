#!/usr/bin/env python3
# pricing_engine.py

import pandas as pd
from typing import Callable, List, Dict

class PricingEngine:
    def __init__(self, price_wide: pd.DataFrame, key_cols: List[str] = ['year','Class']):
        """
        - price_wide: DataFrame แบบ wide (หลายคอลัมน์ราคา เช่น 'F','M', ...)
        - key_cols: ชื่อคอลัมน์เงื่อนไขหลัก เช่น ['year','Class']
        """
        # 1) แปลง wide →  long (unpivot)
        value_vars = [c for c in price_wide.columns if c not in key_cols]
        self.price_table = price_wide.melt(
            id_vars=key_cols,
            value_vars=value_vars,
            var_name='gender',
            value_name='price'
        )

    def calc_orders(
        self,
        orders: List[Dict],
        age_to_range: Callable[[int], str],
        key_cols: List[str] = ['year','Class','gender']
    ) -> pd.DataFrame:
        """
        - orders: List of dicts แต่ละ dict ต้องมี keys: 'age','Class','gender','qty'
        - age_to_range: ฟังก์ชันแปลง int age → ช่วง text (matching price_table.year)
        - คืน DataFrame ที่มีคอลัมน์ [*key_cols, 'qty','price','cost']
        """
        # สร้าง DataFrame ของ orders
        df_o = pd.DataFrame(orders)

        # แปลง age → ช่วงปี แล้ว drop 'age'
        if 'age' in df_o.columns:
            df_o['year'] = df_o['age'].apply(age_to_range)
            df_o.drop(columns=['age'], inplace=True)

        # เช็คว่าคีย์ครบ
        missing_keys = set(key_cols) - set(df_o.columns)
        if missing_keys:
            raise KeyError(f"Orders ต้องมีคอลัมน์: {missing_keys}")

        # merge กับตารางราคา
        df = df_o.merge(self.price_table, on=key_cols, how='left')
        if df['price'].isna().any():
            bad = df[df['price'].isna()]
            raise ValueError(f"ไม่พบราคาสำหรับ:\n{bad}")

        # คำนวณ cost
        df['cost'] = df['price'] * df['qty']
        return df

