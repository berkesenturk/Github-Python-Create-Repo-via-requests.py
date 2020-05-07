def __init__(self, cephe, derinlik,taks,kaks,bina_yük,deger_updated):
        # object attributes
        self.cephe = cephe
        self.derinlik = derinlik
        self.taks = taks
        self.kaks = kaks
        self.bina_yük = bina_yük
        self.deger_updated = deger_updated

    # methods
    def parsel_alan(self):
        return self.cephe * self.derinlik
    def ia(self): 
        return round(self.taks*self.parsel_alan(),2)
    def tia(self):
        return round(self.kaks/self.taks*self.ia(),2)
    def birim_mkare(self):
        return round((self.deger_updated/self.tia()),2)
                      
# object (instance)
f1 = feature(cephe=40,derinlik=50,taks=0.4,kaks=2.8,bina_yük=22,deger_updated=1400000)  
print(f'f1 :cephe: {f1.cephe} derinlik: {f1.derinlik} taks: {f1.taks} kaks: {f1.kaks} bina yüksekliği: {f1.bina_yük} değerleme gününe dönüştürülmüş rayiç değer: {f1.deger_updated}, parsel alanı: {f1.parsel_alan()}')
print(f' toplam inşaat alanı: {f1.tia()}')
print(f' mkare: {f1.birim_mkare()}')
f2 = feature(cephe=30,derinlik=50,taks=0.3,kaks=2.1,bina_yük=22,deger_updated=1000000) 
print(f'f1 :cephe: {f2.cephe} derinlik: {f2.derinlik} taks: {f2.taks} kaks: {f2.kaks} bina yüksekliği: {f2.bina_yük} değerleme gününe dönüştürülmüş rayiç değer: {f2.deger_updated}, parsel alanı: {f2.parsel_alan()}')
print(f' toplam inşaat alanı: {f2.tia()}')
print(f' mkare: {f2.birim_mkare()}')
f3 = feature(cephe=30,derinlik=45,taks=0.3,kaks=3,bina_yük=25,deger_updated=1100000) 
print(f'f1 :cephe: {f3.cephe} derinlik: {f3.derinlik} taks: {f3.taks} kaks: {f3.kaks} bina yüksekliği: {f3.bina_yük} değerleme gününe dönüştürülmüş rayiç değer: {f3.deger_updated}, parsel alanı: {f3.parsel_alan()}')
print(f' toplam inşaat alanı: {f3.tia()}')
print(f' mkare: {f3.birim_mkare()}')

#input almayı 


# değerleri kaydetme!!
with open("emsaller.txt","w",encoding="utf-8") as file:

         