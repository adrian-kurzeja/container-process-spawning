from django.conf.urls import include, url

from main.settings import DEBUG

urlpatterns = [
]

if DEBUG:
    from django.contrib import admin

    admin.autodiscover()

    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
    ]

