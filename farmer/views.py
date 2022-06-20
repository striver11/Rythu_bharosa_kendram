from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductStatus, PurchaseAgroProduct, FarmerFeedback
from .forms import PurchaseAgroProductForm, FarmerFeedbackForm


# Create your views here.
def product_tracking(request):
    products = PurchaseAgroProduct.objects.all()

    return render(request, 'farmer/product_tracking.html', {'products': products})


def available_product(request):
    return render(request, 'farmer/available_products.html')


def crops_types(request):
    return render(request, 'farmer/crops_types.html')


def farmerHome(request):
    form = PurchaseAgroProductForm()
    if request.method == 'POST':
        name = request.session['name']
        products = request.POST.get('products')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        saveData = PurchaseAgroProduct(
            products=products,
            phone=phone,
            address=address,
            farmer_name=name,
        )
        saveData.save()

        return render(request, 'farmer/formerHome.html', {'form': form, 'msg': 'Oredr submitted Successfully.'})

    else:

        form = PurchaseAgroProductForm()

        return render(request, 'farmer/formerHome.html', {'form': form})


def feedback(request, product_id=0):
    product = PurchaseAgroProduct.objects.get(id=product_id)
    form = FarmerFeedbackForm()
    if request.method == 'POST':
        feedBack = request.POST.get('feedBack')
        saveFeedBack = FarmerFeedback(feedBack=feedBack, product=product)
        saveFeedBack.save()
        return render(request, 'farmer/feedback.html', {'form': form, 'product': product, 'msg': 'Feedback submitted Successfully.'})
    else:

        return render(request, 'farmer/feedback.html', {'form': form, 'product': product})
