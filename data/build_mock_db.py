import sqlite3
import random
from datetime import datetime, timedelta

def build_db():
    conn = sqlite3.connect('mock_universe.db')
    c = conn.cursor()

    # 1. Security
    c.execute('''CREATE TABLE Security (s_id INTEGER PRIMARY KEY, cusip TEXT, ticker TEXT, sic TEXT, index_flag BOOLEAN, exchange_flags TEXT, class TEXT, issue_type TEXT, industry_group TEXT)''')
    # 2. Security_Name
    c.execute('''CREATE TABLE Security_Name (s_id INTEGER, date DATE, cusip TEXT, ticker TEXT, class TEXT, issuer_description TEXT, issue_description TEXT, sic TEXT, system_time TIMESTAMP)''')
    # 3. Exchange
    c.execute('''CREATE TABLE Exchange (s_id INTEGER, date DATE, sequence_number INTEGER, status TEXT, exchange TEXT, add_delete_indicator TEXT, exchange_flags TEXT, system_time TIMESTAMP)''')
    # 4. Distribution
    c.execute('''CREATE TABLE Distribution (s_id INTEGER, record_date DATE, sequence_number INTEGER, ex_date DATE, amount REAL, adjustment_factor REAL, declare_date DATE, payment_date DATE, link_security_id INTEGER, distribution_type INTEGER, frequency TEXT, currency TEXT, approximate_flag BOOLEAN, cancel_flag BOOLEAN, liquidation_flag BOOLEAN, system_time TIMESTAMP)''')
    # 5. Security_Price
    c.execute('''CREATE TABLE Security_Price (s_id INTEGER, date DATE, bid_low REAL, ask_high REAL, close_price REAL, volume INTEGER, total_return REAL, adjustment_factor REAL, open_price REAL, shares_outstanding INTEGER, adjustment_factor2 REAL, system_time TIMESTAMP)''')
    # 6. Option_Info
    c.execute('''CREATE TABLE Option_Info (s_id INTEGER, dividend_convention TEXT, exercise_style TEXT, system_time TIMESTAMP)''')
    # 7. Option_Contract
    c.execute('''CREATE TABLE Option_Contract (option_id INTEGER PRIMARY KEY, s_id INTEGER, symbol TEXT, symbol_flag INTEGER, strike INTEGER, expiration DATE, call_put TEXT, contractsize INTEGER, expiryindicator TEXT, system_time TIMESTAMP)''')
    # 8. Option_Price
    c.execute('''CREATE TABLE Option_Price (option_id INTEGER, date DATE, best_bid REAL, best_offer REAL, last_trade_date DATE, volume INTEGER, open_interest INTEGER, special_settlement INTEGER, implied_volatility REAL, delta REAL, gamma REAL, vega REAL, theta REAL, adjustment_factor REAL, system_time TIMESTAMP)''')
    # 9. Forward_Price
    c.execute('''CREATE TABLE Forward_Price (s_id INTEGER, date DATE, expiration DATE, forward_price REAL, system_time TIMESTAMP)''')
    # 10. Zero_Curve
    c.execute('''CREATE TABLE Zero_Curve (date DATE, days INTEGER, expiration_date DATE, rate REAL, system_time TIMESTAMP)''')
    # 11. Dim_Date
    c.execute('''CREATE TABLE Dim_Date (date DATE, is_trading_day BOOLEAN, is_holiday BOOLEAN, next_trading_day DATE)''')

    # Data Setup
    start_date = datetime(2023, 1, 1)
    dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(90)]
    
    securities = [
        (10001002, '30303M10', 'FB'),    
        (10001005, '78486Q10', 'SVB')    
    ]

    # Dim_Date population
    for idx, d in enumerate(dates):
        dt = datetime.strptime(d, '%Y-%m-%d')
        is_weekend = dt.weekday() >= 5
        is_trading = not is_weekend 
        next_dt = dt + timedelta(days=3 if dt.weekday() == 4 else (2 if dt.weekday() == 5 else 1))
        c.execute("INSERT INTO Dim_Date VALUES (?, ?, ?, ?)", (d, is_trading, False, next_dt.strftime('%Y-%m-%d')))

    # Security & Option_Info population
    for s_id, cusip, t in securities:
        c.execute("INSERT INTO Security VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (s_id, cusip, t, '3571', False, 'NASDAQ', 'CLASS_A', 'COMMON_STOCK', '311'))
        c.execute("INSERT INTO Option_Info VALUES (?, ?, ?, ?)", (s_id, 'DISCRETE', 'AMERICAN', dates[0] + ' 16:30'))
        c.execute("INSERT INTO Security_Name VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (s_id, dates[0], cusip, t, 'CLASS_A', f'{t} INC', 'COMMON', '3571', dates[0] + ' 16:30'))

    # Security Prices & Dimensions mapping
    for date in dates:
        dt = datetime.strptime(date, '%Y-%m-%d')
        if dt.weekday() >= 5: continue # Skip weekends
        
        for s_id, cusip, t in securities:
            if s_id == 10001002 and date >= '2023-02-15':  
                if date == '2023-02-15':
                    c.execute("INSERT INTO Security_Name VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (s_id, date, cusip, 'META', 'CLASS_A', 'META PLATFORMS', 'COMMON', '3571', date + ' 16:30'))
            
            if s_id == 10001005 and date >= '2023-02-28': 
                continue # Delisted, equity stops printing
                
            close_col = 150.0 + random.uniform(-2, 2)
            bid = close_col - 0.5
            ask = close_col + 0.5
            adj = 1.0
            vol = random.randint(1000000, 50000000)
            
            # META Cumulative Split Cascades (2-for-1 -> 3-for-1)
            if s_id == 10001002:
                if date >= '2023-02-27':  # The 3-for-1 split hits
                    close_col = close_col / 6.0 
                    bid = bid / 6.0
                    ask = ask / 6.0
                    adj = 6.0
                    if date == '2023-02-27':
                        rec_date = (dt - timedelta(days=2)).strftime('%Y-%m-%d')
                        decl_date = (dt - timedelta(days=15)).strftime('%Y-%m-%d')
                        c.execute("INSERT INTO Distribution VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                 (s_id, rec_date, 2, date, 0, 3.0, decl_date, date, None, 2, 'QUARTERLY', 'USD', False, False, False, decl_date + ' 16:30'))
                elif date >= '2023-02-20': # The 2-for-1 split hits
                    close_col = close_col / 2.0 
                    bid = bid / 2.0
                    ask = ask / 2.0
                    adj = 2.0
                    if date == '2023-02-20':
                        rec_date = (dt - timedelta(days=2)).strftime('%Y-%m-%d')
                        decl_date = (dt - timedelta(days=15)).strftime('%Y-%m-%d')
                        c.execute("INSERT INTO Distribution VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                 (s_id, rec_date, 1, date, 0, 2.0, decl_date, date, None, 2, 'QUARTERLY', 'USD', False, False, False, decl_date + ' 16:30'))

            # SVB Halting physics
            if s_id == 10001005:
                if date >= '2023-02-23' and date < '2023-02-28':
                    close_col = -abs(close_col) # Flat negative midpoints overload
                    bid = -abs(bid)
                    ask = -abs(ask)
                    vol = 0
            
            c.execute("INSERT INTO Security_Price VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                     (s_id, date, bid, ask, close_col, vol, 0.003, adj, close_col, 150000000, adj * 1.05, date + ' 16:30'))
            
            # Forward Price Generation
            exp_date_fp = (dt + timedelta(days=30)).strftime('%Y-%m-%d')
            c.execute("INSERT INTO Forward_Price VALUES (?, ?, ?, ?, ?)", (s_id, date, exp_date_fp, abs(close_col) * 1.01, date + ' 16:30'))
            
            # Bitemporal Restatement Hook (Transferred to FB)
            if s_id == 10001002 and date == '2023-01-05':
                c.execute("INSERT INTO Forward_Price VALUES (?, ?, ?, ?, ?)", (s_id, date, exp_date_fp, 155.00, '2023-02-01 14:00'))

    # Option Contracts & Option Prices
    opt_id_counter = 80000
    for s_id, _, t in securities:
        for strk in [140, 150, 160]: 
            opt_id_counter += 1
            exp_d = (start_date + timedelta(days=120)).strftime('%Y-%m-%d')
            c.execute("INSERT INTO Option_Contract VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                     (opt_id_counter, s_id, f'{t} 230616C00150', 1, strk*1000, exp_d, 'CALL', 100, 'MONTHLY', dates[0] + ' 16:30'))
            
            for date in dates:
                dt = datetime.strptime(date, '%Y-%m-%d')
                if dt.weekday() >= 5: continue 
                
                # If SVB delists, the options might still "exist" but OPRA stops broadcasting entirely for them
                if s_id == 10001005 and date >= '2023-02-28': 
                    continue # Options stop printing OPRA quotes
                
                active_opt_id = opt_id_counter 
                adj = 1.0
                size = 100
                st_time = dates[0] + ' 16:30'
                special_set = 0
                opt_vol = random.randint(10, 500)

                if s_id == 10001002:  # META Derivative Mutations
                    if date >= '2023-02-27':
                        active_opt_id = opt_id_counter + 7000 # 2nd generation
                        adj = 6.0
                        size = 600
                        st_time = '2023-02-27 16:30'
                        if date == '2023-02-27':
                            c.execute("INSERT INTO Option_Contract VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                     (active_opt_id, s_id, f'META2 230616C00083', 3, int(strk*1000/6.0), exp_d, 'CALL', size, 'MONTHLY', st_time))
                    elif date >= '2023-02-20':
                        active_opt_id = opt_id_counter + 3000 # 1st generation
                        adj = 2.0
                        size = 200
                        st_time = '2023-02-20 16:30'
                        if date == '2023-02-20':
                            c.execute("INSERT INTO Option_Contract VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                     (active_opt_id, s_id, f'META1 230616C00125', 2, int(strk*1000/2.0), exp_d, 'CALL', size, 'MONTHLY', st_time))
                
                if s_id == 10001005:
                    if date >= '2023-02-23' and date < '2023-02-28':
                        opt_vol = 0 # No volume due to underlying halt
                        special_set = 1 # Regulatory Halt Special Settlement flag thrown
                
                c.execute("INSERT INTO Option_Price VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                         (active_opt_id, date, 1.45, 1.48, date, opt_vol, 1000, special_set, 0.18, 0.42, 0.05, 0.08, -0.02, adj, date + ' 16:30'))

    # Exchange Corporate Events & Liquidations
    c.execute("INSERT INTO Exchange VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (10001005, '2023-02-23', 1, 'HALTED', 'NASDAQ', 'ADD', 'NASDAQ', '2023-02-23 16:30'))
    c.execute("INSERT INTO Exchange VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (10001005, '2023-02-28', 1, 'DELISTED', 'NASDAQ', 'DELETE', '', '2023-02-28 16:30'))
    # Liquidation corporate action injection
    c.execute("INSERT INTO Distribution VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
             (10001005, '2023-02-28', 1, '2023-02-28', 0, 1.0, '2023-02-23', None, None, 3, 'NONE', 'USD', False, False, True, '2023-02-28 16:30'))

    # Zero Curve Generator
    for date in dates:
        dt = datetime.strptime(date, '%Y-%m-%d')
        if dt.weekday() >= 5: continue
        exp_date_zc = (dt + timedelta(days=30)).strftime('%Y-%m-%d')
        c.execute("INSERT INTO Zero_Curve VALUES (?, ?, ?, ?, ?)", (date, 30, exp_date_zc, 0.045, date + ' 16:30'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    build_db()
    print("Strict 2-Ticker Database (FB/META + SVB limit down) built successfully.")
