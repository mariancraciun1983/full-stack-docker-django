from django.conf.urls import url
from .views import index, test_wait, test_async, test_ajax, test_email

urlpatterns = [
    url(r'test_wait', test_wait, name='tools_test_wait'),
    url(r'test_async', test_async, name='tools_test_async'),
    url(r'test_ajax', test_ajax, name='tools_test_ajax'),
    url(r'test_email', test_email, name='tools_test_email'),
    url('', index, name='tools_index'),
]
