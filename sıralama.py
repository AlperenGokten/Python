dosya = open ("rehberlik.txt","r")
print("╔═════════════════════╗")
print("║ Kayıtlı kişiler     ║")
print("╚═════════════════════╝")

okunan = dosya.readlines()
print(okunan)
for a in okunan:
    print(a)


dosya.close()
    
