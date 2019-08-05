from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from all_books.views import HomeView, BorrowSummuryView, PaymentView, confirm, search
from slideshow.views import slides

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('books/', include('all_books.urls')),
    path('borrow-list/', BorrowSummuryView.as_view(), name='borrow-list'),
    path('fine/payment/<payment-option>',
         PaymentView.as_view(), name='fine-payment'),
    path('confirm-request/<int:pk>/',
         confirm, name='confirm-request'),
    path('search/', search, name="search"),
    path('slide/', slides, name='slide')
    # path('borrow/', include('book_cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'DIIT Library'
admin.site.index_title = 'Library Management System'
admin.site.site_title = 'Admin'
