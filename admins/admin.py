from django.contrib import admin


from .models import *

 
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Agent)
admin.site.register(Airline)
admin.site.register(UserManagement)
admin.site.register(Service)
admin.site.register(ImportantDates)
admin.site.register(Assets)
admin.site.register(Expenses)
admin.site.register(Income)
admin.site.register(Liability)
admin.site.register(GlobalAssets)
admin.site.register(GlobalAgents)
admin.site.register(GlobalAirline)
admin.site.register(GlobalCustomer)
admin.site.register(GlobalExpense)
admin.site.register(GlobalIncome)
admin.site.register(GlobalLiability)
admin.site.register(GlobalNeutral)
admin.site.register(GlobalSuppliers)
admin.site.register(Neutral)
admin.site.register(Quotation)
admin.site.register(ServiceDetail)