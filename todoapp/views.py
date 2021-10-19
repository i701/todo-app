from django.shortcuts import redirect, render
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            print(request.POST)
            todos = List.objects.all()
            context = {
                'todos': todos,
            }
            messages.success(request, ('Item successfully added!'))
            return render(request, 'home.html', context)
        return render(request, 'home.html', {'todos': List.objects.all()})

    else:
        todos = List.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, 'home.html', context)


def delete(request, list_id):
    item = List.objects.get(id=list_id)
    item.delete()
    messages.success(request, ('Item successfully Removed!'))
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(id=list_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item successfully checked off!'))
    return redirect('home')
