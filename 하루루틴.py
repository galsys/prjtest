# public.sys_configuration 테이블의 
""" 
1. 기준일 업데이트
update public.sys_configuration
set date_value = '20241126'
where conf_group = 'SYSTEM'
and conf_name = 'BASE_DATE'

아래 건 삭제생성이 아니라. 하루하루 건건이 추가하는 것으로 변경 필요.
2. 테이블 삭제
drop table analysis.t_20days_investor_big_invest_stock;

3. 테이블 생성
create table analysis.t_20days_investor_big_invest_stock as 
SELECT investor_id, investor_name, investor_rnk, stock_rnk, market, stock_code, stock_name, sector_name, stock_date, date_seq, invest_amt, netbid_trdvol
FROM public.v_20days_investor_big_invest_stock;

"""
from sqlalchemy import text
from database import manager

if __name__ == "__main__":
    try:
        print("Connected to My PostgreSQL database")
        engine = manager.get_engine()

        with engine.connect() as connection:

            today = "20241204"
            query = f"""
            update public.sys_configuration
            set date_value = '{today}'
            where conf_group = 'SYSTEM'
            and conf_name = 'BASE_DATE';
            """
            connection.execute(text(f"{query}"))
            connection.commit()

            print(f"☆☆☆ today: {today} update 완료!")

            # query = 'select * from public.sys_configuration'
            # rst = connection.execute(text(f"{query}"))
            
            # for r in rst:
            #     print(r)

            query = "drop table analysis.t_20days_investor_big_invest_stock;"
            connection.execute(text(f"{query}"))
            connection.commit()

            print("☆☆☆ t_20days_investor_big_invest_stock 테이블 삭제 완료.")

            query = """ 
            create table analysis.t_20days_investor_big_invest_stock as 
            SELECT investor_id, investor_name, investor_rnk, stock_rnk, market, stock_code, stock_name, sector_name, stock_date, date_seq, invest_amt, netbid_trdvol
            FROM public.v_20days_investor_big_invest_stock;
            """
            connection.execute(text(f"{query}"))
            connection.commit()

            print("☆☆☆ t_20days_investor_big_invest_stock 테이블 생성 완료.")


    except Exception as e:
        print("Error:", e)

    finally:
        if engine is not None:
            # 연결 닫기
            engine.dispose()
            print("Connection closed")

    # print('good man')
