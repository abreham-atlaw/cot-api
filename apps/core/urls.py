from django.urls import path

from apps.core.views import GenerateReportView, TranslateView

urlpatterns = [
	path("generate-report/", GenerateReportView.as_view()),
	path("translate/", TranslateView.as_view()),
]
