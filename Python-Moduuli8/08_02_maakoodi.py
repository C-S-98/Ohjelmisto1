'''
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta,
helikopterikenttiä on 15 kappaletta jne.
'''

import mysql.connector

def hae_lentokentat_maakoodilla(maakoodi):
    conn = mysql.connector.connect(
        host="localhost",
        user="CS",
        password="yxth9131",
        database="flight_game",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

    cursor = conn.cursor()

    query = """
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = %s 
        GROUP BY type
    """
    cursor.execute(query, (maakoodi,))

    result = cursor.fetchall()

    if result:
        print(f"{maakoodi} maan lentokenttätyyppien tilastot:")
        for row in result:
            airport_type, count = row
            print(f"{airport_type}: {count} kappaletta")
    else:
        print(f"{maakoodi} maasta ei löytynyt lentokenttätietoja.")

    cursor.close()
    conn.close()

maakoodi = input("Maan koodi on: ").strip().upper()

hae_lentokentat_maakoodilla(maakoodi)

'''
result 片段代码的功能是：
    在查询结果不为空的情况下，循环遍历每一行数据，打印出每种机场类型和其对应的数量。
    如果查询结果为空，则会执行 else 中的代码，提示用户没有找到数据。
        if result:
            这是检查 result 是否有数据。如果查询返回了结果（即 result 不为空），
            则会进入 if 语句中的代码块；否则，会跳到 else 语句
        for row in result:
            这一行是一个 for 循环，用来遍历查询结果 result 中的每一行数据。
            每一行（row）包含两个值：
                airport_type：机场的类型（例如：小型机场、直升机机场等）。
                count：该类型机场的数量。
        airport_type, count = row
            这行代码将 row（查询结果中的一行数据）解包成两个变量：
            airport_type 和 count。
            airport_type 存储机场类型，count 存储该类型机场的数量。
            
%s 是 SQL 查询中的占位符，它表示将在查询执行时插入一个值。
这个值由 (maakoodi,) 提供，maakoodi 是用户输入的国家代码
。例如，如果用户输入 FI，那么查询语句就变成了：
                                        SELECT type, COUNT(*) 
                                        FROM airport 
                                        WHERE iso_country = 'FI' 
                                        GROUP BY type
COUNT(*) 是 SQL 中的聚合函数，用于统计查询结果中符合条件的行数。
    具体来说，COUNT(*) 会计算出查询结果中有多少行数据，而不是每一行的值。
    它通常与 GROUP BY 子句一起使用，用来统计每组中的行数。
GROUP BY type
    GROUP BY 会将数据按照 type 字段的不同值进行分组。
    在我们的数据集中，type 有两个不同的值：Small 和 Large。
'''