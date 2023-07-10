from django.urls import re_path
from django.urls import path
from .views import custom_login_bsm, home_bsm, download_equipment_excel_users, check_history, get_locations, download_equipment_excel_changes, reset_password, change_password, custom_logout, register, custom_login, upload_file, edit_equipment, equipment_search, home, download_equipment_excel, bsm_equipment_search, download_equipment_excel_history, equipment_changes_view

urlpatterns = [
    path('', home, name='home'),
    path('home_bsm/', home_bsm, name='home_bsm'),
    path('equipment_search/', equipment_search, name='equipment_search'),
    path('bsm_equipment_search/', bsm_equipment_search, name='bsm_equipment_search'),
    path('upload/', upload_file, name='upload_file'),
    path('download-equipment-excel/', download_equipment_excel, name='download_equipment_excel'),
    path('download-equipment-excel_history/', download_equipment_excel_history, name='download_equipment_excel_history'),
    path('download-equipment-excel_changes/', download_equipment_excel_changes, name='download_equipment_excel_changes'),
    path('download-equipment-excel_users/', download_equipment_excel_users, name='download_equipment_excel_users'),
    path('edit-item/<int:equipment_id>/', edit_equipment, name='edit_equipment'),
    re_path(r'^equipment/changes/(?P<equipment_id>[0-9]*)/$', equipment_changes_view, name='equipment_changes'),
    path('check_history/', check_history, name='check_history'),
    path('login/', custom_login, name='custom_login'),
    path('bsm_equipment_search/register/', register, name='register'),
    path('get_locations/', get_locations, name='get_locations'),
    path('logout/', custom_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('login/reset_password/', reset_password, name='reset_password'),
    path('login_bsm/', custom_login_bsm, name='custom_login_bsm'),
    path('login_bsm/reset_password/', reset_password, name='reset_password_bsm'),
]