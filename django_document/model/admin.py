from django.contrib import admin

from .models import Manufacturer, User, Car, Pizza, Topping, FacebookUser, InstagramUser, Idol, Group, Membership, \
    Place, Restaurant, Waiter

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)