from courses.models import Category, Teacher, Course, Comment, Ticket, TicketMessage, GroupMembers, CoursTierPrice, Enrollment
from rest_framework.serializers import ModelSerializer



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'picture', 'linkedin']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'course_type', 'price', 'description', 'category',
                  'start_date', 'duration', 'picture', 'files', 'register_deadline',
                  'class_link', 'access_expiration', 'offline_video']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'date', 'text', 'course']


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user', 'title', 'description', 'status', 'section', 'created_at']


class TicketMessageSerializer(ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = ['ticket', 'sender', 'message', 'created_at']


class GroupMemberSerializer(ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = ['course', 'buyer', 'name', 'email', 'phone_number', 'created_at']


class CourseTierPriceSerializer(ModelSerializer):
    class Meta:
        model = CoursTierPrice
        fields = ['min_members', 'max_members', 'price_per_person']


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'date_joined']