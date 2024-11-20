import pandas as pd

# connect postgresql To connect to PostgreSQL using Python, you can use the `psycopg2` library. Here's an example of how to do it:
# Sure! Below is an example of how to connect to PostgreSQL using Python and perform some basic operations with a DataFrame.
# First, install the psycopg2 library if you haven't already:
# pip install psycopg2-binary

from sqlalchemy import create_engine

# Connect to PostgreSQL

engine = create_engine('postgresql+psycopg2://postgres:Sap12345@oracle:5432/postgres')

sql = """
select investor_id, investor_name, investor_rnk, stock_rnk, market, stock_code, stock_name, sector_name,
	max(case when date_seq = 20 then invest_amt end) as day1,
	max(case when date_seq = 19 then invest_amt end) as day2,
	max(case when date_seq = 18 then invest_amt end) as day3,
	max(case when date_seq = 17 then invest_amt end) as day4,
	max(case when date_seq = 16 then invest_amt end) as day5,
	max(case when date_seq = 15 then invest_amt end) as day6,
	max(case when date_seq = 14 then invest_amt end) as day7,
	max(case when date_seq = 13 then invest_amt end) as day8,
	max(case when date_seq = 12 then invest_amt end) as day9,
	max(case when date_seq = 11 then invest_amt end) as day10,
	max(case when date_seq = 10 then invest_amt end) as day11,
	max(case when date_seq = 9 then invest_amt end) as day12,
	max(case when date_seq = 8 then invest_amt end) as day13,
	max(case when date_seq = 7 then invest_amt end) as day14,
	max(case when date_seq = 6 then invest_amt end) as day15,
	max(case when date_seq = 5 then invest_amt end) as day16,
	max(case when date_seq = 4 then invest_amt end) as day17,
	max(case when date_seq = 3 then invest_amt end) as day18,
	max(case when date_seq = 2 then invest_amt end) as day19,
	max(case when date_seq = 1 then invest_amt end) as day20,
	sum(invest_amt) as total
from analysis.t_20days_investor_big_invest_stock
group by investor_id, investor_name, investor_rnk, stock_rnk, market, stock_code, stock_name, sector_name
"""

df = pd.read_sql_query(sql, engine)

# df 에서 day20 에 해당하는 값이 10000 이 넘는 데이터만 필터링 하자
df2 = df[df['day20'] > 10000]


