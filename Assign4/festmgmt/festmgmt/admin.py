from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import UserCreationForm, ParticipantCreationForm, StudentCreationForm, OrganiserCreationForm
from .models import useracc, Student, Organiser, Participant

class CustomUserAdmin(UserAdmin):
    model = useracc
    add_form = UserCreationForm
    list_display = ['user_id', 'username', 'name', 'email', 'phone']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'username', 'password', 'role')}
        ),
    )

class StudentAdmin(UserAdmin):
    model = Student
    add_form = StudentCreationForm
    list_display = ['username', 'name', 'email', 'phone', 'roll_number', 'dept', 'year']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'username', 'password', 'roll_number', 'dept', 'year')}
        ),
    )

class OrganiserAdmin(UserAdmin):
    model = Organiser
    add_form = OrganiserCreationForm
    list_display = ['username', 'name', 'email', 'phone', 'position_of_responsibility']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'username', 'password', 'position_of_responsibility')}
        ),
    )

class ParticipantAdmin(UserAdmin):
    model = Participant
    add_form = ParticipantCreationForm
    list_display = ['username', 'name', 'email', 'phone', 'food', 'accomodation_building', 'accomodation_room']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'username', 'password', 'food', 'accomodation_building', 'accomodation_room')}
        ),
    )

admin.site.register(useracc, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Organiser, OrganiserAdmin)
admin.site.register(Participant, ParticipantAdmin)
