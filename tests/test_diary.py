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