from django.contrib import admin
from django.urls import path
from library_management import views

urlpatterns = [
    path("",views.index,name='home'),

    path("add_book",views.addbook,name='add book'),
    path("edit_book<int:Book_id>",views.editbook,name='edit book'),
    path("do_edit_book<int:Book_id>",views.do_edit_book,name='do edit book'),
    path("delete_book<int:Book_id>",views.deletebook,name='delete book'),
    path("search_book",views.searchbook,name='search book'),

    path("add_member",views.addmember,name='add member'),
    path("search_member",views.searchmember,name='search member'),
    path("edit_member<int:Member_id>",views.editmember,name='edit member'),
    path("do_edit_member<int:Member_id>",views.do_edit_member,name='do edit member'),
    path("delete_member<int:Member_id>",views.deletemember,name='delete member'),

    path("issue_book",views.issuebook,name='issue book'),
    path("issue_details",views.issuedetails,name='issue details'),


    path("return_book",views.returnbook,name='return book'),
    path("return_details",views.returndetails,name='return details'),

     

]
