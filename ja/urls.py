from django.urls import path

from ja.views import JAThankYouView, JAView

app_name = "ja"

urlpatterns = [
    path('', JAView.as_view(), name="ja"),
    path('thank-you/', JAThankYouView.as_view(), name="thank_you"),
]