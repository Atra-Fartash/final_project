from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from courses.serializers import CategorySerializer, TeacherSerializer, CourseSerializer, CommentSerializer, TicketSerializer, TicketMessageSerializer, GroupMemberSerializer
from courses.models import Category, Teacher, Course, Comment, Ticket, TicketMessage, GroupMembers
from rest_framework import permissions



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_permissions(self):

        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        
        return [permissions.IsAuthenticated()]
    

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_permissions(self):

        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        
        return [permissions.IsAuthenticated()]
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['category']
    ordering_fields = ['price', 'start_date', 'duration']

    def get_permissions(self):

        if self.request.method == 'POST':
           return [permissions.IsAdminUser()]
        
        if self.request.method == ['PATCH', 'PUT', 'DELETE']:
           return [permissions.IsAdminUser()]
        
        return [permissions.IsAuthenticated()]


class GroupMemberViewSet(viewsets.ModelViewSet):
    queryset =  GroupMembers.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(user=user)
    

class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at']


class TicketMessageListCreate(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketMessageSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
           return TicketMessage.objects.all()
        return TicketMessage.objects.filter(sender=user)


class TicketMessageRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TicketMessage.objects.all()
    serializer_class = TicketMessageSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(user=user)