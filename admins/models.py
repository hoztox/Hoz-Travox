from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    create_child_acc = models.BooleanField(default=False)
    create_parent_acc = models.BooleanField(default=False)
    choose_parent = models.CharField(max_length=255, null=True, blank=True)  
    op_balance = models.IntegerField(null=True, blank=True)   
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )
    has_credit_limit = models.BooleanField(default=False)
    enter_limit = models.IntegerField(null=True, blank=True)   
    contact_details = models.TextField(null=True, blank=True)  
    gst_in = models.CharField(max_length=255, null=True, blank=True)  
    email = models.EmailField(unique=True, null=True, blank=True)  
    staff_or_group = models.CharField(max_length=255, null=True, blank=True)  
    unique_code = models.CharField(max_length=255, unique=True)  
    id_or_pan = models.CharField(max_length=255, null=True, blank=True)   
    notes = models.TextField(null=True, blank=True)   
    acl_type = models.CharField(
        max_length=20,
        choices=[('BC', 'BC'), ('BB', 'BB')],null=True, blank=True
    )
    acc_type = models.CharField(
        max_length=20,
        choices=[('Customer', 'Customer') ],null=True, blank=True
    )
    def __str__(self):
        return self.name

  

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    has_child_acc = models.BooleanField(default=False)  
    
    op_balance = models.IntegerField(null=True, blank=True)   
    acc_type = models.CharField(
        max_length=20,
        choices=[('Supplier', 'Supplier'), ('Airline Supplier', 'Airline Supplier')],null=True, blank=True
    )
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )
     
    contact_details = models.TextField(null=True, blank=True)  
    tax_id = models.CharField(max_length=255, null=True, blank=True)  
    email = models.EmailField(unique=True, null=True, blank=True)      
    unique_code = models.CharField(max_length=255, unique=True)     
    notes = models.TextField(null=True, blank=True)   
     
    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=255)   
    op_balance = models.IntegerField(null=True, blank=True)   
    acc_type = models.CharField(
        max_length=20,
       choices=[('Agent', 'Agent')],null=True, blank=True
    )
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )
   
    location =  models.TextField(null=True, blank=True)   
    contact_details = models.TextField(null=True, blank=True)  
    gst_in = models.CharField(max_length=255, null=True, blank=True)  
    email = models.EmailField(unique=True, null=True, blank=True)      
    unique_code = models.CharField(max_length=255, unique=True)     
    notes = models.TextField(null=True, blank=True)   
     
    def __str__(self):
        return self.name

class Airline(models.Model):
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    unique_id = models.CharField(max_length=255, unique=True, editable=False)  

    def save(self, *args, **kwargs):
        if not self.unique_id: 
            last_airline = Airline.objects.order_by('-id').first()
            if last_airline and last_airline.unique_id:
                last_number = int(last_airline.unique_id[3:])  
                new_number = last_number + 1
            else:
                new_number = 1000   

            self.unique_id = f"AIR{new_number}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class UserManagement(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255,null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    usertype = models.CharField(
        max_length=20,
       choices=[('Staff', 'Staff'),('Admin' , 'Admin')],null=True, blank=True
    )
    username =  models.CharField(max_length=255 ,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    unique_id = models.CharField(max_length=255, unique=True, editable=False,  null =True ,blank =True)  

    def save(self, *args, **kwargs):
        if not self.unique_id:
            last_user = UserManagement.objects.order_by('-id').first()
            if last_user and last_user.unique_id:
                last_number = int(last_user.unique_id[1:])   
                new_number = last_number + 1
            else:
                new_number = 1  

            self.unique_id = f"U{new_number:03d}"  

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Service(models.Model):
    name =  models.CharField(max_length=255)
    code = models.CharField(max_length=255, null = True ,blank= True)
    supplier_charge = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    

class ImportantDates(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    due_date = models.DateField(null =True ,blank=True)
    item_name =  models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    payable_to = models.CharField(max_length=255,null =True ,blank=True)
    contact_details = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unpaid')

    def __str__(self):
        return self.item_name
    
class Assets(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Cash And Bank Balance', 'Cash And Bank Balance'),
                ('Current assets','Current assets'),
                ('Deposite','Deposite'),
                ('Fixed assets','Fixed assets'),
                ('Investment','Investment'),
                ('Loan And Advances','Loan And Advances'),
                ('Staff Advances','Staff Advances'),
                ('Other assets','Other assets'),
                ('Branches','Branches'),
                ('Sundry Debtors','Sundry Debtors'),],null=True, blank=True
    )
    acc_type = models.CharField(
        max_length=20,
       choices=[('Bank', 'Bank')
                 ],null=True, blank=True
    )
    op_balance = models.IntegerField(null=True, blank=True) 
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )
    acc_number =  models.CharField(max_length=255,null =True,blank=True)
    ifsc =  models.CharField(max_length=255,null =True,blank=True)
    address = models.TextField(null=True, blank=True) 
    email = models.EmailField(unique=True, null=True, blank=True)  
    unique_code = models.CharField(max_length=255, unique=True, null=True,blank=True) 
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = Assets.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"AS{new_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.acc_head} - {self.title} ({self.unique_code})"


