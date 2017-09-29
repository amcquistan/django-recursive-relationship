# hrmgmt/models.py
from django.db import models

class Employee(models.Model):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True, related_name='employee')

    def __str__(self):
        return "<Employee: {} {}>".format(self.first_name, self.last_name)

    def __repr__(self):
        return self.__str__()
