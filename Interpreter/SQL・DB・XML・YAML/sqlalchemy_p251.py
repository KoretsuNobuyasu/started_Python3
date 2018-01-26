#そもそも全体的にインタプリタモードで使用する。
#履歴
'''
#>>> import sqlalchemy as sa
#>>> conn = sa.create_engine('sqlite://')
#>>> conn.execute('''CREATE TABLE zoo
#...     (critter VARCHER(20) PRIMARY KEY,
#...     count INT,
...     damages FLOAT)''')
<sqlalchemy.engine.result.ResultProxy object at 0x102a1cbe0>
>>> ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
>>> conn.execute(ins, 'duck', 10, 0.0)
<sqlalchemy.engine.result.ResultProxy object at 0x102a1ce10>
>>> conn.execute(ins, 'bear', 2, 1000.0)
<sqlalchemy.engine.result.ResultProxy object at 0x102a1ceb8>
>>> conn.execute(ins, 'weasel', 1, 2000.0)
<sqlalchemy.engine.result.ResultProxy object at 0x102a1cda0>
>>> rows = conn.execute('SELECT * FROM zoo')
>>> print(rows)
<sqlalchemy.engine.result.ResultProxy object at 0x102a1c710>
>>> for row in rows:
...     print(row)
...
('duck', 10, 0.0)
('bear', 2, 1000.0)
('weasel', 1, 2000.0)
'''
