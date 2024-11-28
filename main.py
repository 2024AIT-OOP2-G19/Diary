from diaries.DiarySample import DiarySample
from diaries.narifumi_Diary import narifumi_Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           narifumi_Diary() ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
