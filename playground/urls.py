# This file works with URL patterns.

# A URL pattern is the general form of a URL - for example: ./newsarchive/<year>/<month>/
# To get from a URL to a view Django uses what is known as "URLconfs". A URLconf maps URL patterns to views.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The path() function receives four arguments, two required and two optional. The arguments below are routes. Route is a string that contains a URL pattern.
    path('admin/', admin.site.urls),

    # The include() function allows you to reference other URLconfs. Each time Django finds include() it cuts off any part of the URL that matches up to that point and sends the remaining string to the included URLconf to follow the process.
    path('show_something_app/', include('show_something_app.urls'))
]