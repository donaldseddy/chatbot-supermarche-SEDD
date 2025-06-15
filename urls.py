from django.urls import path, include

urlpatterns = [
    path("admin/", include("django.contrib.admin.urls")),
    path('api/chatbot/', include('chatbot.urls')),
    path("api/users/", include("users.urls")),
]
