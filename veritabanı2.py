import mysql.connector
try:
  
    xxx = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="2217" )
     
    

    secilenvt = xxx.cursor()
    secilenvt.execute ("SHOW DATABASES")
    print ("\nVeritabanlari:")
    for x in secilenvt: print(x)
except mysql.connector.Error as xx:
    print("hata oluştu")
    print (f"hata kodu:\n{xx}")