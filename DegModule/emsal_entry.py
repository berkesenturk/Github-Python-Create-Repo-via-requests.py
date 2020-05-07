def emsal_kayit():
    emsal_id= int(input("emsal id: "))
    cephe = int(input("cephe: "))
    derinlik = int(input("derinlik :"))
    taks = int(input("taks :"))
    kaks = int(input("kaks :"))
    bina_yük = int(input("bina yüksekliği : "))
    deger_updated = int(input("değerleme gününe dönüştürülmüş rayiç değer: "))
    
    with open("emsaller_bilgi.txt","a",encoding="utf-8") as file:
        file.write(f'Emsal id: {emsal_id}\ncephe: {cephe}\nderinlik: {derinlik}\ntaks: {taks}\nkaks: {kaks}\nbina yüksekliği: {bina_yük}\ndeger: {deger_updated}\n')


def parsel_alan():
    parsel_alan = cephe * derinlik
def ia(): 
    ia = taks * parsel_alan
def tia():
    tia= kaks/taks*ia



   
    
while True:
    islem = input('1- Yeni Emsal Kayıt\n2- Çıkış')
    if islem == '1':
        emsal_kayit()
    elif islem == '2':
        print("Görüşmek üzere")
        break
    else:
        break


