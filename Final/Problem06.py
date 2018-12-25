
# coding: utf-8

# In[24]:


# Problem 6-1


# In[134]:


class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)
    def say(self, stuff): 
        return Professor.say(self, stuff)


# In[135]:


e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')


# In[136]:


ae.say('the sky is blue')=='eric says: It is obvious that eric says: the sky is blue'


# In[137]:


ae.lecture('the sky is blue')== 'It is obvious that eric says: the sky is blue'


# In[138]:


# Problem 6-2


# In[139]:


class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
    def say(self, stuff): 
        return Professor.say(self, stuff)


# In[140]:


e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')


# In[141]:


ae.say('the sky is blue')=='eric says: It is obvious that I believe that eric says: the sky is blue'


# In[142]:


ae.lecture('the sky is blue')=='It is obvious that I believe that eric says: the sky is blue'


# In[143]:


# Problem 6-3


# In[144]:


class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)


# In[145]:


e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')


# In[146]:


pe.say('the sky is blue')=='Prof. eric says: I believe that eric says: the sky is blue'


# In[147]:


ae.say('the sky is blue')=='Prof. eric says: It is obvious that I believe that eric says: the sky is blue'

