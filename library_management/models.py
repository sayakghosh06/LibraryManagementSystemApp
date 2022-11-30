from django.db import models

# Create your models here.


    
class Bookadd(models.Model):        
    Book_Name = models.CharField(max_length=122)
    Author_Name=models.CharField(max_length=122)
    Price= models.IntegerField()
    Copies= models.IntegerField(default=1)
    Remaining_Copies= models.IntegerField(null=True)       
    Book_id=models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.Book_Name 


class Memberadd(models.Model):        
    Member_Name = models.CharField(max_length=122)
    Member_Address=models.CharField(max_length=122)
    Phone= models.IntegerField()    
    Member_id=models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.Member_Name


class Issuebook(models.Model):   
    Issue_id=models.IntegerField(primary_key=True)
    Issuedate = models.DateField() 
    Member=models.ForeignKey(Memberadd, on_delete=models.CASCADE)
    Book=models.ForeignKey(Bookadd, on_delete=models.CASCADE)
    Copies=models.IntegerField()
     
    def __str__(self):
        return self.Book

class Returnbook(models.Model):   
    Return_id=models.IntegerField(primary_key=True)
    Returndate = models.DateField() 
    Member=models.ForeignKey(Memberadd, on_delete=models.CASCADE)
    Book=models.ForeignKey(Bookadd, on_delete=models.CASCADE)
    Copies=models.IntegerField()
     
    def __str__(self):
        return self.Book