from django.urls import path
from courses.views import (CategoryListCreate, CategoryRetrieveUpdateDestroy, TeacherListCreate, TeacherRetrieveUpdateDestroy,
                          CourseListCreate, CourseRetrieveUpdateDestroy, CommentListCreate, CommentRetrieveUpdateDestroy,
                          TicketListCreate, TicketRetrieveUpdateDestroy, TicketMessageListCreate,
                          TicketMessageRetrieveUpdateDestroy,GroupMemberListCreate, GroupMemberRetrieveUpdateDestroy) 



urlpatterns = [
    path('category-list-create', CategoryListCreate.as_view()),
    path('category-retrieve-update-destroy/<str:pk>', CategoryRetrieveUpdateDestroy.as_view()),
    path('teacher-list-create', TeacherListCreate.as_view()),
    path('teacher-retrieve-update-destroy/<str:pk>', TeacherRetrieveUpdateDestroy.as_view()),
    path('course-list-create', CourseListCreate.as_view()),
    path('course-retrieve-update-destroy/<str:pk>', CourseRetrieveUpdateDestroy.as_view()),
    path('group-member-list-create', GroupMemberListCreate.as_view()),
    path('group-member-retrieve-update-destroy/<str:pk>', GroupMemberRetrieveUpdateDestroy.as_view()),
    path('comment-list-create', CommentListCreate.as_view()),
    path('comment-retrieve-update-destroy/<str:pk>', CommentRetrieveUpdateDestroy.as_view()),
    path('Ticket-list-create', TicketListCreate.as_view()),
    path('ticket-retrieve-update-destroy/<str:pk>', TicketRetrieveUpdateDestroy.as_view()),
    path('ticket-message-list-create', TicketMessageListCreate.as_view()),
    path('ticket-message-retrieve-update-destroy/<str:pk>', TicketMessageRetrieveUpdateDestroy.as_view()),
]