import pandas as pd
import numpy as np
import os

def card():
    bill_path = 'bill/이용대금명세서_이용상세내역.xls'
    df = pd.read_excel(bill_path)
    mile = 'Mile 1.8 대한항공 본인 828'
    welix = '웰릭스렌탈 하나카드 본인 0385'

    df.columns = ['거래일자', '가맹점명', '이용금액', '할부기간', '청구회차', '결제원금', '수수료', '이용혜택',
                 '혜택금액', '이용지역', '혜택구분', '결제후잔액', '포인트']

    mile_idx = df.index[df['거래일자'] == mile].tolist()[0]
    welix_idx = df.index[df['거래일자'] == welix].tolist()[0]

    mile_df = df[mile_idx:welix_idx]
    mile_df = mile_df[1:-1]

    welix_df = df[welix_idx:]
    welix_df = welix_df[1:-2]

    mile_sum = mile_df['결제원금'].sum()
    mile_sum = '{:,}'.format(mile_sum)



    print(mile_sum)






if __name__ == '__main__':
    card()