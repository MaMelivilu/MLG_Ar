from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "Nombre: {0} - {1}"
        return txt.format(self.nombre,self.categoria_id)



class Producto(models.Model):
    sku = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=150,null=False)
    stock = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True,blank=True)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to="imagenesProductos")

    def __str__(self):
        txt = "N° {0} - Nombre: {1} - Stock: {2} - fecha: {3}"  
        return txt.format(self.sku,self.nombre,self.stock,self.fecha_ingreso)
    
class Usuario(models.Model):
        nombre = models.CharField(max_length=100, null=False)
        apellido = models.CharField(max_length=100, null=False)
        rut = models.CharField(max_length=12,primary_key=True)
        correo = models.CharField(max_length=100, null=False)
        contraseña = models.CharField(max_length=100, null=False)


class Suscripcion(models.Model):
     rut = models.CharField(max_length=12,primary_key=True)
     nombre = models.CharField(max_length=100, null=False)
     apellido = models.CharField(max_length=100, null=False)
     correo = models.CharField(max_length=100, null=False)


class Juegos(models.Model):
     juegos_id = models.IntegerField(primary_key=True)
     nombre = models.CharField(max_length=100, null=False)
     img_url = models.ImageField(upload_to="imgJuegos")

class Streamers(models.Model):
     Stream_id = models.IntegerField(primary_key=True)
     nombre = models.CharField(max_length=100, null=False)
     img_url = models.ImageField(upload_to="imgStream")
     icon = models.ImageField(upload_to="icon")


class Chat(models.Model):
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


