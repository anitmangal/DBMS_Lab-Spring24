from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
# Register your models here.

from .forms import UserCreationForm, ParticipantCreationForm, StudentCreationForm, OrganiserCreationForm, TimeSlotCreationForm, VenueCreationForm, EventCreationForm
from .models import useracc, Student, Organiser, Participant, TimeSlot, Venue, Event
    
class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
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

class TimeSlotAdmin(admin.ModelAdmin):
    model = TimeSlot
    add_form = TimeSlotCreationForm
    list_display = ['time_slot_id', 'date', 'start_time', 'end_time']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('date', 'start_time', 'end_time')}
        ),
    )

class VenueAdmin(admin.ModelAdmin):
    model = Venue
    add_form = VenueCreationForm
    list_display = ['venue_name', 'building', 'audio_visual', 'computer_terminals', 'capacity']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('venue_name', 'building', 'audio_visual', 'computer_terminals', 'capacity')}
        ),
    )

class EventAdmin(admin.ModelAdmin):
    model = Event
    add_form = EventCreationForm
    list_display = ['event_id', 'event_name', 'event_type', 'event_description', 'time_slot_id', 'venue_name']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('event_name', 'event_type', 'event_description', 'time_slot_id', 'venue_name')}
        ),
    )

admin.site.unregister(Group)

admin.site.register(useracc, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Organiser, OrganiserAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)

admin.site.site_header = 'Fest Management System'