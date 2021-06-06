from django.db import models

# Create your models here.

#We inherit our Todo list from a django model parent class.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): 
        #When converted to string, this is returned.
        #This lets us see what is in the todo list.
        return self.name 

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    #Each item only has 1 ToDo list.
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

'''
from main.models import ToDoList
ls = ToDoList.object.get(id=2)
ls.item_set.create(text="Not Showing", complete=True)
'''