from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


app_name = 'accounts_app'
urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name='accounts_app/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='accounts_app/logout.html'), name='logout'),
    # path('password_change', auth_views.PasswordChangeView.as_view(template_name='accounts_app/password_change.html'),
    #      name='password_change'),
    # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='accounts_app/password_change_done.html'),
    #      name='password_change_done'),
    path('password_reset', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts_app:password_reset_done'), email_template_name='accounts_app/password_reset_email.html', template_name='accounts_app/password_reset.html'),
         name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts_app/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts_app:password_reset_complete'), template_name='accounts_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done', auth_views.LoginView.as_view(template_name='accounts_app/password_reset_complete.html'),
         name='password_reset_complete'),
]
