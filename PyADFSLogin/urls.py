from django.conf.urls.defaults import patterns, include, url

from PyADFSLogin.views import hello, secret, do_login, SAML_handler
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PyADFSLogin.views.home', name='home'),
    # url(r'^PyADFSLogin/', include('PyADFSLogin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('',
                    ('^$', hello),
                    ('^secret/$',  secret),
                    ('^accounts/login/$',  do_login),
                    ('^SAML/$', SAML_handler))
