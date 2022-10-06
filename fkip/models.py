from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=50)
    nama = models.CharField(max_length=40)
    tanggal_lahir = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/')
    email = models.CharField(max_length=40)
    fakultas = models.CharField(max_length=40)
    prodi = models.CharField(max_length=40)
    alamat = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.nama

class Staff(models.Model):
    NIP = models.CharField(max_length=50)
    nama = models.CharField(max_length=40)
    tanggal_lahir = models.CharField(max_length=20)
    photo = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    unit = models.CharField(max_length=40)
    alamat = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.nama

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=50)
    nama = models.CharField(max_length=40)
    tanggal_lahir = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/')
    email = models.CharField(max_length=40)
    fakultas = models.CharField(max_length=40)
    prodi = models.CharField(max_length=40,null=True)
    
    def __str__(self):
        return self.nama