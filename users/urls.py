from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "users"

urlpatterns = [
    path("", views.lookers_list, name="lookers_list"),
    path(
        "looker-detail/<int:looker_id>/",
        views.looker_detail_view,
        name="looker_detail_view",
    ),
    path(
        "looker-profile/<int:looker_id>/",
        views.looker_profile_view,
        name="looker_profile_view",
    ),
    path(
        "edit-looker-profile/<int:looker_id>/",
        views.edit_looker_profile_view,
        name="edit_looker_profile_view",
    ),
    path("lookers-statistics", views.lookers_statistics, name="lookers_statistics"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup, name="signup"),
    path(
        "terms-and-conditions", views.terms_and_conditions, name="terms-and-conditions"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
