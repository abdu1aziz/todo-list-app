from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.contrib.auth.models import User


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def viewUsersList(request):
    users = User.objects.all()
    context = {'users': users}
    if 'term' in request.GET:
        query           = User.objects.filter(email__icontains=request.GET.get('term'))
        userInformation = [userInformation.email for userInformation in query]
        if userInformation:
            return JsonResponse(userInformation, safe=False)
        else:
            userInformation = ["Not Found! (Seems like this user hasn't Signed up With us yet.)"]
            return JsonResponse(userInformation, safe=False)
    if request.method == "POST":
        email = request.POST['search']
        print(email)
        print("POST WORKED!!")
        viewUserInformation = User.objects.filter(email=email).first()
        print(viewUserInformation.email)
        context = {'users': viewUserInformation}
        return render(request, 'stock/users_list.html', context)

    return render(request, 'users/users_list.html', context)

# @login_required(login_url='login')
# def searchProducts(request):

#     if 'term' in request.GET:
#         query            = stockInfo.objects.filter(name__icontains=request.GET.get('term'))
#         productNamesList = [products.name for products in query]
#         return JsonResponse(productNamesList, safe=False)
    
#     if request.method == "POST":
#         name = request.POST['search']
#         print(name)
#         print("POST WORKED!!")
#         products = stockInfo.objects.filter(name=name).first()
#         print(products.name)
#         context = {'products': products}
#         return render(request, 'stock/productSearch.html', context)

#     return redirect('index')