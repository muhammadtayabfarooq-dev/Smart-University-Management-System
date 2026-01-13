from django.contrib import admin

from .models import Course, CourseOffering, Enrollment, Term


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'credits', 'department')
    search_fields = ('code', 'title', 'department')


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')


@admin.register(CourseOffering)
class CourseOfferingAdmin(admin.ModelAdmin):
    list_display = ('course', 'term', 'faculty', 'capacity')
    list_filter = ('term', 'course')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'offering', 'status', 'grade', 'enrolled_at')
    list_filter = ('status', 'offering')
