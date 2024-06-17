from django.urls import path

from apps.authentication.views import LoginView, SignupView, InviteView, RequestPasswordResetView, VerifyResetView, \
	ResetPasswordView, ChangePasswordView, CreateOrganizationKeysView, GetOrgKeysView

urlpatterns = [
	path("login/", LoginView.as_view()),
	path("signup/", SignupView.as_view()),
	path("invite/", InviteView.as_view()),
	path("reset-password/request/", RequestPasswordResetView.as_view()),
	path("reset-password/verify/", VerifyResetView.as_view()),
	path("reset-password/reset/", ResetPasswordView.as_view()),
	path('change-password/', ChangePasswordView.as_view()),
	path('create-org-keys/', CreateOrganizationKeysView.as_view()),
	path('get-org-keys/', GetOrgKeysView.as_view()),
]