class Expenses(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Direct Expenses', 'Direct Expenses'),
                ('Indirect Expenses','Indirect Expenses'),
                ],null=True, blank=True
    )     
    op_balance = models.IntegerField(null=True, blank=True) 
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )  
    has_child_acc = models.BooleanField(default=False)  
    unique_code = models.CharField(max_length=255, unique=True, null=True,blank=True) 
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = Expenses.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"Ex{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title} ({self.unique_code})"
    
class Income(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Visa Service Incomes', 'Visa Service Incomes'),
                ('Ticketing Incomes','Ticketing Incomes'),
                ('Attestation Incomes','Attestation Incomes'),
                ('Emigration Income','Emigration Income'),
                ('Umrah Income','Umrah Income'),
                ('Other Incomes','Other Incomes'),
                ('Recruitment Incomes','Recruitment Incomes'),
                ('Insurance Incomes','Insurance Incomes'),
                ('Service Income','Service Income'),               
                ],null=True, blank=True
    )     
    op_balance = models.IntegerField(null=True, blank=True) 
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )  
    has_child_acc = models.BooleanField(default=False)  
    unique_code = models.CharField(max_length=255, unique=True, null=True,blank=True) 
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = Income.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"IN{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title} ({self.unique_code})"
    



class Liability(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Capital Account', 'Capital Account'),
                ('Current Liabilities','Current Liabilities'),
                ('Reserves And Surplus A/C','Reserves And Surplus A/C'),
                ('Salary Payable','Salary Payable'),
                ('Statutary Liabilities','Statutary Liabilities'),
                ('Other Liabilities','Other Liabilities'),
                ('Branches','Branches'),
                ('Sundry Creditors','Sundry Creditors'),
                ('Secured Loan','Secured Loan'),   
                ('Insecured Loan','Insecured Loan'),               
                ],null=True, blank=True
    )     
    op_balance = models.IntegerField(null=True, blank=True) 
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )  
    has_child_acc = models.BooleanField(default=False)  
    unique_code = models.CharField(max_length=255, unique=True, null=True,blank=True) 
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = Liability.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"LB{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title} ({self.unique_code})"
    

