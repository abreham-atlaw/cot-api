from django.urls import path

from apps.core.views import GenerateReportView

urlpatterns = [
	path("generate-report/", GenerateReportView.as_view()),
]
