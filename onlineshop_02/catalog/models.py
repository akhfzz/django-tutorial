from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    nama = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('nama',)
    
    def __str__(self):
        return f"{self.nama} pada tabel kategori berhasil ditambahkan"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='produk')
    nama = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(max_length=255, blank=True, upload_to='produk/%Y/%m/%d')
    deskripsi = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nama',)
    
    def __str__(self):
        return f"{self.nama} pada tabel produk ditambahkan"
