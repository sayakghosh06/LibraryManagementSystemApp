from django.shortcuts import render,HttpResponse,redirect
from library_management.models import *
from datetime import datetime
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
    
    Books= Bookadd.objects.all()

    return render(request,'index.html',{'Books':Books})   
    

def addbook(request):
    if request.method == "POST":        
        Book_Name = request.POST.get('Book_Name')
        Author_Name= request.POST.get('author')
        Price= request.POST.get('price')
        Copies= request.POST.get('Copies')
        Remaining_Copies= request.POST.get('Copies')
        addbook=Bookadd(Book_Name=Book_Name,Author_Name=Author_Name,Price=Price,Copies=Copies,Remaining_Copies=Remaining_Copies)
        addbook.save()
        messages.success(request,"Book Added Successfully")
        return redirect("add book")
      
     
    return render(request,'addbook.html')   

def editbook(request,Book_id):

    b=Bookadd.objects.get(pk=Book_id)
    return render(request,'editbook.html',{'b':b})   
    return redirect("home")

def do_edit_book(request,Book_id):
        Book_Name = request.POST.get('Book_Name')
        Author_Name= request.POST.get('author')
        Price= request.POST.get('price')
        Copies= request.POST.get('Copies')

        book_copy=Bookadd.objects.get(pk=Book_id)

        book=Bookadd.objects.get(pk=Book_id)
        book.Book_Name=Book_Name
        book.Author_Name=Author_Name
        book.Price=Price
        book.Copies=Copies
        book.Remaining_Copies= (int(book.Copies)-int(book_copy.Copies))+int(book.Remaining_Copies) 
        book.save()
        
        return redirect("search book")
        


def deletebook(request,Book_id):
    b=Bookadd.objects.get(pk=Book_id)
    b.delete()
    return redirect("home")

def searchbook(request):

        Books= Bookadd.objects.all()

        if request.method=='GET':
         st=request.GET.get("searchname")
         if st!=None:
              Books = Bookadd.objects.filter(Book_Name__icontains = st) 

        return render(request,'searchbook.html',{'Books':Books})  

def addmember(request):

    if request.method == "POST":        
        Member_Name= request.POST.get('Member_Name')
        Member_Address= request.POST.get('Member_Address')
        Phone= request.POST.get('Phone')
        
        addmember=Memberadd(Member_Name=Member_Name,Member_Address=Member_Address,Phone=Phone)
        addmember.save()
        messages.success(request,"Member Added Successfully")
        return redirect("add member")

    return render(request,'addmember.html')

def searchmember(request):
    Members=Memberadd.objects.all()

    if request.method=='GET':
         st=request.GET.get("searchname")
         if st!=None:
              Members = Memberadd.objects.filter(Member_Name__icontains = st) 

    return render(request,'searchmember.html',{'Members':Members})


def editmember(request,Member_id):

    m=Memberadd.objects.get(pk=Member_id)
    return render(request,'editmember.html',{'m':m})   
    return redirect("home")

def do_edit_member(request,Member_id):
        Member_Name = request.POST.get('Member_Name')
        Member_Address= request.POST.get('Member_Address')
        Phone= request.POST.get('Phone')
       

        Member=Memberadd.objects.get(pk=Member_id)
        Member.Member_Name=Member_Name
        Member.Member_Address=Member_Address
        Member.Phone=Phone
        Member.save()
        return redirect("search member")

def deletemember(request,Member_id):
    m=Memberadd.objects.get(pk=Member_id)
    m.delete()
    
    return redirect("search member")

def issuebook(request):
    if request.method == "POST":           
           Member= request.POST.get('Member_id')
           Book= request.POST.get('Book_id')
           Copies= int(request.POST.get('Copies'))
           issuebook=Issuebook(Member_id=Member,Book_id=Book,Copies=Copies,Issuedate=datetime.now())
           book=Bookadd.objects.get(pk=Book)
           if issuebook.Copies<=book.Remaining_Copies:   
                  
                  issuebook.save()
                  messages.success(request,"Book Has Been Issued Successfully")
                  
                  book.Remaining_Copies= int(book.Remaining_Copies)-int(issuebook.Copies)
                  book.save()             

           else:
         
              messages.success(request,"book is not available")
    
    
    return render(request,'issuebook.html')  
def issuedetails(request):
    issues=Issuebook.objects.all()
    if request.method=='GET':
         st=request.GET.get("searchname")
         if st!=None:
              issues = Issuebook.objects.filter(Q(Member__Member_Name__icontains = st) | Q(Book__Book_Name__icontains = st) )
              
        


    return render(request,'issuedetails.html',{'issues':issues})
    



def returnbook(request):
    if request.method == "POST":        
        Member= request.POST.get('Member_id')
        Book= request.POST.get('Book_id')
        Copies= request.POST.get('Copies')
        
        
        returnbook=Returnbook(Member_id=Member,Book_id=Book,Copies=Copies,Returndate=datetime.now())
        book=Bookadd.objects.get(pk=Book)
      
        
        
        if int(returnbook.Copies)+int(book.Remaining_Copies)<=book.Copies :   
       
            returnbook.save()
            messages.success(request,"Book Has Been Returned Successfully")

            book.Remaining_Copies= int(book.Remaining_Copies)+int(returnbook.Copies)
            book.save() 

        else:
             messages.success(request,"wrong number of copies")
             

    return render(request,'returnbook.html')  




def returndetails(request):
    returns=Returnbook.objects.all()

    if request.method=='GET':
         st=request.GET.get("searchname")
         if st!=None:
              returns = Returnbook.objects.filter(Q(Member__Member_Name__icontains = st) | Q(Book__Book_Name__icontains = st) )





    return render(request,'returndetails.html',{'returns':returns})