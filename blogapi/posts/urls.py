from django.urls import path

#from .views import PostList, PostDetail, UserList, UserDetail
from .views import PostList, PostDetail
from .views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')

urlpatterns = [
    #path('users/', UserList.as_view()),
    #path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
] + router.urls