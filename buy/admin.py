from django.contrib import admin
from buy.models import *


class BuyHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('date','time')

admin.site.register(Product)  # Use the default options
admin.site.register(BuyHistory, BuyHistoryAdmin)  # Use the default options
admin.site.register(ProductCatalog)  # Use the default options

#credentials: username:user , password: admin
