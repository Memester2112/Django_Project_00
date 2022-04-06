from django.urls import path
from . import views

#MAPPING URLS TO FUNCTIONS 
#All url requests from the urls.py in the mysite(main app) starting with 'plaground/' are being directed in the app "play" to the file play/urls.py 
"""
Then using the urlpatterns in play/urls.py we are redirecting for a specific page plaground/hello/ using the first entry in urlpatterns. It connects this particular path to this view
"""
urlpatterns = [
  path('hello/', views.say_hello)
]