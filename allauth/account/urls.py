from django.urls import path, re_path

from . import views


urlpatterns = [
    path("signup/", views.error, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path(
        "password/change/",
        views.error,
        name="account_change_password",
    ),
    path("password/set/", views.error, name="account_set_password"),
    path("inactive/", views.error, name="account_inactive"),
    # E-mail
    path("email/", views.error, name="account_email"),
    path(
        "confirm-email/",
        views.error,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        views.error,
        name="account_confirm_email",
    ),
    # password reset
    path("password/reset/", views.error, name="account_reset_password"),
    path(
        "password/reset/done/",
        views.error,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.error,
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        views.error,
        name="account_reset_password_from_key_done",
    ),
]
