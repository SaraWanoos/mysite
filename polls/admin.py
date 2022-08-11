from django.contrib import admin

from .models import Candidates,People,Election,Employee,Parties
admin.site.register(Parties)
admin.site.register(Candidates)
admin.site.register(People)
admin.site.register(Election)
admin.site.register(Employee)

