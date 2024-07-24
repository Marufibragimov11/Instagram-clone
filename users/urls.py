from .serializers import SignUpSerializer
from django.urls import path
from .views import CreateUserView, VerifyAPIView, GetNewVerification, ChangeUserInformationView, ChangeUserPhotoView, \
    LoginRefreshView, LogOutView, ForgotPasswordView

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('login/refresh/', LoginRefreshView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerification.as_view()),
    path('change-user/', ChangeUserInformationView.as_view()),
    path('change-user-photo/', ChangeUserPhotoView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),
]
