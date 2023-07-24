from django.urls import path
from django.urls import path
# from .admin_views import (AdminDashboardView, CreateStaffView,
#                           EditStaffView, DeleteStaffView)
from .superuser_views import (SuperUserDashboardView,
                                CreateAdminView,
                                EditAdminView,
                                DeleteAdminView)

from .admin_views import (AdminDashboardView, 
                          CreateStaffView, 
                          EditStaffView, 
                          DeleteStaffView)

from .staff_views import (StaffDashboardView, 
                          RegisterParentView, )

from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('superuser_dashboard/', SuperUserDashboardView.as_view(), name='superuser_dashboard'),
    path('superuser_dashboard/create_admin/', CreateAdminView.as_view(), name='create_admin'),
    path('superuser_dashboard/edit_admin/<int:user_id>/', EditAdminView.as_view(), name='edit_admin'),
    path('superuser_dashboard/delete_admin/<int:user_id>/', DeleteAdminView.as_view(), name='delete_admin'),

    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin_dashboard/create_staff/', CreateStaffView.as_view(), name='create_staff'),
    path('admin_dashboard/edit_staff/<int:user_id>/', EditStaffView.as_view(), name='edit_staff'),
    path('admin_dashboard/delete_staff/<int:user_id>/', DeleteStaffView.as_view(), name='delete_staff'),


    path('staff_dashboard/', StaffDashboardView.as_view(), name='staff_dashboard'),
    path('staff_dashboard/register_parent', RegisterParentView.as_view(), name='register_parent'),



    # ... your other url patterns
]
