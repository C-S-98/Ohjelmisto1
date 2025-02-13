'''
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
'''

import mysql.connector

def hae_lentokentta(icao_koodi):
    conn = mysql.connector.connect(
        host="localhost",
        user="CS",
        password="yxth9131",
        database="flight_game",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao_koodi,))

    # tulos
    lentokentta = cursor.fetchone()

    if lentokentta:
        print(f"Lentokentän nimen: {lentokentta[0]}")
        print(f"Lentokentän sijaintikunnan: {lentokentta[1]}")
    else:
        print("ICAO ei löytyy.")

    cursor.close()
    conn.close()

# 提示用户输入 ICAO 代码
icao_koodi = input("Lentoaseman ICAO-koodi on: ").strip().upper()

# 查询并打印机场信息
hae_lentokentta(icao_koodi)
