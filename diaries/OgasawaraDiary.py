from diaries.AbstractDiary import AbstractDiary

class OgasawaraDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "オブジェクト指向プログラミングⅡ 第9回の授業を受けた."

    def get_author(self):
        return "Ogasawara"
