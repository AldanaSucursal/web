import flet as ft
import modelo
import peewee as pw
def main(page:ft.Page):
    def guardar_datos(e:ft.ControlEvent):
        if txtempresa.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Ingresa El nombre de la empresa")
            dialogo.open=True
            page.update()
            return
        if txtproducto.value.strip()=='':
            dialogo.title=ft.Text("ERROR: ingresa el producto")
            dialogo.open=True
            page.update()
            return
        if txtdireccion.value.strip()=='':
            dialogo.title=ft.Text("ERROR: ingresa la direccion")
            dialogo.open=True
            page.update()
            return
        if txttelefono.value.strip()=='':
            dialogo.title=ft.Text("ERROR: ingresa numero telefonico")
            dialogo.open=True
            page.update()
            return
        if txtemail.value.strip()=='':
            dialogo.title=ft.Text("ERROR: ingresa un correo")
            dialogo.open=True
            page.update()
            return
        try:
            p=modelo.Proveedor.create(nombre=txtempresa.value.strip(),
                                        producto=txtproducto.value.strip(),
                                        direccion=txtdireccion.value.strip(),
                                        telefono=txttelefono.value.strip(),
                                        email=txtemail.value.strip())
            dialogo.title=ft.Text("DATOS GUARDADOS")
            dialogo.open=True
            page.update()

        except pw.IntegrityError as error:
            print("Error en SQLite: ",error)
    
    dialogo=ft.AlertDialog(modal=False)
    page.dialog=dialogo

    txtproveedor=ft.Text('Proveedor',size=25,weight=ft.FontWeight.BOLD)
    txtagregar=ft.Text('Agregar',size=30,weight=ft.FontWeight.BOLD)

    txtempresa=ft.TextField(label='Empresa',border=ft.InputBorder.UNDERLINE)
    txtproducto=ft.TextField(label='Producto',border=ft.InputBorder.UNDERLINE)
    filaEP=ft.Row([txtempresa,txtproducto])#AÑADIR

    txtdireccion=ft.TextField(label='Direccion',border=ft.InputBorder.UNDERLINE)
    txttelefono=ft.TextField(label='Telefono',border=ft.InputBorder.UNDERLINE)
    filaDT=ft.Row([txtdireccion,txttelefono])#AÑADIR

    txtemail=ft.TextField(label='Email',border=ft.InputBorder.UNDERLINE)
    txt=ft.Text(width=100)
    btnaceptar=ft.ElevatedButton('Aceptar',bgcolor='blue',color='white',on_click=guardar_datos)
    filaETB=ft.Row([txtemail,txt,btnaceptar])#AÑADIR
    
    columnaF=ft.Column([txtproveedor,txtagregar,filaEP,filaDT,filaETB])
    return columnaF
if __name__=='__main__':
    ft.app(target=main)