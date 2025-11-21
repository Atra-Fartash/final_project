from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import (CategoryViewSet, TeacherViewSet,CourseViewSet, CommentListCreate, CommentRetrieveUpdateDestroy,
                          TicketViewSet, TicketMessageListCreate, TicketMessageRetrieveUpdateDestroy, GroupMemberViewSet) 



router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('teachers', TeacherViewSet)
router.register('courses', CourseViewSet)
router.register('tickets', TicketViewSet)
router.register('group_members', GroupMemberViewSet)

urlpatterns = [
    path('comment-list-create', CommentListCreate.as_view()),
    path('comment-retrieve-update-destroy/<str:pk>', CommentRetrieveUpdateDestroy.as_view()),
    path('ticket-message-list-create', TicketMessageListCreate.as_view()),
    path('ticket-message-retrieve-update-destroy/<str:pk>', TicketMessageRetrieveUpdateDestroy.as_view()),
    path("", include(router.urls)),
]