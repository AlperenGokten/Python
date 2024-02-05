import mysql.connector
try:
  
    xxx = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="2217",
    database="deneme1"
    )
    
    mycursor = xxx.cursor()

    a= "INSERT INTO ogrenciler (AdSoyad, Telefon) VALUES (%s, %s)"
    b= ("Alperen Gökten","05438857422")
    mycursor.execute(a, b)

    xxx.commit()

    print(mycursor.rowcount, " kayit eklendi.")

except:
    print("hata oluştu")

