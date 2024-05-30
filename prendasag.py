from datetime import datetime
hoy=datetime.today()
hora=hoy.hour
minuto=hoy.minute
variable=str(hora)+':'+str(minuto)
from flet_multi_page import subPage
import modificar
import flet as ft
import modelo
import peewee as pw
def main(page:ft.Page):

    def modi(e:ft.ControlEvent):
        a=subPage(target=modificar.main)
        a.start()

    def mostrar_categorias(e:ft.ControlEvent):
        listacategoria=[]
        for c in modelo.Categoria.select().where(modelo.Categoria.tipo==drptipo.value):
            option=ft.dropdown.Option(key=c.id_categoria,text=c.categoria)
            listacategoria.append(option)
        drpcategoria.options=listacategoria
        drpcategoria.update()
    
    def guardar_datos(e:ft.ControlEvent):
        if drpproveedor.value is None:
            dialogo.title=ft.Text("ERROR: Seleccion un Proveedor")
            dialogo.open=True
            page.update()
            return
        if txtcantidad.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Ingresa la Cantidad")
            dialogo.open=True
            page.update()
            return
        if drptipo.value is None:
            dialogo.title=ft.Text("ERROR: Seleccion el tipo")
            dialogo.open=True
            page.update()
            return
        if drpcategoria.value is None:
            dialogo.title=ft.Text("ERROR: Selecciona la Categoria del producto")
            dialogo.open=True
            page.update()
            return
        if txttalla.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Selecciona la Talla")
            dialogo.open=True
            page.update()
            return
        if txtcolor.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Selecciona el Color")
            dialogo.open=True
            page.update()
            return
        if txtfecha.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Falta La Fecha")
            dialogo.open=True
            page.update()
            return
        try:
            prendas=modelo.Prendas.create(id_proveedor=drpproveedor.value,
                                            cantidad=txtcantidad.value.strip(),
                                            id_categoria=drpcategoria.value,
                                            talla=txttalla.value.strip(),
                                            color=txtcolor.value.strip(),
                                            fecha=txtfecha.value.strip()+'-'+variable)
            dialogo.title=ft.Text("DATOS GUARDADOS")
            dialogo.open=True
            page.update()

        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)

    dialogo=ft.AlertDialog(modal=False)
    page.dialog=dialogo

    txtprendas=ft.Text('Prendas',size=25,weight=ft.FontWeight.BOLD)
    btnmodificar=ft.ElevatedButton('Modificar',bgcolor='Blue',color='White',on_click=modi)
    filatxtbtnam=ft.Row([txtprendas,btnmodificar])#Añadir
    
    txt1=ft.Text('Agregar',size=35,weight=ft.FontWeight.W_900)#AÑADIR

    listaproveedor=[]
    proveedores=modelo.Proveedor.select()
    for p in proveedores:
        listaproveedor.append(ft.dropdown.Option(key=p.id_proveedor,text=p.nombre))
    drpproveedor=ft.Dropdown(options=listaproveedor,label='Proveedor')
    txtcantidad=ft.TextField(label='Cantidad',width=100,border=ft.InputBorder.UNDERLINE)
    filaPC=ft.Row([drpproveedor,txtcantidad])#AÑADIR

    opctipo=[ft.dropdown.Option('Mujer'),
             ft.dropdown.Option('Hombre')]
    drptipo=ft.Dropdown(options=opctipo,label='Tipo',on_change=mostrar_categorias)
    drpcategoria=ft.Dropdown(options=None,label='Categoria')
    filaCT=ft.Row([drptipo,drpcategoria])#AÑADIR

    txttalla=ft.TextField(label='Talla',border=ft.InputBorder.UNDERLINE)
    txtcolor=ft.TextField(label='Color',border=ft.InputBorder.UNDERLINE)
    filaTC=ft.Row([txttalla,txtcolor])#Añadir
    btnaceptar=ft.ElevatedButton('Aceptar',icon=ft.icons.ARROW_BACK,on_click=guardar_datos)
    txtvacio=ft.Text(width=150)
    txtfecha=ft.TextField(label='DD/MM/AAAA')
    filaVA=ft.Row([txtfecha,txtvacio,btnaceptar])#Añadir


    columnaF=ft.Column([filatxtbtnam,
                        txt1,
                        filaPC,
                        filaCT,
                        filaTC,
                        filaVA])
    return columnaF
    #page.add(columnaF)
if __name__=='__main__':
    ft.app(target=main)