class Queue(object):
    def __init__(self):
        self.people = []
        
    def insert(self, i):
        self.people.append(i)
        
    def remove(self):
        try:
            temp = self.people[0]
            self.people = self.people[1:]
            return temp
        except:
            raise ValueError()
