from django.urls import path
from .views import index, upload_gtd, ShowGtdView, test_view, show_gtd_file, CDDLogin, CDDLogout, RegisterDoneView, handbook, GtdDetailView, GtdUpdateView, GtdDeleteView, RegisterUserView, profile


app_name = 'main'
urlpatterns = [
    path('handbook', handbook, name='handbook'),
   # path('register_user/done/', RegisterDoneView.as_view(), name='register_done'),
   # path('register_user/', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', CDDLogin.as_view(), name='login'),
    path('accounts/logout/', CDDLogout.as_view(), name='logout'),
    path('documents/update_gtd/<int:pk>', GtdUpdateView.as_view(), name='update_gtd'),
    path('documents/delete_gtd/<int:pk>', GtdDeleteView.as_view(), name='delete_gtd'),
    path('documents/show_gtd/file/<path:filename>', show_gtd_file, name='show_gtd_file'),
    path('documents/show_gtd/<int:pk>', GtdDetailView.as_view(), name='per_gtd'),
    path('documents/show_gtd', ShowGtdView.as_view(), name='show_gtd'),
    path('documents/upload_gtd', upload_gtd, name='upload_gtd'),
    path('test', test_view, name='test'),
    path('', index, name='index')
]
