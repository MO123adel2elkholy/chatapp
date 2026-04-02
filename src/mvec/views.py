from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Slider, BannerArea, Main_Category, Product, Category, Codon_copon
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models import Max, Min, Sum
from cart.cart import Cart
# Create your views here.


@login_required(login_url='login')
def base(request):
    Main_Categories = Main_Category.objects.all()
    context = {"Main_Categories": Main_Categories}
    return render(request, 'base.html')


@login_required(login_url='login')
def home(request):
    Sliders = Slider.objects.all()
    Banners = BannerArea.objects.all()
    Main_Categories = Main_Category.objects.all()
    top_deal_products = Product.objects.filter(
        section__name='Top Deals Of The Day')
    print(top_deal_products)
    context = {"Sliders": Sliders, "Banners": Banners,
               "Main_Categories": Main_Categories, "top_deal_products": top_deal_products}
    return render(request, 'main/home.html', context)


@login_required(login_url='login')
def product_details(request, pk):
    try:
        product = Product.objects.get(id=pk)
        Main_Categories = Main_Category.objects.all()
        context = {"product": product, "Main_Categories": Main_Categories}
    except:
        context = {}
        return redirect('page_404')
    return render(request, 'main/product_details.html', context=context)


@login_required(login_url='login')
def page_404(request):
    return render(request, 'main/not_found.html', )


@login_required(login_url='login')
def my_account(request):
    return render(request, 'account/my_account.html',)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('user data =', username, email, password)
        print('fuck you')
        if User.objects.filter(username=username).exists():
            messages.info(request, 'user ' + username +
                          " is Aleardy in system ")
            return redirect('login')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'user email ' +
                          email + "  is Aleardy in system ")
            return redirect('login')
        else:
            user = User()
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        messages.info(request, 'user ' + username +
                      " created successfuly login to view all websit features")
        print('user ' + username + " created successfuly")

    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('user data =', username, email, password)
        print('fuck you')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'user ' + username +
                          " loged in  successfuly")
            print('user ' + username + " loged in  successfuly")
            return redirect('/')
        else:
            messages.info(request, 'user ' + username +
                          " or password are wrong please try again!")
            return redirect('login')

    return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_profile(request):
    return render(request, 'account/profile.html',)


@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('user data =',  password, first_name, last_name, username, email)
        print('fuck you')
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password != None or password == "":
            user.set_password(password)
        user.save()
        print('user object data ', user)
        messages.info(request, 'user ' + username +
                      " Profile Data updated successfuly ")
        return redirect('user_profile')


@login_required(login_url='login')
def about_us(request):
    return render(request, 'main/about_us.html', )


@login_required(login_url='login')
def contact_us(request):
    return render(request, 'main/contact_us.html', )


@login_required(login_url='login')
def product(request):
    Main_Categories = Main_Category.objects.all()
    category = Category.objects.all()
    products = Product.objects.all()
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    print(min_price)
    print(max_price)

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte=Int_FilterPrice)
    else:
        product = Product.objects.all()

    print("FilterPrice ==>", FilterPrice)

    print(category)
    context = {"Main_Categories": Main_Categories,

               'categories': category,
               'products': products,
               'min_price': min_price,
               'max_price': max_price,
               'FilterPrice': FilterPrice,
               }

    return render(request, 'main/product.html', context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(
            Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()

    t = render_to_string('ajax/product.html', {'products': allProducts})

    return JsonResponse({'data': t})


def shoping_cart(request):
    return render(request, 'cart/cart.html')


@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    cart = request.session.get('cart')
    print(cart)

    # tax = sum(i["tax"] for i in cart.values() if i)
    # packing_cost = sum(i["packing_cost"] for i in cart.values() if i)
    # print("Delivery_Data => in number", str(packing_cost), str(tax))
    # print(tax, packing_cost)
    # data = {
    #     'packing_cost': packing_cost,
    #     'tax': tax
    # }
    copoun = None
    valid_copoun = None
    invalid_copoun = None
    if request.method == 'GET':
        codon_copon = request.GET.get('coupon_csode')
        print(codon_copon)
        if codon_copon:
            try:
                copoun = Codon_copon.objects.get(condon=codon_copon)
                valid_copoun = 'valid copoun applaiend to current item '
            except:
                invalid_copoun = 'invalid copoun applaiend to current item '
    data = {'copoun': copoun, "valid_copoun": valid_copoun,
            "invalid_copoun": invalid_copoun}

    return render(request, 'cart/cart.html', data)


@login_required(login_url="login")
def cart_checkout(request):
    return render(request, 'cart/checkout.html')
