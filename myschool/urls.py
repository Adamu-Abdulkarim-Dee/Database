from django.urls import path
from . import views 

urlpatterns =[
    path('', views.dashboard, name='Dashboard'),
    path('home', views.home, name='Home'),
    path('sss_primary_school', views.primary, name='Primary'),
    path('bbb_secondary_school', views.secondary, name='Secondary'),

    # A url that allow me to see existing albums
    path('zzz_primary_albums/<int:pk>/', views.primary_albums_views, name='Primary-Albums'),
    path('ccc_secondary_albums/<int:pk>/', views.secondary_albums_views, name='Secondary-Albums'),

    # A url that allow me to view student informations
    path('ppp_student_information_primary/<int:pk>/', views.view_student_information_primary, name='Primary-Student-Informations'),
    
    path('qqq_secondary_informations/<int:pk>/', views.view_Student_information_secondary, name='Secondary-Informations'),


    # A url that allow me to create Albums
    path('create_primary_albums', views.Primary_album_form.as_view(), name='Create-Primary-Albums'),

    path('www_create_secondary_albums', views.Secondary_album_form.as_view(), name='Create-Secondary-Albums'),

    # A url that allow me to create students informations
    path('primary', views.CreatePrimaryStudent.as_view(), name='Create-Primary-Student'),

    path('secondary', views.CreateSecondaryStudent.as_view(), name='Create-Secondary-Student'),
    path('m_edit-primary/<slug:slug>/', views.XEditPrimary.as_view(), name='Edit-Primary-Student'),
    path('edit-secondary/<slug:slug>/', views.EditSecondary.as_view(), name='Edit-Secondary-Student'),
    path('n_delete/<slug:slug>/', views.BDeletePrimary.as_view(), name='Delete-primary'),
    path('delete/<slug:slug>/', views.DeleteSecondary.as_view(), name='Delete-secondary'),

    path('profile/<slug:slug>/', views.profile, name='Profile'),

]