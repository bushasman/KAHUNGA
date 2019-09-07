import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", db="mydb")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE `mydb`.`test1` () ENGINE = InnoDB;""")
conn.commit()
conn.close()
