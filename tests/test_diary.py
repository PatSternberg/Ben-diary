from lib.diary_entry import *
from lib.diary import *

def test_entry_add():
    new = Diary()
    entry = DiaryEntry("First", "This is first entry")
    new.add(entry)
    assert new.entries ["First"] == "This is first entry"

def test_return_all():
    new = Diary()
    entry = DiaryEntry("First", "This is first entry")
    entry2 = DiaryEntry("Second", "This is the second entry")
    new.add(entry)
    new.add(entry2)
    testing = new.all()
    assert testing == {"First": "This is first entry", "Second": "This is the second entry"}

def test_return_particular():
    new = Diary()
    entry = DiaryEntry("First", "This is first entry")
    entry2 = DiaryEntry("Second", "This is the second entry")
    new.add(entry)
    new.add(entry2)
    result = new.return_particular("Second")
    assert result == "This is the second entry"

def test_diary_based_off_reading_time():
    new = Diary()
    entry = DiaryEntry("First", "This")
    entry2 = DiaryEntry("Second", "This is the second entry This is the second entry")
    entry3 = DiaryEntry('Third', 'This is the second entry and it\'s too long entry and it\'s too long entry and it\'s too long entry and it\'s too long')
    new.add(entry)
    new.add(entry2)
    new.add(entry3)
    result = new.find_best_entry_for_reading_time(5, 2)
    assert result == [("First", "This"), ('Second', "This is the second entry This is the second entry")]