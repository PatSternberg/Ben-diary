from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries = {}
        self.word_counts = {}
    def add(self, entry):
        self.entries[entry.title] = entry.contents
    def all(self):
        return self.entries
    def return_particular(self, title):
        return self.entries[title]
    def count_words(self):
        self.word_counts
    def reading_time(self, wpm):
        pass
    def find_best_entry_for_reading_time(self, wpm, minutes):
        pass