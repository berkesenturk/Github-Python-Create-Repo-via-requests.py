#BANKAMATİK

BerkeHesap = {
    'ad' : 'Berke Şentürk',
    'hesapNo' : '1234798',
    'bakiye':   3000,
    'ekHesap' : 2000
}

AliHesap = {
    'ad' : 'Ali Kasap',
    'hesapNo' : '1234799',
    'bakiye':10000,
    'ekHesap' : 3000
}

def paraCek(hesap, miktar):  #hesaptan para çekilmesini sağlayan fonksiyon
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap['bakiye'] >= miktar):  #bakiye miktarının çekilecek miktardan büyük olduğu KOŞUL
        hesap['bakiye'] -= miktar    #çekilen miktarın bakiyeden düşülmesi
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)        #BAKİYENİN DURUMU
    else:  #eğer bakiye miktardan yetersiz ise Ek Hesaba başvurulmasını sağlayan KOŞUL!
        toplam = hesap['bakiye'] + hesap['ekHesap']
        
        if (toplam >= miktar): #BAKİYE ve EK HESABIN TOPLAM MİKTARININ ÇEKİLMEK İSTENEN PARADAN BÜYÜK OLDUĞU KOŞUL
            ekHesapKullanimi = input('Ek Hesap Kullanılsın mı? (E/H)') #EK HESABIN KULLANILMASININ İZNİNİN İSTENMESİ KOŞULU
            if ekHesapKullanimi =='E':
                ekHesapKullaniLacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullaniLacakMiktar   #çekilen miktarın EKHESAPTAN düşülmesi
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)        #BAKİYENİN DURUMU
            else: #EK HESABIN TOPLAM MİKTARININ ÇEKİLMEK İSTENEN PARANIN BAKİYEDEN DÜŞÜLMÜŞ KISMINDAN DAHİ KÜÇÜK OLDUĞU KOŞUL
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmakta.") #HESABIN DURUMU
        else: #BAKİYE ve EK HESABIN TOPLAM MİKTARININ ÇEKİLMEK İSTENEN PARADAN KÜÇÜK OLDUĞU KOŞUL
            print('Bakiyen yok')
            bakiyeSorgula(hesap) #BAKİYENİN DURUMU

def bakiyeSorgula(hesap):  #HESABIN DURUMU FONKSİYONU
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmakta.Ek hesap limitiniz ise {hesap['ekHesap']}")
    


paraCek(BerkeHesap, 3000)

print('*******************')

paraCek(BerkeHesap, 2000)