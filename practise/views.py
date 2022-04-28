from django.shortcuts import redirect, render
from .models import Customer

# Create your views here.
def create_view(request):
    if request.method == "POST":
        name_v = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        
        c = Customer(name=name_v, email=email, phone=phone)
        c.save()
        
        return redirect('/')
    
    return render(request, 'practise/create.html', context={})

def update_view(request):
    if request.method == "POST":
        # Old fields
        name_o = request.POST["name"]
        email_o = request.POST["email"]
        phone_o = request.POST["phone"]
    
        # New fields
        name = request.POST["name_n"]
        email = request.POST["email_n"]
        phone = request.POST["phone_n"]
        
        print("Old Data")
        print(name_o, email_o, phone_o)
        print("New Data")
        print(name, email, phone)
        
        return redirect('/')
        
    return render(request, 'practise/update.html')

def delete_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        c = Customer.objects.get(name=name)
        c.delete()
        return redirect('/')
    
    return render(request, 'practise/delete.html', context={})

def show_users(request):
    customers = Customer.objects.all()
    
    return render(request, 'practise/users.html', context={"customers":customers})