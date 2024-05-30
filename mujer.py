import flet as ft
from registrosM import blusas,vestidos,faldas,playeras,pantalones,jeans,sudaderas,abrigos,chalecos
def main(page:ft.Page):
    def registrosm(e:ft.ControlEvent):
        if e.control.selected_index==0:
            contenedorRM.content=blusas.main(page)
        elif e.control.selected_index==1:
            contenedorRM.content=vestidos.main(page)
        elif e.control.selected_index==2:
            contenedorRM.content=faldas.main(page)
        elif e.control.selected_index==3:
            contenedorRM.content=playeras.main(page)
        elif e.control.selected_index==4:
            contenedorRM.content=pantalones.main(page)
        elif e.control.selected_index==5:
            contenedorRM.content=jeans.main(page)
        elif e.control.selected_index==6:
            contenedorRM.content=sudaderas.main(page)
        elif e.control.selected_index==7:
            contenedorRM.content=abrigos.main(page)
        elif e.control.selected_index==8:
            contenedorRM.content=chalecos.main(page)
        contenedorRM.update()

    btn1=ft.NavigationDestination(label='BLUSAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn2=ft.NavigationDestination(label='VESTIDOS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn3=ft.NavigationDestination(label='FALDAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn4=ft.NavigationDestination(label='PLAYERAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn5=ft.NavigationDestination(label='PANTALONES',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn6=ft.NavigationDestination(label='JEANS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn7=ft.NavigationDestination(label='SUDADERAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn8=ft.NavigationDestination(label='ABRIGOS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn9=ft.NavigationDestination(label='CHALECOS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)

    filabotones=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
    nav=ft.NavigationBar(destinations=filabotones,
                         on_change=registrosm,
                         width=720,
                         height=50,
                         bgcolor=ft.colors.TRANSPARENT)
    
    contenedorRM=ft.Container()

    columna=ft.Column([nav,contenedorRM])
    return columna
if __name__=='__main__':
    ft.app(target=main)