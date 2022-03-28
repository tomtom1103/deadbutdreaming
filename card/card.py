import pandas as pd
import numpy as np
import os

class Card:

    def __init__(self):
        bill_path = 'bill/이용대금명세서_이용상세내역.xls'
        df = pd.read_excel(bill_path)
        self.mile = 'Mile 1.8 대한항공 본인 828'
        self.welix = '웰릭스렌탈 하나카드 본인 0385'
        self.mile_short = 'Mile 1.8 대한항공'
        self.welix_short = '웰릭스렌탈 하나카드'

        df.columns = ['거래일자', '가맹점명', '이용금액', '할부기간', '청구회차', '결제원금', '수수료', '이용혜택',
                      '혜택금액', '이용지역', '혜택구분', '결제후잔액', '포인트']

        self.date = df['거래일자'][1]

        mile_idx = df.index[df['거래일자'] == self.mile].tolist()[0]
        welix_idx = df.index[df['거래일자'] == self.welix].tolist()[0]

        mile_df = df[mile_idx:welix_idx]
        self.mile_df = mile_df[1:-1]

        welix_df = df[welix_idx:]
        self.welix_df = welix_df[1:-2]

        mile_sum = mile_df['결제원금'].sum()
        welix_sum = welix_df['결제원금'].sum()
        total_sum = mile_sum + welix_sum

        self.mile_sum = '{:,}'.format(mile_sum)
        self.welix_sum = '{:,}'.format(welix_sum)
        self.total_sum = '{:,}'.format(total_sum)

    def main_menu(self):
        recap = (
        f'''
        {self.date}
        {self.mile}: {self.mile_sum} 원
        {self.welix}: {self.welix_sum} 원
        '''
        )
        print(recap)

        choice = int(input(
        """
        ------------Main Menu------------
        1. Mile 1.8 상세내역               |   
        2. Welix 상세내역                  |   
        ------------Main Menu------------
        >> """

        ))

        if choice == 1:
            mile()
        elif choice == 2:
            welix()

    def classmile(self):
        mile_df = self.mile_df
        mile_short = self.mile_short
        date = self.date
        query = input(
        f"""
        --------------------
        {mile_short} 의 결제내역 중 가맹점명을 입력하세요. (전체내역은 enter)
        ex. 쿠팡, APPLE, 넷플릭스, 택시
        --------------------
        >>"""
        )
        query_sum = mile_df.loc[mile_df['가맹점명'].str.contains(f'{query}'), '결제원금'].sum()
        query_sum = '{:,}'.format(query_sum)

        print(
        f"""
        ********************
        {mile_short} - {query} 에 소비한 금액: {query_sum} 원
        ********************
        """
        )
        select = int(input(
        f"""
        --------------------
        {mile_short}에서 다른 가맹점을 찾으려면 1, 메인메뉴로 돌아가려면 2를 입력하세요.
        --------------------
        >>"""
        ))

        if select == 1:
            thomas.classmile()
        elif select == 2:
            thomas.main_menu()

    def classwelix(self):
        welix_df = self.welix_df
        welix_short = self.welix_short
        date = self.date
        query = input(
        f"""
        --------------------
        {welix_short} 의 결제내역 중 가맹점명을 입력하세요. (전체내역은 enter)
        ex. 우아한형제들, 코엑스, 택시, 쿠팡, 네이버, TOSS
        --------------------
        >>"""
        )
        query_sum = welix_df.loc[welix_df['가맹점명'].str.contains(f'{query}'), '결제원금'].sum()
        query_sum = '{:,}'.format(query_sum)

        print(
        f"""
        ********************
        {welix_short} - {query} 에 소비한 금액: {query_sum} 원
        ********************
        """
        )
        select = int(input(
        f"""
        --------------------
        {welix_short}에서 다른 가맹점을 찾으려면 1, 메인메뉴로 돌아가려면 2를 입력하세요.
        --------------------
        >>"""
        ))

        if select == 1:
            thomas.classwelix()
        elif select == 2:
            thomas.main_menu()


def mile():
    thomas.classmile()
    thomas.main_menu()

def welix():
    thomas.classwelix()
    thomas.main_menu()

if __name__ == '__main__':
    thomas = Card()
    thomas.main_menu()