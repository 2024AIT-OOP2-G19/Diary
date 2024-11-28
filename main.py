from diaries.DiarySample import DiarySample
from diaries.HattoriDiary import HattoriDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    HattoriDiary(),
    ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
