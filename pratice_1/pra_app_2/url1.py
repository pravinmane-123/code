from django.conf.urls import url
from pra_app_2 import views
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^even/', views.greeting),

]