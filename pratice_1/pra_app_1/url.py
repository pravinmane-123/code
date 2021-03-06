from django.conf.urls import url
from pra_app_1 import views
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^morning/', views.display),
    url(r'^evening/', views.dis),

]
