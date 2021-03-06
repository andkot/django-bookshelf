from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books', include('book.urls')),
    path('books_owners/', include('books_owner.urls')),
    path('api/', include('book.urls'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.BOOKS_URL, document_root=settings.BOOKS_ROOT)
