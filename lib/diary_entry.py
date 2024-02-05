class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
    def count_words(self):
        list_of_words = [word for word in self.contents.split()]
        return len(list_of_words)
    def reading_time(self, wpm):
        pass
    def reading_chunk(self, wpm, minutes):
        pass