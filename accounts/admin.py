from django.contrib import admin
from accounts.models import Profile, Wallet, Transaction



admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Transaction)