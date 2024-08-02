#24.5.31
class Note():
    def __init__(self,content=None):
        self.content=content
    def write_content(self,content):
        self.content=content
    def remove_all(self):
        self.content=""        
    def __add__(self,other):
        return self.content+other.content        
    def __str__(self):
        return self.content
    
class NoteBook():
    def __init__(self,title):
        self.title=title
        self.page_numger=1
        self.note={}
    def add_note(self,note,page=0):
        if self.page_numger<300:
            if page==0:
                self.notep[self.page_numger]=note
                self.page_numger+=1
            else:
                self.notes={page:note}
                self.page_numger+=1
        else:
            print("페이지가 꽉 찼습니다.")

    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")
    def get_number_of_pages(self):
        return len (self.notes.keys())
