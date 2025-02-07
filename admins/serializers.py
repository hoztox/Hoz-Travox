from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class  UserManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserManagement
        fields = '__all__'

class  ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Service
        fields = '__all__'

class  ImportantDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model =   ImportantDates
        fields = '__all__'

class  AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Assets
        fields = '__all__'

class  ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Expenses
        fields = '__all__'


class  IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Income
        fields = '__all__'

class  LiabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model =   Liability
        fields = '__all__'

class  GlobalAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalAssets
        fields = '__all__'

class  GlobalAgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalAgents
        fields = '__all__'

class  GlobalAirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalAirline
        fields = '__all__'


class  GlobalCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalCustomer
        fields = '__all__'

class  GlobalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalExpense
        fields = '__all__'

class  GlobalIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalIncome
        fields = '__all__'

class  GlobalLiabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalLiability
        fields = '__all__'

class  GlobalNeutralSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalNeutral
        fields = '__all__'

class GlobalSuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model =   GlobalSuppliers
        fields = '__all__'

class NeutralSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Neutral
        fields = '__all__'


from rest_framework import serializers
from .models import Quotation, ServiceDetail

class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = ['id', 'service_name', 'fare']

class QuotationSerializer(serializers.ModelSerializer):
    services = ServiceDetailSerializer(many=True)

    class Meta:
        model = Quotation
        fields = '__all__'

    def create(self, validated_data):
        services_data = validated_data.pop('services', [])
        quotation = Quotation.objects.create(**validated_data)
        for service in services_data:
            ServiceDetail.objects.create(quotation=quotation, **service)
        return quotation

    def update(self, instance, validated_data):
        services_data = validated_data.pop('services', [])
        
       
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

   
        instance.services.all().delete()
        for service in services_data:
            ServiceDetail.objects.create(quotation=instance, **service)

        return instance
