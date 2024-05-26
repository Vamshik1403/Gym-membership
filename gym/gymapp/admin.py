from django.contrib import admin
from .models import Product,Cart,Attendance,Enrollment,MembershipPlan,Trainer

#Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)