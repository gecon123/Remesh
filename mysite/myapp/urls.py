from django.urls import path
from . import views
from .views import FirstView, MessView, ThoView, AddConvoView, AddMessView, AddThoView, searchbar

urlpatterns = [
    path('', FirstView.as_view(), name="home"),
    path('conversation/<int:conversation_id>', MessView.as_view(), name='conversations_by_id'),
    path('message/<int:thought_id>', ThoView.as_view(), name='messages_by_id'),
    path('add_conversation', AddConvoView.as_view(), name='add_convo'),
    path('conversation/add_message', AddMessView.as_view(), name='add_mess'),
    path('message/add_tho', AddThoView.as_view(), name='add_tho'),
    path('searchbar', views.searchbar, name="searchbar")
] 