class GlobalAssets(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Cash And Bank Balance', 'Cash And Bank Balance'),
                ('Current assets','Current assets'),
                ('Deposite','Deposite'),
                ('Fixed assets','Fixed assets'),
                ('Investment','Investment'),
                ('Loan And Advances','Loan And Advances'),
                ('Staff Advances','Staff Advances'),
                ('Other assets','Other assets'),
                ('Branches','Branches'),
                ('Sundry Debtors','Sundry Debtors'),],null=True, blank=True
    )     
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalAssets.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GAS{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"
    

class GlobalAgents(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Agent', 'Agent'),
                 ],null=True, blank=True
    )     
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalAgents.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[3:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GAG{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"
    
class GlobalAirline(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Airline', 'Airline'),
                 ],null=True, blank=True
    )     
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalAirline.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[3:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GAL{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"
    
class GlobalCustomer(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Customer', 'Customer'),
                 ],null=True, blank=True
    )     
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalCustomer.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GC{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"

class GlobalExpense(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Direct Expenses', 'Direct Expenses'),
                ('Indirect Expenses', 'Indirect Expenses')
                 ],null=True, blank=True
    )     
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalExpense.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GE{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"


class GlobalIncome(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Visa Service Incomes', 'Visa Service Incomes'),
                ('Ticketing Incomes','Ticketing Incomes'),
                ('Attestation Incomes','Attestation Incomes'),
                ('Emigration Income','Emigration Income'),
                ('Umrah Income','Umrah Income'),
                ('Other Incomes','Other Incomes'),
                ('Recruitment Incomes','Recruitment Incomes'),
                ('Insurance Incomes','Insurance Incomes'),
                ('Service Income','Service Income'),               
                ],null=True, blank=True
    )      
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalIncome.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GI{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"
    
class GlobalLiability(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Capital Account', 'Capital Account'),
                ('Current Liabilities','Current Liabilities'),
                ('Reserves And Surplus A/C','Reserves And Surplus A/C'),
                ('Salary Payable','Salary Payable'),
                ('Statutary Liabilities','Statutary Liabilities'),
                ('Other Liabilities','Other Liabilities'),
                ('Branches','Branches'),
                ('Sundry Creditors','Sundry Creditors'),
                ('Secured Loan','Secured Loan'),   
                ('Insecured Loan','Insecured Loan'),               
                ],null=True, blank=True
    ) 
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalLiability.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GL{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"
    
class GlobalNeutral(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title = models.CharField(
        max_length=100,
       choices=[('Neutral', 'Neutral')
                             
                ],null=True, blank=True
    ) 
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalNeutral.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GN{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"

class GlobalSuppliers(models.Model):
    acc_head =  models.CharField(max_length=255,null =True,blank=True)
    title =  models.CharField(
        max_length=20,
        choices=[('Supplier', 'Supplier'), ('Airline Supplier', 'Airline Supplier')],null=True, blank=True
    )
    
    notes = models.TextField(null=True, blank=True) 
    unique_id = models.CharField(max_length=255, unique=True, editable=True, null=True, blank=True)

    def save(self, *args, **kwargs):
       
        if not self.unique_id:
            last_asset = GlobalSuppliers.objects.order_by('-id').first()
            if last_asset and last_asset.unique_id:
                last_number = int(last_asset.unique_id[2:])  
                new_number = last_number + 1
            else:
                new_number = 1001   

            
            self.unique_id = f"GS{new_number:04d}"

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.acc_head} - {self.title}"
    


class Neutral(models.Model):
    name = models.CharField(max_length=255)
    create_child_acc = models.BooleanField(default=False)
    create_parent_acc = models.BooleanField(default=False)
    choose_parent = models.CharField(max_length=255, null=True, blank=True)  
    op_balance = models.IntegerField(null=True, blank=True)   
    cr_or_dr = models.CharField(
        max_length=20,
        choices=[('CR', 'CR'), ('DR', 'DR')],null=True, blank=True
    )
    has_credit_limit = models.BooleanField(default=False)
    enter_limit = models.IntegerField(null=True, blank=True)   
    contact_details = models.TextField(null=True, blank=True)  
    gst_in = models.CharField(max_length=255, null=True, blank=True)  
    email = models.EmailField(unique=True, null=True, blank=True)  
    staff_or_group = models.CharField(max_length=255, null=True, blank=True)  
    unique_code = models.CharField(max_length=255, unique=True)  
    id_or_pan = models.CharField(max_length=255, null=True, blank=True)   
    notes = models.TextField(null=True, blank=True)   
    acl_type = models.CharField(
        max_length=20,
        choices=[('BC', 'BC'), ('BB', 'BB')],null=True, blank=True
    )
    acc_type = models.CharField(
        max_length=20,
        choices=[('Neutral', 'Neutral') ],null=True, blank=True
    )
    def __str__(self):
        return self.name