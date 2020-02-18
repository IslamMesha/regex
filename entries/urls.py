from django.urls import path

from entries.views import EntryListView, EntryFormView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/', EntryListView.as_view(), name='list'),
    path('insert', EntryFormView.as_view(), name='insert'),
    # path('login/', auth_views.auth_login, kwargs={'template_name': 'admin/login.html'}, name='login'),
    # path('logout/', auth_views.auth_logout, kwargs={'next_page': reverse_lazy('home')}, name='logout')
]
