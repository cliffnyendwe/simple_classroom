# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from contact_us.views import contact_us
from registration.backends.simple.views import RegistrationView

from simple_classroom.apps.classroom.views import HomeView, ProfileView
from simple_classroom.apps.classroom.forms import StudentRegistrationForm


urlpatterns = patterns(
    '',
    (r'', include('simple_classroom.apps.classroom.urls')),
    (r'', include('simple_classroom.apps.downloads.urls')),
    (r'', include('simple_classroom.apps.bibliography.urls')),
    # Accounts URLs
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(
        r'^accounts/register/$',
        RegistrationView.as_view(form_class=StudentRegistrationForm),
        name='registration_register'),
    (r'^accounts/', include('registration.backends.default.urls')),

    (r'^password/reset/fail/', TemplateView.as_view(template_name="registration/password_reset_fail.html")),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete, name='password_reset_complete'),
    # Admin URLs
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),

    # Site URLs
    url(r'^(?P<site>[A-Za-z]*)/$', HomeView.as_view(), name='home'),
    url(r'^contact_us/', contact_us, name='contact_us'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('django.contrib.flatpages.views',
                        (r'^(?P<url>.*/)$', 'flatpage'),)
