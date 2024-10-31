from django.shortcuts import render, redirect, get_object_or_404
from .forms import StdForm
from .models import StudentsInfo

def add(request):
    form = StdForm()
    if request.method == 'POST':
        form = StdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'invapp/add.html', {'form': form})

def update(request, student_id):
    student = get_object_or_404(StudentsInfo, student_id=student_id)
    form = StdForm(instance=student)
    if request.method == 'POST':
        form = StdForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'invapp/edit.html', {'form': form})

def list(request):
    info = StudentsInfo.objects.all()
    return render(request, 'invapp/list.html', {'info': info})

def delete(request, student_id):
    student = get_object_or_404(StudentsInfo, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, 'invapp/confirm_delete.html', {'student': student})
