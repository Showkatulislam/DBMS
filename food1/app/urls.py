from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import loginForm,MyPasswordChangeForm
urlpatterns = [
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductViewDetail.as_view(), name='product-detail'),
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('paymentdone/',views.payment_done,name='paymentdone'),

    path('accounts/login/',auth_views.LoginView.as_view(
    template_name='app/login.html',authentication_form=loginForm),name='login'),

    # path('accounts/login',auth_views.LoginView.as_view(
    # template_name='app/login.html',authentication_form=loginForm),name='login'),

    path('passwordchange/',auth_views.PasswordChangeView.as_view
    (template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view
    (template_name='app/passwordchangedone.html',form_class=MyPasswordChangeForm,),name='passwordchangedone'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerRegistationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/',views.search,name='search-pro'),
    path('lower/<str:cat>',views.lower,name='lower')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)