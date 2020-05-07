from emsal_entry import *

def deger_hesabý():
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
            
            if 'tia:' in line:    #TÝA YOK TXT'DE YARIN DAHA ÝYÝ DÜÞÜNEREK ÇÖZ            
                deger = int(line.split(':')[-1].strip())
                liste.append(deger)
    






deger_hesabý()

                
                
            
        



