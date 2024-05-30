from datetime import datetime
hoy=datetime.today()
hora=hoy.hour
minuto=hoy.minute
variable=str(hora)+':'+str(minuto)
import flet as ft
import registrovr
import modelo
import peewee as pw
def main(page:ft.Page):
    def cerrar(e:ft.ControlEvent):
        page.window_close()

    def registros(e:ft.ControlEvent):
        contendorRV.content=registrovr.main(page)
        contendorRV.update()
    
    def mostrar_categorias(e:ft.ControlEvent):
        listacategoria=[]
        for c in modelo.Categoria.select().where(modelo.Categoria.tipo==drptipo.value):
            option=ft.dropdown.Option(key=c.id_categoria,text=c.categoria)
            listacategoria.append(option)
        drpcategoria.options=listacategoria
        drpcategoria.update()
    
    def proveedorm(e:ft.ControlEvent):
        if txtid.value.strip()=='':
            drpproveedor.value=None
            dialogo.title=ft.Text("ERROR: Ingresa ID")
            dialogo.open=True
            page.update()
            return
        try:
            m=modelo.Prendas(id_prenda=txtid.value.strip(),id_proveedor=drpproveedor.value)
            m.save()
            dialogo.title=ft.Text("DATOS ACTULIZADOS")
            dialogo.open=True
            page.update()
        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)

    def cantidadm(e:ft.ControlEvent):
        if txtid.value.strip()=='':
            txtcantidad.value=''
            dialogo.title=ft.Text("ERROR: Ingresa ID")
            dialogo.open=True
            page.update()
            return
        try:
            m=modelo.Prendas(id_prenda=txtid.value.strip(),cantidad=txtcantidad.value.strip())
            m.save()
            dialogo.title=ft.Text("DATOS ACTULIZADOS")
            dialogo.open=True
            page.update()
        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)

    def categoriam(e:ft.ControlEvent):
        if txtid.value.strip()=='':
            drpcategoria.value=None
            dialogo.title=ft.Text("ERROR: Ingresa ID")
            dialogo.open=True
            page.update()
            return
        try:
            m=modelo.Prendas(id_prenda=txtid.value.strip(),id_categoria=drpcategoria.value)
            m.save()
            dialogo.title=ft.Text("DATOS ACTULIZADOS")
            dialogo.open=True
            page.update()
        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)

    def tallam(e:ft.ControlEvent):
        if txtid.value.strip()=='':
            txttalla.value=''
            dialogo.title=ft.Text("ERROR: Ingresa ID")
            dialogo.open=True
            page.update()
            return
        try:
            m=modelo.Prendas(id_prenda=txtid.value.strip(),talla=txttalla.value.strip())
            m.save()
            dialogo.title=ft.Text("DATOS ACTULIZADOS")
            dialogo.open=True
            page.update()
        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)

    def colorm(e:ft.ControlEvent):
        if txtid.value.strip()=='':
            txtcolor.value=''
            dialogo.title=ft.Text("ERROR: Ingresa ID")
            dialogo.open=True
            page.update()
            return
        try:
            m=modelo.Prendas(id_prenda=txtid.value.strip(),color=txtcolor.value.strip())
            m.save()
            dialogo.title=ft.Text("DATOS ACTULIZADOS")
            dialogo.open=True
            page.update()
        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)
    
    def fecham(e:ft.ControlEvent):
        if txtid.value.strip()=='':
            txtfecha.value=''
            dialogo.title=ft.Text("ERROR: Ingresa ID")
            dialogo.open=True
            page.update()
            return
        try:
            m=modelo.Prendas(id_prenda=txtid.value.strip(),fecha=txtfecha.value+'-'+variable)
            m.save()
            dialogo.title=ft.Text("DATOS ACTULIZADOS")
            dialogo.open=True
            page.update()
        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)

    page.title='Modificar🔩'
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window_width=830
    page.window_height=800
    page.scroll="always"
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.appbar=ft.AppBar(title=ft.Text('Modificar Campo(s)'),
                            leading=ft.Icon(ft.icons.SETTINGS_SUGGEST),
                            center_title=True,
                            bgcolor=ft.colors.BLUE)
    dialogo=ft.AlertDialog(modal=False)
    page.dialog=dialogo
    
    btnver=ft.ElevatedButton('VER REGISTROS',
                             bgcolor=ft.colors.BLUE,
                             color=ft.colors.WHITE,
                             on_click=registros)
    texto=ft.Text('Busca El Registro A Modificar')
    TXT=ft.Text(width=100)
    btnact=ft.ElevatedButton('Actualizar',
                             icon=ft.icons.CHANGE_CIRCLE_ROUNDED,
                             on_click=registros)
    rowbtntexto=ft.Row([texto,btnver,TXT,btnact])
    texto=ft.Text('Ingresa El ID')
    txtid=ft.TextField(label='ID',width=210)
    rowid=ft.Row([texto,txtid])

    listaproveedor=[]
    proveedores=modelo.Proveedor.select()
    for p in proveedores:
        listaproveedor.append(ft.dropdown.Option(key=p.id_proveedor,text=p.nombre))
    drpproveedor=ft.Dropdown(options=listaproveedor,label='Proveedor')
    btnmodi1=ft.IconButton(icon=ft.icons.CACHED_OUTLINED,on_click=proveedorm)
    rw1=ft.Row([drpproveedor,btnmodi1])
    
    txtcantidad=ft.TextField(label='Cantidad',width=100)
    btnmodi2=ft.IconButton(icon=ft.icons.CACHED_OUTLINED,on_click=cantidadm)
    rw2=ft.Row([txtcantidad,btnmodi2])

    opctipo=[ft.dropdown.Option('Mujer'),
             ft.dropdown.Option('Hombre')]
    drptipo=ft.Dropdown(options=opctipo,label='Tipo',on_change=mostrar_categorias)
    
    drpcategoria=ft.Dropdown(options=None,label='Categoria')
    btnmodi4=ft.IconButton(icon=ft.icons.CACHED_OUTLINED,on_click=categoriam)
    rw4=ft.Row([drpcategoria,btnmodi4])

    txttalla=ft.TextField(label='Talla')
    btnmodi5=ft.IconButton(icon=ft.icons.CACHED_OUTLINED,on_click=tallam)
    rw5=ft.Row([txttalla,btnmodi5])

    txtcolor=ft.TextField(label='Color')
    btnmodi6=ft.IconButton(icon=ft.icons.CACHED_OUTLINED,on_click=colorm)
    rw6=ft.Row([txtcolor,btnmodi6])

    txtfecha=ft.TextField(label='DD/MM/AAAA')
    btnmodi7=ft.IconButton(icon=ft.icons.CACHED_OUTLINED,on_click=fecham)
    rw7=ft.Row([txtfecha,btnmodi7])
    
    contendorRV=ft.Container()

    btnc=ft.ElevatedButton('Cerrar',bgcolor=ft.colors.RED,color='white',icon=ft.icons.CANCEL,on_click=cerrar)
    
    columnaF=ft.Column([rw1,rw2,drptipo,rw4,rw5,rw6,rw7])
    rowCC=ft.Row([columnaF,contendorRV])

    page.add(rowbtntexto,rowid,rowCC,btnc)
    page.update()
if __name__=='__main__':
    ft.app(target=main)