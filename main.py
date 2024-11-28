from diaries.DiarySample import DiarySample
from diaries.narifumi_Diary import narifumi_Diary
from diaries.HattoriDiary import HattoriDiary
from diaries.TsugeDiary import TsugeDiary
from diaries.OgasawaraDiary import OgasawaraDiary
from diaries.HayashiDiary import HayashiDiary

diaries = [
    DiarySample(), 
    HattoriDiary(),
    TsugeDiary(),
    OgasawaraDiary(),
    HayashiDiary(),
    narifumi_Diary()
    ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
