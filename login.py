import flet as ft
import menu
from flet_multi_page import subPage
def main(page:ft.Page):
    def validar(e:ft.ControlEvent):
        if txtcorreo.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Ingresa Tu CORREO")
            dialogo.open=True
            page.update()
            return
        if txtpassword.value.strip()=='':
            dialogo.title=ft.Text("ERROR: Ingresa Contraseña")
            dialogo.open=True
            page.update()
            return
        if txtcorreo.value.strip() !='sucursal_aldana@almacen.com' and txtpassword.value.strip() != 'aldana108':
            dialogo.title=ft.Text("ERROR: Usuario NO Admitido")
            dialogo.open=True
            page.update()
            return
        else:
            # c.content=menu.main(page)
            page.window_close()
            c=subPage(target=menu.main)
            #c.update()

    #Cuadro de Dialogo
    dialogo=ft.AlertDialog(modal=False)
    page.dialog=dialogo

    page.title='Bienvenido'
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.theme_mode=ft.ThemeMode.LIGHT
    page.appbar=ft.AppBar(title=ft.Text('Sistema Aldana',font_family="Times New Roman",size=30),
                            leading=ft.Icon(ft.icons.ADD_CIRCLE),
                            center_title=True,
                            bgcolor=ft.colors.BLUE,
                            color="White")

    txtcorreo=ft.TextField(hint_text='Ingresa tu Correo',icon=ft.icons.EMAIL,width=350,border='underline')
    txtpassword=ft.TextField(hint_text='Ingresa Contraseña',icon=ft.icons.LOCK,width=350,border='underline')
    btn=ft.ElevatedButton('Aceptar',bgcolor='blue',color='white',width=350,on_click=validar)

    c=ft.Container(border_radius=5,
                   bgcolor=ft.colors.WHITE,
                    content=ft.Column([txtcorreo,txtpassword,btn]))

    page.add(c)
    page.update()
if __name__=='__main__':
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)