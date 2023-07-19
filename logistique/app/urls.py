from django.urls import path
from app.views import admin, employes, categories, users, products, transferts
#from logistique.app.views import transferts

urlpatterns = [
    path('', admin.index, name='home'),
    
    #------------------------------------Employe Urls------------------------------------
    path('employes/', employes.index, name="employes"),
    path('employes/add', employes.add, name="employes_add"),
    path('employes/store', employes.store, name="employes_store"),
    path('employes/edit/<int:id>', employes.edit, name="employes_edit"),
    path('employes/update/<int:id>', employes.update, name="employes_update"),
    path('employes/delete/<int:id>', employes.delete, name="employes_delete"),
    
    #--------------------------------------Categories--------------------------------------
    path('categories/', categories.index, name="categories"),
    path('categories/add', categories.add, name="categories_add"),
    path('categories/store', categories.store, name="categories_store"),
    path('categories/edit/<int:id>', categories.edit, name="categories_edit"),
    path('categories/update/<int:id>', categories.update, name="categories_update"),
    path('categories/delete/<int:id>', categories.delete, name="categories_delete"),

    #----------------------------------------Users----------------------------------------
    path('users/', users.index, name='users_index'),
    path('login/', users.user_login, name='users_login'),
    path('register/', users.register, name='users_register'),
    path('users/store', users.store, name='users_store'),
    path('logout/', users.user_logout, name='logout'),

    #---------------------------------------Products---------------------------------------
    path('products/', products.index, name='products'),
    path('products/create', products.create, name='products_create'),
    path('products/store', products.store, name='products_store'),
    path('products/edit/<int:id>', products.edit, name='products_edit'),
    path('products/delete/<int:id>', products.delete, name='products_delete'),

    #---------------------------------------Transfert---------------------------------------
    path('transferts/', transferts.index, name='transferts'),
    path('transferts/create', transferts.create, name='transferts_create'),
    path('transferts/getProducts', transferts.getProducts, name='getProducts'),
    path('transferts/store', transferts.store, name='transferts_store'),
]