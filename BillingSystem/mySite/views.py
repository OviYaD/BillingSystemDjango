from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mySite.models import signin, Product, customerDetail, Bill, CartItem

# Create your views here.

bill = None

def index(request):
    t=loader.get_template("login.html")
    return HttpResponse(t.render())

def login(request):
    errors=[]
    if request.method=="POST":
        if 'signup' in request.POST:
            print("signup")
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['passwrd']
            insert=signin(username=username,email=email,password=password)
            insert.save()
            print("saved successfully")
            # return render(request,"login.html")
        elif 'signin' in request.POST:
            print("signin")
            username=request.POST['username']
            password=request.POST['passwrd']
            # print(find.password,find.username)

            try:
                find=signin.objects.get(username=username)
                print(find.password,find.username)

                if find.password==password:
                    return HttpResponse("successfully complated")
                else:
                    print(find.password)
                    errors.append("invalid  passwrd")
            except signin.DoesNotExist:
                print("error")
                errors.append("invalid username or passwrd")
                return render(request,"login.html",{"errors":errors})
            # elif request.POST['signin']=="Sign In":
            #     print("signin")

    return render(request,"login.html",{"errors":errors})
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['passwrd']
        insert=signin(username=username,email=email,password=password)
        insert.save()
        print("saved successfully")
    return render(request,"login.html")
        
def signingin(request):
    errors=[]
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['passwrd']
        # print(find.password,find.username)

        try:
            find=signin.objects.get(username=username)
            print(find.password,find.username)

            if find.password==password:
                return HttpResponse("successfully complated")
            else:
                print(find.password)
                errors.append("invalid  passwrd")
        except signin.DoesNotExist:
            print("error")
            errors.append("invalid username or passwrd")
        
    return render(request,"login.html",{'errors':errors})


def home(request):
    t=loader.get_template("home.html")
    return render(request,"home.html")


def addProduct(request):
    if request.method=="POST":
        name = request.POST["name"]
        price = int(request.POST["price"])
        stock = int(request.POST["stock"])
        print(name, price, stock)
        p = Product(name = name, price = price, stock = stock)
        p.save()
    return render(request, "addproduct.html")


def checkStock(request):
    return render(request,"checkStock.html")
def showStock(request):
    stockDetails={}
    if request.method=="POST":
        print("post")
        name=request.POST.get('name',None)
        # global p
        p=Product.objects.filter(name=name)[0]
        stockDetails={"name":p.name,"price":p.price,"stock":p.stock}
        print(stockDetails)
    return render(request,"showStock.html",stockDetails)
def customerDetails(request):
    
    return render(request,"customerDetails.html")
def createBill(request):
    print(request.method)
    if request.method=="POST":
        print(request.POST)
        cname=request.POST.get("name",None)
        cphone=request.POST.get("phone",None)
        caddress=request.POST.get("address",None)
        c = customerDetail(name=cname,contact=cphone,address=caddress)
        c.save()
        global bill
        bill = Bill(total=0, customer = c)
        bill.save()
        print(c)
        print(bill)
        print(bill.id)
    return render(request,"customerProducts.html")

def addProductToBill(request):
    if(request.method == "POST"):
        name = request.POST.get("name", None)
        quantity = int(request.POST.get("quantity", 1))
        print(name, quantity)
        p=Product.objects.filter(name=name)[0]
        print(p)

        global bill
        print(bill)
        cartItem = CartItem(bill = bill, product = p, quantity = quantity)
        cartItem.save()

    return render(request, "customerProducts.html")

def showBill(request):
    data ={"items":[]}

    global bill
    # bill = Bill.objects.all()[5]
    # print(bill)
    subTotal = 0

    data["billId"] = bill.id
    data["name"] = bill.customer.name


    itemsQuerySet = CartItem.objects.filter(bill = bill)    
    for item in itemsQuerySet:
        temp = {}
        temp["name"] = item.product.name
        temp["quantity"] = item.quantity
        temp["price"]=item.product.price
        temp["total"] = item.quantity * item.product.price
        subTotal += temp["total"]

        data["items"].append(temp)

    data["subTotal"] = subTotal
    data["total"] = subTotal + 30
    

    return render(request,"bill.html", data)