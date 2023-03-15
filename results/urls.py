from django.urls import path
from . import views 

urlpatterns = [
    path('result', views.Result.as_view(), name='Result'),
    path('create-result', views.CreateResult.as_view(), name='Create-Result'),
    path('aa-edit-result/<slug:slug>/', views.EditResult.as_view(), name='Edit-Result'),
    path('view-result', views.view_result_primary, name='Result-Primary'),
    path('result_view/<int:pk>/', views.result_view, name='Result-View'),
    path('PView-Result-Primary/<int:pk>/', views.View_Primary_result, name='View-Result-Primary'),
    path('V-Result-Secondary', views.secondary_result_albums, name= 'Secondary-Results-Albums'),
    path('View-Secondary-Results-Albums/<int:pk>/', views.result_view_secondary, name='View-Secondary-Results-Albums'),
    path('Result-Secondary-Create', views.ResultSecondaryCreate.as_view(), name='Result-Secondary-Create'),
    path('Result-Create-Secondary-Album', views.ResultCreateSecondaryAlbum.as_view(), name='Result-Create-Secondary-Album'),


    
    path('Art-Albums', views.art_home, name='Art'),
    path('Dart_albums_view/<int:pk>/', views.art_albums_view, name='View_albums_Art'),
    path('Art-Create-Albums', views.CreateArtAlbums.as_view(), name='Create-Art-Albums'),
    path('cCreate-Art-Result', views.CreateArtResult.as_view(), name='Create-Art-Result'),
    path('fart_result_full/<int:pk>/', views.art_result_full, name='Art_Result_Full'),
    path('art-edit-result/<slug:slug>/', views.ArtEdit.as_view(), name='Art-Edit-Result'),

    path('commerce', views.commerce, name='Commerce-C'),
    path('Commerce-home', views.commerce_home, name='Commerce'),
    path('c-CreateCommerce-Albums', views.CreateCommerceAlbums.as_view(), name='Create-Commerce-Albums'),
    path('x-CreateCommerce-Result', views.CreateCommerceResult.as_view(), name='Create-Commerce-Result'),
    path('m-commerce_view_albums-m/<int:pk>/', views.commerce_view_albums, name='Commerce_view_albums'),
    path('F-Commerce-Result-Full/<int:pk>/', views.commerce_result_full, name='Commerce-Result-Full'),
    path('e-Edit-Commerce-Results/<slug:slug>/', views.EditCommerceResults.as_view(), name='Edit-Commerce-Results')
]