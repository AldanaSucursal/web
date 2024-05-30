import flet as ft
import hombre
import mujer
def main(page:ft.Page):
    def interfaces(e:ft.ControlEvent):
        if e.control.selected_index==0:
            contendor.content=hombre.main(page)
        elif e.control.selected_index==1:
            contendor.content=mujer.main(page)
        contendor.update()

    
    txtcategoria=ft.Text('Categoria',size=25,weight=ft.FontWeight.W_800)
    txthhombre=ft.Text('Hombre',size=30,weight=ft.FontWeight.BOLD)

    btnH=ft.NavigationDestination(icon=ft.icons.PERSON_4_SHARP,label='Hombre',
                                  selected_icon=ft.icons.PERSON_4_OUTLINED)
    btnM=ft.NavigationDestination(icon=ft.icons.PERSON_2_SHARP,label='Mujer',
                                  selected_icon=ft.icons.PERSON_2_OUTLINED)
    listabotones=[btnH,btnM]

    nav=ft.NavigationBar(destinations=listabotones,
                            on_change=interfaces,
                            width=300,
                            bgcolor=ft.colors.TRANSPARENT,
                            )

    contendor=ft.Container()
    columna=ft.Column([txtcategoria,txthhombre,nav,contendor])
    return columna
if __name__=='__main__':
    ft.app(target=main)