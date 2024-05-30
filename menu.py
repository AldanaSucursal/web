import flet as ft
import inicio
import usuario
import prendasag
import proveedorag
import categoria
import login
def main(page:ft.Page):
    def mostrar_opcion(e:ft.ControlEvent):
        if e.control.selected_index==0:
            contenedorP.content=inicio.main(page)
        elif e.control.selected_index==1:
            contenedorP.content=usuario.main(page)
        elif e.control.selected_index==2:
            contenedorP.content=proveedorag.main(page)
        elif e.control.selected_index==3:
            contenedorP.content=prendasag.main(page)
        elif e.control.selected_index==4:
            contenedorP.content=categoria.main(page)
        elif e.control.selected_index==5:
            # # page.window_close()
            # page.clean()
            contenedorP.clean()
            contenedorP.content=login.main(page)
        contenedorP.update()

    page.title='Sistema de Administracion ALDANA👍' 
    page.appbar=ft.AppBar(title=ft.Text('Sistema Aldana',font_family="Times New Roman",size=30),
                            leading=ft.Icon(ft.icons.ADD_CIRCLE),
                            center_title=True,
                            bgcolor=ft.colors.BLUE,
                            color="White")
    page.theme_mode=ft.ThemeMode.LIGHT
    # page.scroll=True

    #Botones de Navegacion
    btninicio=ft.NavigationRailDestination(icon=ft.icons.HOME_ROUNDED,
                                           selected_icon=ft.icons.HOME_OUTLINED,
                                           label='Inicio')
    btnusuario=ft.NavigationRailDestination(icon=ft.icons.PERSON_PIN_CIRCLE_SHARP,
                                            selected_icon=ft.icons.PERSON_PIN_CIRCLE_OUTLINED,
                                            label='Usuario')
    btnprendas=ft.NavigationRailDestination(icon=ft.icons.SHOPPING_CART_ROUNDED,
                                            selected_icon=ft.icons.SHOPPING_CART_OUTLINED,
                                            label='Prendas')
    btncategorias=ft.NavigationRailDestination(icon=ft.icons.LIBRARY_BOOKS_ROUNDED,
                                               selected_icon=ft.icons.LIBRARY_BOOKS_OUTLINED,
                                               label='Categoria')
    btnproveedor=ft.NavigationRailDestination(icon=ft.icons.PERSON_ADD_ROUNDED,
                                              selected_icon=ft.icons.PERSON_ADD_OUTLINED,
                                              label='Proveedor')
    btnSalir=ft.NavigationRailDestination(icon=ft.icons.CLOSE,
                                          label='Salir')
    #LIsta de los Botones Anteriores
    lista_botones=[btninicio,btnusuario,btnproveedor,btnprendas,btncategorias,btnSalir]
    #Componente NAVIGATION RAIL
    navrail=ft.NavigationRail(bgcolor=ft.colors.BLUE,
                                destinations=lista_botones,
                                on_change=mostrar_opcion)
    #Contenedor Principal
    contenedorP=ft.Container(expand=True,
                             gradient=ft.LinearGradient([ft.colors.BLUE_400,ft.colors.WHITE70,ft.colors.BLUE_400]))
    
    #Fila para el Rail y el Contenedor Principal
    fila=ft.Row([navrail,contenedorP],expand=True)

    return fila
    # page.add(fila)
    # page.update()
if __name__=='__main__':
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)