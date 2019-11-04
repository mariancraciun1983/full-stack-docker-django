from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from app_movies.models import Movie
from django.urls import reverse
from .models import Cart, CartItems
from django.http import Http404


@csrf_protect
def index(request):
    cart = None
    if request.method == "POST":
        # Easier for this demo to not allow changes to the cart as guest
        if request.user.is_anonymous:
            return redirect(reverse("auth-login"))
        # find or create the cart
        cart, _ = Cart.objects.get_or_create(status=Cart.NEW, user=request.user)
        movies = request.POST.getlist("movie[]")
        quantities = request.POST.getlist("quantity[]")
        if len(movies) != len(quantities):
            raise Http404
        # !TODO reduce the num of queries with movie/qty diffing
        for idx in range(len(movies)):
            movie_id = movies[idx]
            # !TODO quantity needs verification for int/in-range
            quantity = int(quantities[idx])
            movie = get_object_or_404(Movie, id=movie_id)
            if quantity > 0:
                cartitem, created = CartItems.objects.get_or_create(
                    cart=cart, movie=movie, defaults={"quantity": quantity}
                )
                if not created:
                    if 'add' in request.POST:
                        cartitem.quantity = cartitem.quantity + quantity
                        cartitem.save()
                    else:
                        cartitem.quantity = quantity
                        cartitem.save()
            else:
                CartItems.objects.filter(cart=cart, movie=movie).delete()
    elif not request.user.is_anonymous:
        cart = Cart.objects.get(status=Cart.NEW, user=request.user)
    return render(request, "cart/index.html", {"cart": cart})
