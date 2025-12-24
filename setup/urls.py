from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers, permissions
from students.views import StudentViewSet
from courses.views import CourseViewSet
from books.views import BookViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title='Django REST API - Books, Courses & Students',
        default_version='v1',
        description='REST API for managing books, courses and students',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()  # create automatic routes
router.register(r'students', StudentViewSet, basename='students')   #  This shows which routes are needed
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'books', BookViewSet,basename='book')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
    path('',include(router.urls)),
]
