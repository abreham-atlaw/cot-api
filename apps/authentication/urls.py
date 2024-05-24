from django.urls import path

from apps.authentication.views import LoginView, SignupView, InviteView, RequestPasswordResetView, VerifyResetView, \
	ResetPasswordView

urlpatterns = [
	path("login/", LoginView.as_view()),
	path("signup/", SignupView.as_view()),
	path("invite/", InviteView.as_view()),
	path("reset-password/request/", RequestPasswordResetView.as_view()),
	path("reset-password/verify/", VerifyResetView.as_view()),
	path("reset-password/reset/", ResetPasswordView.as_view())
]
