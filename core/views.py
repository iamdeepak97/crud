from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'delete.html', {'employee': employee})

################################################################
import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Failed to fetch data: {response.status_code}")

#webscraping
import requests

url = 'https://commons.wikimedia.org/wiki/File:Track_through_Cally_Mains_Wood_-_geograph.org.uk_-_5182206.jpg'
response = requests.get(url)

if response.status_code == 200:
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Failed to download image: {response.status_code}")




