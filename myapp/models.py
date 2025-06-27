from django.db import models
from django.contrib.auth.models import User  # needed for login links

# ------------------- Security Office -------------------
class SecurityOffice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # used for login
    STATUS_CHOICES = [
        ("PRIVATE", "PRIVATE"),
        ("PUBLIC", "PUBLIC"),
    ]
    officename = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"SecurityOffice: {self.officename}"


# ------------------- Armed Security Guard -------------------
class ArmedSecurityGuard(models.Model):
    STATUS_CHOICES = [
        ("ORDINARY", "ordinary"),
        ("ADVANCED", "advanced"),
    ]

    GENDER_CHOICES = [
        ("M", "MALE"),
        ("F", "FEMALE"),
    ]

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.BigIntegerField()  # for large phone numbers
    adress = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    worked_office = models.ForeignKey(SecurityOffice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Guard: {self.name} ({self.status})"


# ------------------- Organization -------------------
class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # used for login
    STATUS_CHOICES = [
        ("PRIVATE", "PRIVATE"),
        ("PUBLIC", "PUBLIC"),
    ]
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    bussiness = models.CharField(max_length=20)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Organization: {self.name}"


# ------------------- Order -------------------
class Order(models.Model):
    GENDER_CHOICES = [
        ("M", "MALE"),
        ("F", "FEMALE"),
    ]

    STATUS_CHOICES = [
        ("ORDINARY", "ordinary"),
        ("ADVANCED", "advanced"),
    ]

    Office_name = models.ForeignKey(SecurityOffice, on_delete=models.CASCADE)
    Organization_name = models.ForeignKey(Organization, on_delete=models.CASCADE)
    guardAge = models.IntegerField()
    guardSex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    guardStatus = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    # NEW: approval field to allow Security Office to approve/reject order
    approved = models.BooleanField(null=True, blank=True)  # None: pending, True: approved, False: rejected

    def __str__(self):
        status = (
            "Pending" if self.approved is None
            else "Approved" if self.approved
            else "Rejected"
        )
        return f"Order from {self.Organization_name.name} to {self.Office_name.officename} - {status}"
