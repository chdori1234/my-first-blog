from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    
    #url ( '^' ,  include ( 'django.contrib.auth.urls' ),

    url(r'^$',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': 'blog/login.html'
        }
    ),
    url(
        r'^accounts/logout/$',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': '/'
        }
    ),

]
