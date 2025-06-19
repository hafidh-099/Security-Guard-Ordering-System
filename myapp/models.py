from django.db import models

# ------------------- Security Office -------------------
class SecurityOffice(models.Model):
    STATUS_CHOICES = [
        ("PRIVATE", "PRIVATE"),
        ("PUBLIC", "PUBLIC"),
    ]

    officename = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.officename}"


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
    phone = models.BigIntegerField()  # phone numbers may exceed normal IntegerField
    adress = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    worked_office = models.ForeignKey(SecurityOffice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


# ------------------- Organization -------------------
class Organization(models.Model):
    STATUS_CHOICES = [
        ("PRIVATE", "PRIVATE"),
        ("PUBLIC", "PUBLIC"),
    ]

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    bussiness = models.CharField(max_length=20)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name}"


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

    def __str__(self):
        return f"Order from {self.Organization_name} to {self.Office_name}"
