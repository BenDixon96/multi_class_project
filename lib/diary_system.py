#As a user
#So that I can record my experiences
#I want to keep a regular diary
# 
#  one class, diary-- has attribute self.diary_chapters: a list of diary chapters(class two)
#  has attribute words per min self.wpm
#  has attribute 3 todolist a list of class 3, tasks
#  has attribute 4 contacts  a list of class 4 contacts
#
# has method read chapter returns a chapter(class 2) entry
#  has method 2: give me a chapter based of how musch time i have
#   has method three add task
#   has method 4 show complted task
#   has method 5 show task todo

#  class two, diary chapter, includes day_of entry and entry
#  has method word count or attribute 
#  has a method open shows the diary chapter nicley formated with the date
##   
#  class 3 Tasks 
#   includes  a task and if its been done:  and   contains method = mark as comlete
#   self.task
#   self.complete
#    
##  class 4 is contact contains two atributes name and number
#
#
#
#   As a user
#So that I can reflect on my experiences
#I want to read my past diary entries
#As a user
#So that I can reflect on my experiences in my busy day
#I want to select diary entries to read based on how much time I have and my reading speed
#As a user
#So that I can keep track of my tasks
#I want to keep a todo list along with my diary
#As a user
#So that I can keep track of my contacts
# i want to see a list of all of the mobile phone numbers in all my diary entries
class Diary_chapter():
    def __init__(self, date, contents):
        self.date = date
        self.contents = contents
    def open(self):
        return f"entry for {self.date}: {self.contents}"
    def word_count(self):
        my_loop = self.contents.split()
        non_word = 0
        for i in my_loop:
            if i[0].isalpha() != True:
                non_word += 1
        return len(my_loop) - non_word  

class Dummy_class():
    def __init__(self, string):
        self.string = string        

class Task():
    def __init__(self, task):
        self.is_done = False
        self.task = task
    def done(self):
        self.is_done = True

class contact():
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Diary():
    def __init__(self):
        self.tasks = []
        self.chapters = []
        self.contacts = []
    def add(self, data):
        if hasattr(data, 'contents') == True:
            self.chapters.append(data)    
        elif hasattr(data, 'task') == True:
            self.tasks.append(data)
        elif hasattr(data, 'number') == True:
            self.contacts.append(data)
        else:
            raise Exception("invalid data, not stored")
    def read_entry(self, date_of_entry):
        for i in self.chapters:
            if i.date == date_of_entry:
                print(i.open())
                return i.open()    
        else:
            return 'sorry no entry'    
    def busy_read(self, wpm, mins):
        res = None
        tot_words = 0
        can_read_words = wpm * mins
        print(self.chapters)
        for i in self.chapters: 
            if i.word_count() > tot_words and i.word_count() <= can_read_words:
                res = i
                tot_words = i.word_count()
        if res == None:
            return 'you have no time for that'
        else:        
            return res.open()    

    def todo(self):
        res = []
        for i in self.tasks:
            if i.is_done == False:
                res.append(i.task)
        if res == []:
            return "all done"
        else:
            return res
    def get_number(self, name):
        for i in self.contacts:
            if i.name == name:
                return f'{i.name}s number: {i.number}'
    def show_contacts(self):
        res = []
        for i in self.contacts:
            res.append(f'{i.name}s number: {i.number}')        
        return res    
