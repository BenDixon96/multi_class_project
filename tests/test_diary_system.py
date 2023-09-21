from lib.diary_system import *
import pytest

diary_entry_one = Diary_chapter("april 12th", "i dont know what to write for this it seems weird. but i need to fill this up with data to get better results. on an unrealted note i should really look up how to add a new line in python.")
diary_entry_two = Diary_chapter('may 1st', 'a shot one for sanity')
diary_entry_three = Diary_chapter('september 21', 'here is more test bobbins for bobbins sake')
def test_diary_chapter_open():
    assert diary_entry_one.open() == "entry for april 12th: i dont know what to write for this it seems weird. but i need to fill this up with data to get better results. on an unrealted note i should really look up how to add a new line in python."
def test_diary_chapter_word_count():
    assert diary_entry_two.word_count() == 5

def test_task():
    my_task = Task('walk dog')
    assert my_task.is_done == False
def test_task_done():
    my_task = Task('walk dog')
    my_task.done()
    assert my_task.is_done == True
def test_contact():
    a_contact = contact('bob' ,'078354324')
    assert a_contact.name == 'bob'
    assert a_contact.number == '078354324'       
my_other_task = Task('cook')
another_task = Task('clean')
my_task = Task('walk dog')
a_contact = contact('bob' ,'078354324')
def test_diary():
    my_diary = Diary()
    assert my_diary.tasks == []
    assert my_diary.chapters == []
    assert my_diary.contacts == []
# this should add a diary entry,  a task or a contact to the approriate place
def test_add_diary_chapter():
    my_diary = Diary()
    my_diary.add(diary_entry_two)
    assert my_diary.chapters == [diary_entry_two]
def test_add_diferent_data():
    my_diary = Diary()
    my_diary.add(a_contact)
    my_diary.add(my_task)
    assert my_diary.tasks == [my_task]
    assert my_diary.contacts ==[a_contact]
def test_for_excpetion_adding_non_valid():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        my_diary.add('sting')
    error_message = str(e.value)
    assert error_message == "invalid data, not stored"

def test_for_excpetion_adding_non_valid_class():
    my_diary = Diary()
    fake_class = Dummy_class('test')
    with pytest.raises(Exception) as e:
        my_diary.add(fake_class)
    error_message = str(e.value)
    assert error_message == "invalid data, not stored"    

def test_read_entry():
    my_diary = Diary()
    my_diary.add(diary_entry_two)
    my_diary.add(diary_entry_one)
    my_diary.add(diary_entry_three)
    assert my_diary.read_entry('september 21') == 'entry for september 21: here is more test bobbins for bobbins sake'

def test_for_no_entry():
    my_diary = Diary()
    assert my_diary.read_entry('febuary 30') == "sorry no entry"

def test_busy_entry():
    my_diary = Diary()
    my_diary.add(diary_entry_two)
    my_diary.add(diary_entry_one)
    my_diary.add(diary_entry_three)
    assert my_diary.busy_read(5, 2) == 'entry for september 21: here is more test bobbins for bobbins sake'   

def test_no_time_to():
    my_diary = Diary()
    my_diary.add(diary_entry_two)
    my_diary.add(diary_entry_one)
    my_diary.add(diary_entry_three)
    assert my_diary.busy_read(1,1) == "you have no time for that"

def test_todo_list():
    my_diary = Diary()
    my_diary.add(my_other_task)
    my_diary.add(my_task)
    assert my_diary.todo() == ['cook', 'walk dog']

def test_done_class():
    my_diary = Diary()
    my_diary.add(my_other_task)
    my_other_task.done()
    assert my_diary.todo() == "all done"
a_contact = contact('bob' ,'078354324')
my_contact = contact('babs', '073333' )  
more_contact = contact('jimmy', '0744444')      
def test_get_contact():
    my_diary = Diary()
    my_diary.add(a_contact)
    my_diary.add(my_contact)
    my_diary.add(more_contact)
    assert my_diary.get_number('bob') == "bobs number: 078354324"
def test_show_contacts():
    my_diary = Diary()
    my_diary.add(a_contact)
    my_diary.add(my_contact)
    my_diary.add(more_contact)
    assert my_diary.show_contacts() == ["bobs number: 078354324", 'babss number: 073333', 'jimmys number: 0744444']