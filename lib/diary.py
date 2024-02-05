from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries = {}
        self.word_counts = {}

    def add(self, entry):
        self.entries[entry.title] = entry.contents
        self.word_counts[entry.title] = entry.count_words()

    def all(self):
        return self.entries
    
    def return_particular(self, title):
        return self.entries[title]
    
    def count_words(self):
        self.word_counts

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Get the total words the user can read
        readable_words = wpm * minutes
        returnable_list = []
        # Create a new dictionary containing only readable entries
        readable_entries = { key : value for key,value in self.word_counts.items() if value <= readable_words }
        for entry in self.entries.items():
            for entry1 in readable_entries.items():
                if entry[0] == entry1[0]:
                    returnable_list.append(entry)
        return returnable_list
    