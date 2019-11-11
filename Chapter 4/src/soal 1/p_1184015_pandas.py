# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:00:12 2019

@author: Ahmad Agung Tawakkal
"""

import pandas

def bacalistpandas():
    df = pandas.read_csv('1184015.csv')
    print(df)

def bacadictpandas():
    df = pandas.read_csv('1184015.csv')
    uji = pandas.DataFrame.from_dict(df)
    print(uji)
    
def standartanggal():
    df = pandas.read_csv('1184015.csv', parse_dates=['ttl'])
    print(df)

def changeindexcol():
    df = pandas.read_csv('1184015.csv', index_col='npm')
    print(df)

def renameatt():
    df = pandas.read_csv('1184015.csv',
            header=0, 
            names=['Nomor Induk Mahasiswa', 'Name','Class', 'Tanggal Lahir'])
    print(df)

def write():
    df = pandas.read_csv('data.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('p_1184015_pandas_baru.csv')    