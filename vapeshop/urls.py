from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('shoppingcart/', include('shopping_cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('reviews/', include('reviews.urls')),
    path('contact/', include('contact_form.urls')),

    # Had to use https://adamj.eu/tech/2020/02/10/robots-txt/ to
    # get my robots.txt readable by lighthouse
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain")
        ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'vapeshop.views.error_404'
handler500 = 'vapeshop.views.error_500'
