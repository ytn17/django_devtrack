from django.urls import path

from issues.views import create_issue, create_reporter, get_issues, get_open_issues, get_reporters


urlpatterns = [
    # reporter endpoints
    path("create-reporter/", create_reporter, name="create_reporters"),
    path("reporters/", get_reporters, name="get_all_reporters"),
    path("reporters/<int:id>", get_reporters, name="get_reporter_by_id"),

    #issue endpoints
    path("create-issue/", create_issue, name="create_issues"),
    path("issues/", get_issues, name="get_all_issues"),
    path("issues/status/", get_open_issues, name="get_all_open_issues")

]