from emsal_entry import *

def deger_hesab�():
    liste1=[]
    with open('emsaller_bilgi.txt', 'r',encoding="utf-8") as file:        
        for line in file:
            
            if 'deger:' in line:                
                deger = int(line.split(':-1').strip())
                liste.append(deger)
    print(liste)
    avg = sum(liste)/len(liste)
    print(avg)
def birim_mkare():
    liste2=[]
    with open('emsaller_bilgi.txt', 'r',encoding="utf-8") as file:        

    for line in file:
            
            if 'tia:' in line:    #T�A YOK TXT'DE YARIN DAHA �Y� D���NEREK ��Z            
                deger = int(line.split(':')[-1].strip())
                liste.append(deger)
    






deger_hesab�()

                
                
            
        



