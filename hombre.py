import flet as ft
from registrosH import sacos,playeras,camisas,pantalones,jeans,sudaderas,abrigos,chalecos
def main(page:ft.Page):
    def registros(e:ft.ControlEvent):
        if e.control.selected_index==0:
            contenedorR.content=playeras.main(page)
        elif e.control.selected_index==1:
            contenedorR.content=camisas.main(page)
        elif e.control.selected_index==2:
            contenedorR.content=pantalones.main(page)
        elif e.control.selected_index==3:
            contenedorR.content=jeans.main(page)
        elif e.control.selected_index==4:
            contenedorR.content=sudaderas.main(page)
        elif e.control.selected_index==5:
            contenedorR.content=abrigos.main(page)
        elif e.control.selected_index==6:
            contenedorR.content=chalecos.main(page)
        elif e.control.selected_index==7:
            contenedorR.content=sacos.main(page)
        contenedorR.update()
        
    btn1=ft.NavigationDestination(label='PLAYERAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn2=ft.NavigationDestination(label='CAMISAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn3=ft.NavigationDestination(label='PANTALONES',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn4=ft.NavigationDestination(label='JEANS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn5=ft.NavigationDestination(label='SUDADERAS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn6=ft.NavigationDestination(label='ABRIGOS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn7=ft.NavigationDestination(label='CHALECOS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)
    btn8=ft.NavigationDestination(label='SACOS',
                                  icon=ft.icons.NAVIGATION_SHARP,
                                  selected_icon=ft.icons.NAVIGATION_OUTLINED)

    filabotones=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8]
    nav=ft.NavigationBar(destinations=filabotones,
                         on_change=registros,
                         width=650,
                         height=50,
                         bgcolor=ft.colors.TRANSPARENT)

    contenedorR=ft.Container()

    columna=ft.Column([nav,contenedorR])
    #page.add(columna)
    return columna
if __name__=='__main__':
    ft.app(target=main)