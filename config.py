import pymysql

# CONFIG - 1 (DEFAULT CONFIG)

host = 'localhost'
user = 'root'
mypass = ""
mydatabase="db"

con = pymysql.connect(host=host,user=user,password=mypass,database=mydatabase)
cur = con.cursor()

if __name__ == "__main__":  
    print("Database Connected",cur)
