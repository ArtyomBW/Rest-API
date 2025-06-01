from django.urls import path

from apps.views import hello_world_api_view, category_create_api_view, category_delete_api_view, \
    category_update_api_view, book_create_api_view, book_update_api_view, category_list_api_view, add_api_view, \
    register_api_view

urlpatterns = [
    path('hello', hello_world_api_view),
    path('category/create/', category_create_api_view),
    path('category/delete/<int:pk>', category_delete_api_view),
    path('category/update/<int:pk>', category_update_api_view),
    path('book/create/', book_create_api_view),
    path('book/ubdate/<int:pk>', book_update_api_view),
    path('category/list/', category_list_api_view),
    path('add/nums/', add_api_view),
    path('auth/register/', register_api_view)
]
