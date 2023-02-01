from django.urls import path
from .views import new_product, product_detail, product_update, product_delete, new_comment, delete_comment

app_name = 'products' # {% url 'products:new' %}
urlpatterns = [
    path("new", new_product, name='new'),
    path("<int:product_id>/detail", product_detail, name='detail'),
    path("<int:product_id>/update", product_update, name='update'),
    path("<int:product_id>/delete", product_delete, name='delete'),
    path("<int:product_id>/comment/new", new_comment, name='comment_new'),
    path("<int:product_id>/comment/<int:comment_id>/delete", delete_comment, name='comment_delete'),
]