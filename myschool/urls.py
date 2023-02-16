from django.urls import path
from . import views 

urlpatterns =[
    path('', views.dashboard, name='Dashboard'),
    path('login', views.login, name='login'),
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

    path('about', views.about, name='About'),

    path('terms-and-conditions-privacy', views.terms, name='Terms'),

    path('contact', views.Contact.as_view(), name='Contact'),


    path('m_edit-primary/<slug:slug>/', views.XEditPrimary.as_view(), name='Edit-Primary-Student'),
    path('edit-secondary/<slug:slug>/', views.EditSecondary.as_view(), name='Edit-Secondary-Student'),

    path('n_delete/<slug:slug>/', views.BDeletePrimary.as_view(), name='Delete-primary'),

    path('delete/<slug:slug>/', views.DeleteSecondary.as_view(), name='Delete-secondary'),

    path('BoardEdit/<slug:slug>/', views.Board.as_view(), name='Board'),

    path('profile/<slug:slug>/', views.profile, name='Profile'),

    path('register', views.sign_up, name='Register'),

    path('result', views.Result.as_view(), name='Result'),

    path('create-result', views.CreateResult.as_view(), name='Create-Result'),

    path('aa-edit-result/<slug:slug>/', views.EditResult.as_view(), name='Edit-Result'),

    path('view-result', views.view_result_primary, name='Result-Primary'),

    path('result_view/<int:pk>/', views.result_view, name='Result-View'),

    path('PView-Result-Primary/<int:pk>/', views.View_Primary_result, name='View-Result-Primary'),

    path('Delete-primary-Result/<slug:slug>/', views.DeletePrimaryResult.as_view(), name='Delete-Primary-Result'),


    path('payments', views.handle_payment, name='Pay'),

]