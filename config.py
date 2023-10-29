import mysql.connector

# CONFIG - 1 (DEFAULT CONFIG)

MyDB = mysql.connector.connect(
    host =  "65.21.238.121",
    user = "u30_waUv9b64uD",
    database = "s30_python",
    password = "r=m9AdANJe!ntQyQQux+kMh4"
)

print("Database Connected",MyDB)
