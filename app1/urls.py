from django.conf.urls import url

from . import views

urlpatterns = [
    # /app1
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^plot1d/$', views.Plot1DView.as_view(), name='plot1d'),
    url(r'^plot1d_multiple/(?P<n>\d+)/$',
        views.Plot1DMultipleView.as_view(), name='plot1d_multiple'),
    

]
