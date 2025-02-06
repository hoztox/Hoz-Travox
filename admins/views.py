from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response({"message": "Customer added successfully", "customer": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
     
        return Customer.objects.filter(create_parent_acc=True)
    

class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response({"message": "Supplier added successfully", "supplier": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class =SupplierSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Supplier deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class AgentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": " Agent added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AgentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class =AgentSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Agent deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        

class AirlineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            airline = serializer.save()
            return Response({"message": " Airline added successfully", "airline": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AirlineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class =AirlineSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Airline deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class UserManagementListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserManagement.objects.all()
    serializer_class = UserManagementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": " User added successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserManagementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserManagement.objects.all()
    serializer_class =UserManagementSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save()
            return Response({"message": " Service added successfully", "service": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Service.objects.all()
    serializer_class =ServiceSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Service deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ImportantDatesListCreateAPIView(generics.ListCreateAPIView):
    queryset = ImportantDates.objects.all()
    serializer_class =ImportantDatesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            dates = serializer.save()
            return Response({"message": " ImportantDates added successfully", "dates": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImportantDatesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =ImportantDates.objects.all()
    serializer_class =ImportantDatesSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " ImportantDates deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ChangeStatusAPIView(APIView):
    def patch(self, request, pk, *args, **kwargs):
        important_date = get_object_or_404(ImportantDates, pk=pk)
        new_status = request.data.get("status")

        if new_status not in ["Paid", "Unpaid"]:
            return Response({"error": "Invalid status. Choose 'Paid' or 'Unpaid'."}, status=status.HTTP_400_BAD_REQUEST)

        important_date.status = new_status
        important_date.save()

        return Response({"message": f"Status updated to {new_status}", "data": ImportantDatesSerializer(important_date).data}, status=status.HTTP_200_OK)
    


 

class ImportantDatesFilterAPIView(APIView):
    def post(self, request):
        from_date = request.data.get('from_date')
        to_date = request.data.get('to_date')
        item_name = request.data.get('item_name')

        queryset = ImportantDates.objects.all()

   
        if from_date and to_date:
            from_date = parse_date(from_date)
            to_date = parse_date(to_date)
            queryset = queryset.filter(due_date__range=[from_date, to_date])

 
        if item_name:
            queryset = queryset.filter(item_name__icontains=item_name)

        serializer = ImportantDatesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 

 
class AssetsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class =AssetsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            assets = serializer.save()
            return Response({"message": " Assets added successfully", "assets": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Assets.objects.all()
    serializer_class =AssetsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Assets deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

 

 

class GroupAssetsByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
       
        assets = Assets.objects.all()
        
       
        grouped_assets = {}

      
        for asset in assets:
            if asset.title not in grouped_assets:
                grouped_assets[asset.title] = []
            grouped_assets[asset.title].append(asset)

   
        result = {}
        for title, assets_in_group in grouped_assets.items():
            result[title] = []
            for asset in assets_in_group:
                asset_data = {
                    'unique_id': asset.unique_id,
                    'acc_head': asset.acc_head,
                    'acc_number': asset.acc_number,
                    'ifsc': asset.ifsc,
                    'op_balance': asset.op_balance,
                    'cr_or_dr': asset.cr_or_dr,
                    'notes': asset.notes,
                    'email': asset.email,
                }
                result[title].append(asset_data)

        return Response(result)


     


class ExpensesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class =ExpensesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            expenses = serializer.save()
            return Response({"message": " Expenses added successfully", "expenses": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpensesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Expenses.objects.all()
    serializer_class =ExpensesSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Expenses deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

 

class GroupExpensesByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
     
        expenses = Expenses.objects.all()
        
       
        grouped_expenses = {}

       
        for expense in expenses:
            if expense.title not in grouped_expenses:
                grouped_expenses[expense.title] = []
            grouped_expenses[expense.title].append(expense)
 
        result = {}
        for title, expenses_in_group in grouped_expenses.items():
            result[title] = []
            for expense in expenses_in_group:
                expense_data = {
                    'unique_id': expense.unique_id,
                    'acc_head': expense.acc_head,
                    'op_balance': expense.op_balance,
                    'cr_or_dr': expense.cr_or_dr,
                    'notes': expense.notes,
                }
                result[title].append(expense_data)

        return Response(result)


class IncomeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class =IncomeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            income = serializer.save()
            return Response({"message": " Income added successfully", "income": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Income.objects.all()
    serializer_class =IncomeSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Income deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class GroupIncomeByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
    
        incomes = Income.objects.all()   
        grouped_incomes = {}

     
        for income in incomes:
            if income.title not in grouped_incomes:
                grouped_incomes[income.title] = []
            grouped_incomes[income.title].append(income)

       
        result = {}
        for title, incomes_in_group in grouped_incomes.items():
            result[title] = []
            for income in incomes_in_group:
                income_data = {
                    'unique_id': income.unique_id,
                    'acc_head': income.acc_head,
                    'op_balance': income.op_balance,
                    'cr_or_dr': income.cr_or_dr,
                    'notes': income.notes,
                }
                result[title].append(income_data)

        return Response(result)


class LiabilityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Liability.objects.all()
    serializer_class =LiabilitySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            liability = serializer.save()
            return Response({"message": " Liability added successfully", "liability": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiabilityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Liability.objects.all()
    serializer_class =LiabilitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Liability deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


 

class GroupLiabilityByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
 
        liabilities = Liability.objects.all()
        
     
        grouped_liabilities = {}

   
        for liability in liabilities:
            if liability.title not in grouped_liabilities:
                grouped_liabilities[liability.title] = []
            grouped_liabilities[liability.title].append(liability)

 
        result = {}
        for title, liabilities_in_group in grouped_liabilities.items():
            result[title] = []
            for liability in liabilities_in_group:
                liability_data = {
                    'unique_id': liability.unique_id,
                    'acc_head': liability.acc_head,
                    'op_balance': liability.op_balance,
                    'cr_or_dr': liability.cr_or_dr,
                    'notes': liability.notes,
                }
                result[title].append(liability_data)

        return Response(result)



class GlobalAssetsListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalAssets.objects.all()
    serializer_class =GlobalAssetsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            assets = serializer.save()
            return Response({"message": "   Assets added successfully", "assets": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalAssetsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalAssets.objects.all()
    serializer_class =GlobalAssetsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Global Assets deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

 

class GroupGlobalAssetsByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_assets = GlobalAssets.objects.all()
 
        grouped_global_assets = {}
 
        for global_asset in global_assets:
            if global_asset.title not in grouped_global_assets:
                grouped_global_assets[global_asset.title] = []
            grouped_global_assets[global_asset.title].append(global_asset)

     
        result = {}
        for title, assets_in_group in grouped_global_assets.items():
            result[title] = []
            for asset in assets_in_group:
                asset_data = {
                    'unique_id': asset.unique_id,
                    'acc_head': asset.acc_head,
                    'notes': asset.notes,
                }
                result[title].append(asset_data)

        return Response(result)



class GlobalAgentsListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalAgents.objects.all()
    serializer_class =GlobalAgentsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": " Agents added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalAgentsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalAgents.objects.all()
    serializer_class =GlobalAgentsSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Agents deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalAgentByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_agents = GlobalAgents.objects.all()
 
        grouped_global_agents = {}
 
        for global_agent in  global_agents:
            if global_agent.title not in grouped_global_agents:
                grouped_global_agents[global_agent.title] = []
            grouped_global_agents[global_agent.title].append(global_agent)

     
        result = {}
        for title, agents_in_group in grouped_global_agents.items():
            result[title] = []
            for asset in agents_in_group:
                asset_data = {
                    'unique_id': asset.unique_id,
                    'acc_head': asset.acc_head,
                    'notes': asset.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    
class  GlobalAirlineListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalAirline.objects.all()
    serializer_class =GlobalAirlineSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": " Airline added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalAirlineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalAirline.objects.all()
    serializer_class =GlobalAirlineSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Airline deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalAirlineByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalAirline.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    
class  GlobalCustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalCustomer.objects.all()
    serializer_class =  GlobalCustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": "Customer added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalCustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalCustomer.objects.all()
    serializer_class =GlobalCustomerSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalCustomerByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalCustomer.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    

class  GlobalExpenseListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalExpense.objects.all()
    serializer_class =  GlobalExpenseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": "Expense added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalExpense.objects.all()
    serializer_class =GlobalExpenseSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": " Expense deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalExpenseByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalExpense.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    

class  GlobalIncomeListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalIncome.objects.all()
    serializer_class =  GlobalIncomeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": "Income added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalIncomeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalIncome.objects.all()
    serializer_class =GlobalIncomeSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Income deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalIncomeByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalIncome.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    
class  GlobalLiabilityListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalLiability.objects.all()
    serializer_class = GlobalLiabilitySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": "Liability added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalLiabilityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalLiability.objects.all()
    serializer_class =GlobalLiabilitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Liability deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalLiabilityByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalLiability.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    
class GlobalNeutralListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalNeutral.objects.all()
    serializer_class =GlobalNeutralSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": "Neutral added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalNeutralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalNeutral.objects.all()
    serializer_class =GlobalNeutralSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Neutral deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalNeutralByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalNeutral.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    
class GlobalSuppliersListCreateAPIView(generics.ListCreateAPIView):
    queryset = GlobalSuppliers.objects.all()
    serializer_class =GlobalSuppliersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            agent = serializer.save()
            return Response({"message": "Suppliers added successfully", "agent": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GlobalSuppliersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =GlobalSuppliers.objects.all()
    serializer_class =GlobalSuppliersSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Suppliers deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
 

class GroupGlobalSuppliersByTitleAPIView(APIView):

    def get(self, request, *args, **kwargs):
  
        global_airline = GlobalSuppliers.objects.all()
 
        grouped_global_airline = {}
 
        for global_agent in   global_airline:
            if global_agent.title not in grouped_global_airline:
                grouped_global_airline[global_agent.title] = []
            grouped_global_airline[global_agent.title].append(global_agent)

     
        result = {}
        for title, airline_in_group in grouped_global_airline.items():
            result[title] = []
            for airline in airline_in_group:
                asset_data = {
                    'unique_id': airline.unique_id,
                    'acc_head': airline.acc_head,
                    'notes': airline.notes,
                }
                result[title].append(asset_data)

        return Response(result)
    
class NeutralListCreateAPIView(generics.ListCreateAPIView):
    queryset = Neutral.objects.all()
    serializer_class = NeutralSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response({"message": "Neutral added successfully", "customer": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NeutralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neutral.objects.all()
    serializer_class = NeutralSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Neutral deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class NeutralListView(generics.ListAPIView):
    serializer_class = NeutralSerializer
    
    def get_queryset(self):
     
        return Neutral.objects.filter(create_parent_acc=True)
    