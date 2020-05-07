import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz.
results = df.head(10)

# 2- Toplam kaç kayıt vardır ?
results = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
results = df["Salary"].mean()
# 4- En yüksek maaşı ne kadardır ?
results = df["Salary"].max()
# 5- En yüksek maaşı alan oyuncu kimdir ?
results = df[df["Salary"] == df["Salary"].max()]["Name"]
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
results = df[(df["Age"]<=25) & (df["Age"] >=20)].sort_values("Age", ascending = False)[["Name","Team","Age"]]
# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
results = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
results =  df.groupby("Team").mean()["Salary"]

# 9- Kaç farklı takım mevcut ?
results = len(df.groupby("Team"))
results = df["Team"].unique()

# 10- Her takımda kaç oyuncu oynamaktadır ?
results = df["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df = df.dropna() # df.dropna(inplace=True) 'da olur.


def str_find(name):
    if "and" in name.lower():
        return True
    return False

results = df[df["Name"].apply(str_find)]

print(results)