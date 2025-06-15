#!/usr/bin/env python3
import pandas as pd
class TableToContext:
    def __init__(self, filepath):
        self.df = self.ToDataFrame(filepath)

    def ToDataFrame(self, filepath):
        df = pd.read_csv(filepath, header=1)
        df.columns = ['year', '1M_M', '1M_F', '5M_M', '5M_F', '15M_M', '15M_F', '25M_M', '25M_F']
        
        df = pd.melt(df, id_vars=['year'], var_name='Category', value_name='Value')
        df[['Class', 'Gender']] = df['Category'].str.extract(r'(\d+M)_(M|F)')
        # label mapping

        
        df['year'] = (
        df['year']
        .astype(str)
        .str.replace(r'["\',*]', '', regex=True)   
        .str.replace(r'\s+', ' ถึง', regex=True)    
    )
        df['Value'] = df['Value'].str.replace(',', '').astype(float)
        df = df.pivot_table(index=['year', 'Class'], columns='Gender', values='Value').reset_index()
        df.columns.name = None

        return df
    def Table2Context(self, template):

        """
        template: str, e.g. "อายุ {year} แผน {Class} เพศ {gender} เบี้ย {Value:,.0f} บาท"
        """
        df = self.df.melt(id_vars=['year', 'Class'], value_vars=['M', 'F'],
                              var_name='gender', value_name='Value')

        # map gender เป็นคำไทย
        gender_map = {'M': 'ชาย', 'F': 'หญิง'}
        df['gender'] = df['gender'].map(gender_map)


        return df.apply(
            lambda row: template.format_map(row.to_dict()),
            axis=1
        ).tolist()