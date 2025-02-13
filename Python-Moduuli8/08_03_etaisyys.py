'''
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.
'''

import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
    host="localhost",
    user="CS",
    password="yxth9131",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_unicode_ci"
)

cursor = conn.cursor()


icao1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Syötä toisen lentokentän ICAO-koodi: ")

'''
用户输入ICOD-koodi，然后使用 cursor.execute() 查询数据库中的 latitude 和 longitude 字段，获取对应机场的坐标。
cursor.execute("SQL 语句", 参数元组)
cursor 是用来执行 SQL 语句并获取查询结果的对象。在连接数据库后，你需要通过创建游标（cursor）来与数据库交互。
execute() 方法用来执行 SQL 语句。这个方法可以用来执行查询（SELECT）、插入（INSERT）、更新（UPDATE）或删除（DELETE）等 SQL 操作。
SQL 语句：这是你想要执行的 SQL 查询语句或者命令。
参数元组：如果 SQL 语句中包含参数（例如 WHERE 子句中的变量），你可以将这些参数作为元组传递给 execute() 方法。
'''

cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao1,))
airport1 = cursor.fetchone()

cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao2,))
airport2 = cursor.fetchone()

# 当机场存在，将提取经纬度 latitude/longitude degree，然后使用 geopy 计算两个坐标之间的距离。
if airport1 and airport2:
    lat1, lon1 = airport1
    lat2, lon2 = airport2

    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)

    distance = geodesic(coords_1, coords_2).kilometers

    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {distance:.2f} kilometriä.")
else:
    print("Yksi tai molemmat ICAO-koodit eivät ole olemassa tietokannassa.")

cursor.close()
conn.close()
