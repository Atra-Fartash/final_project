from django.contrib import admin
from courses.models import Category, Teacher, Course,  Comment, Ticket, TicketMessage, GroupMembers, Enrollment, CoursTierPrice



class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'course_type', 'price']
    search_fields = ['title']
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(TicketMessage)
admin.site.register(GroupMembers)
admin.site.register(Enrollment)
admin.site.register(CoursTierPrice)