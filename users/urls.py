from django.urls import path

from users.views import RegisterView, ConfirmEmailCodeView, LoginView, logout_view, user_detail_view, UpdateDetail

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmEmailCodeView.as_view(), name='confirm'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/', user_detail_view, name='details'),
    path('update/<int:pk>/', UpdateDetail.as_view(), name='update')
]
