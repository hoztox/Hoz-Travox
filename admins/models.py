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

    def __str__(self):
        return self.name


