from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodolistItem

# Create your views here.
def todolistView(request):
    all_todolist_items = TodolistItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items': all_todolist_items})

def addTodolist(request):
    new_item = TodolistItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todolist')

def deleteTodolist(request, todolist_id):
    item_to_delete = TodolistItem.objects.get(id=todolist_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todolist')
