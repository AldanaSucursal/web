import peewee as pw
bd_inventario=pw.SqliteDatabase('sucursal.sqlite3')

class Categoria(pw.Model):
    id_categoria=pw.IntegerField(primary_key=True)
    tipo=pw.TextField()
    categoria=pw.TextField()
    class Meta:
        database=bd_inventario

class Proveedor(pw.Model):
    id_proveedor=pw.IntegerField(primary_key=True)
    nombre=pw.TextField()
    producto=pw.TextField()
    direccion=pw.TextField()
    telefono=pw.TextField()
    email=pw.TextField()
    class Meta:
        database=bd_inventario

class Prendas(pw.Model):
    id_prenda=pw.IntegerField(primary_key=True)
    id_proveedor=pw.ForeignKeyField(field='id_proveedor',column_name='id_proveedor',model=Proveedor)
    cantidad=pw.IntegerField()
    id_categoria=pw.ForeignKeyField(field='id_categoria',column_name='id_categoria',model=Categoria)
    talla=pw.TextField()
    color=pw.TextField()
    fecha=pw.TextField()
    class Meta:
        database=bd_inventario

class Sucursal(pw.Model):
    id_sucursal=pw.TextField(primary_key=True)
    no_sucursal=pw.TextField()
    direccion=pw.TextField()
    telefono=pw.TextField()
    email=pw.TextField()
    password=pw.TextField()
    class Meta:
        database=bd_inventario