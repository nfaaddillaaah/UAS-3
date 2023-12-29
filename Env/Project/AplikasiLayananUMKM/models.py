from django.db import models
#Class dan Objek
class BaseMenu(models.Model):
    nama_menu = models.CharField(max_length=255)
    deskripsi = models.TextField()
    _harga = models.DecimalField(max_digits=10, decimal_places=2)

    gambar = models.ImageField(upload_to='img/', null=True)


    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nama_menu}"

class Roti(BaseMenu):
    pass
class AishTea(BaseMenu):
    pass

class Wang(BaseMenu):
    pass

class Saguku(BaseMenu):
    @property
    def harga(self):
        return self._harga

    def save(self, *args, **kwargs):
        if self._harga < 0:
            self._harga = self.__class__.objects.get(pk=self.pk)._harga
        super().save(*args, **kwargs)

class Esteh(BaseMenu):
    @property
    def save(self, *args, **kwargs):
        if self._harga < 10.000:
            self._harga = self.__class__.objects.get(pk=self.pk)._harga
        super().save(*args, **kwargs)
class AyamGeprek(BaseMenu):
    def __str__(self):
        return f"AyamGeprek: {self.nama_menu}, Harga: {self.harga}"
 
 ######################################## NO. 2 ############################################
    
class Pelanggan:
    nama_pelanggan = models.CharField(max_length=100)
    pesanan = models.CharField(max_length=300)

 ######################################## NO. 3 ############################################

class NasiKuning(BaseMenu):
  def harga(self):
        return f"NasiKuning: {self.nama_menu}, Harga: {self.harga}"
  
  def save(self, *args, **kwargs):
        if self._harga :
            self._harga = self.__class__.objects.get(pk=self.pk)._harga
        super().save(*args, **kwargs)

