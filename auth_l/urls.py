from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from article import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('article.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('', article_views.art_lst, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
