from django.urls import path
from authentication.views import login, logout, get_item_json

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('json/', get_item_json, name='get_item_json'),
]