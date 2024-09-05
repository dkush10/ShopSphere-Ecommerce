from django.shortcuts import render, redirect
from .models import Products, Cart, Contact, Checkout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import contactForm, checkoutForm

# Create your views here.

def count_(request):
    count = 0
    if request.user.is_authenticated:
        count=Cart.objects.filter(host=request.user)
        print("hello")
    return count

def totalitem(request):
    totalitem=0
    if request.user.is_authenticated:
        ca=Cart.objects.filter(host=request.user)
        for i in ca:
            totalitem+=i.quantity
    return totalitem

def home(request):
    c=Products.objects.all()
    categorylinks=[]
    for i in c:
        if i.category not in categorylinks:
            categorylinks+=[i.category]

    all=[]
    off=''
    norec=''
    if request.method=='GET':
        if 'cat' in request.GET:
            cat=request.GET['cat']
            all=Products.objects.filter(category=cat)
        
        elif 'trending' in request.GET:
            trending=request.GET['trending']
            all=Products.objects.filter(trending=1)

        elif 'offer' in request.GET:
            off='Offer - flat 40% off'
            offer=request.GET['offer']
            all=Products.objects.filter(offer=1)

        elif 'q' in request.GET:
            q=request.GET['q']
            all=Products.objects.filter(Q(category__icontains=q)|Q(name__icontains=q)|Q(desc__icontains=q))
            if len(all)==0:
                norec = 'No record found.'
        else:
            all=Products.objects.all()

    context={
        'all':all,
        'category':categorylinks,
        'off':off,
        'norec':norec,
        'tre':True,
        'connav':False,
        'totalitem':totalitem(request),
        'count':count_,
    }
    return render(request,'home.html',context)

def cart(request):
    c=Cart.objects.filter(host=request.user)

    totalamount=0
    for i in c:
        totalamount+=i.totalprice

    noitem=False
    if len(c)==0:
        noitem=True

    return render(request,'cart.html',{'c':c,
                                       'tre':False,
                                       'connav':True,
                                       'noitem':noitem,
                                       'totalamount':totalamount,
                                       'totalitem':totalitem(request),
                                       'count':count_,
                                       })

def addcart(request, id):
    auth='Please login first!'

    if request.user.is_authenticated:
        p=Products.objects.get(id=id)

        try:
            c=Cart.objects.get(name=p.name,host=request.user)
            c.quantity+=1
            c.totalprice+=p.price
            c.save()
        except:
            Cart.objects.create(category=p.category,
                                name=p.name,
                                image=p.image,
                                desc=p.desc,
                                price=p.price,
                                quantity=1,
                                totalprice=p.price,
                                host=request.user)
        return redirect('home')
    else:
        return render(request,'home.html',{'auth':auth})
    
def quantityplus(request, id):
    c=Cart.objects.get(id=id)
    c.quantity+=1
    c.totalprice+=c.price
    c.save()
    return redirect('cart')

def quantityminus(request, id):
    c=Cart.objects.get(id=id)
    if c.quantity>1:
        c.quantity-=1
        c.totalprice-=c.price
        c.save()
        return redirect('cart')
    else:
        c.delete()
    return redirect('cart')

def profile(request):
    return render(request,'profile.html',{'tre':False,'connav':True,'totalitem':totalitem(request)})

def updateprofile(request,id):
    a=User.objects.get(id=id)
    print(a.first_name,a.last_name,a.email,a.username)
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        a.first_name=first_name
        a.last_name=last_name
        a.email=email
        a.username=username
        a.save()
        return redirect('profile')
    return render(request,"updateprofile.html",{'a':a,'totalitem':totalitem(request)})


def changepassword(request, id):
    c=User.objects.get(id=id)
    print(c.password, c.username)
    invalidpass=''
    if request.method=='POST':
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        if current_password==c.password:
            c.password=new_password
            c.save()
            logout(request)
            return redirect('login_')
        else:
            invalidpass='Current password in invalid'
    return render(request,'changepassword.html',{'c':c,'invalidpass':invalidpass,'totalitem':totalitem(request)})

def deleteaccount(request, id):
    u=User.objects.get(id=id)
    u.delete()
    logout(request)
    return redirect('login_')

def remove(request,id):
    c=Cart.objects.get(id=id)
    c.delete()
    return redirect('cart')

def contactus(request):
    # ca=Cart.objects.filter(host=request.user)
    # totalitem=0
    # for i in ca:
    #     totalitem+=i.quantity

    # if request.method=='POST':
    #     fname=request.POST['fname']
    #     lname=request.POST['lname']
    #     email=request.POST['email']
    #     message=request.POST['message']
    #     print(fname, lname, email, message)
    #     Contact.objects.create(fname=fname,lname=lname,email=email,message=message,host=request.user)
    #     return render(request,'successcontact.html',{'totalitem':totalitem})

    if request.method == 'POST':
        f=contactForm(data=request.POST)
        if f.is_valid():
            ho=f.save(commit=False)
            ho.host=request.user
            ho.save()
            return render(request,'successcontact.html')
    return render(request,'contact.html',{'contactForm':contactForm,'totalitem':totalitem(request)})

def checkout(request):
    if request.method == 'POST':
        f=checkoutForm(data=request.POST)
        if f.is_valid():
            ho=f.save(commit=False)
            ho.host=request.user
            ho.save()
            return redirect('orderplaced')
    return render(request,'checkout.html',{'checkoutForm':checkoutForm,'totalitem':totalitem(request)})

def aboutus(request):
    return render(request,'aboutus.html',{'totalitem':totalitem(request)})

def orderplaced(request):
    c=Cart.objects.all()
    c.delete()
    return render(request,'orderplaced.html')




