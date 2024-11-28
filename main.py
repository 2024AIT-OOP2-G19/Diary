from diaries.DiarySample import DiarySample
from diaries.OgasawaraDiary import OgasawaraDiary
from diaries.HayashiDiary import HayashiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    OgasawaraDiary(),
    HayashiDiary(),
    ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
