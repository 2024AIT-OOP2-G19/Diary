from diaries.AbstractDiary import AbstractDiary

class HattoriDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日も平凡なりけり"

    def get_author(self):
        return "Hattori"