import flet as ft
def main(page:ft.Page):
    #Datos solamente por defecto realizados con TEXTOS    
    txtusuario=ft.Text('Sucursal',size=30,weight=ft.FontWeight.BOLD,font_family='times new roman')
    txt1=ft.Text('Sucursal: Sucursal Aldana',size=20,font_family='verdana')
    txt2=ft.Text('No de Sucursal: 1',size=20,font_family='verdana')
    txt4=ft.Text('Direccion: AV.------col----#--',size=20,font_family='verdana')
    txt5=ft.Text('Telefono: 993 541 23 08',size=20,font_family='verdana')
    txt6=ft.Text('Email:sucursal_aldana@almacen.com',size=20,font_family='verdana')
    txtcolumna=ft.Column([txtusuario,txt1,txt2,txt4,txt5,txt6])

    imagen=ft.Image(src='logo.png',
                    width=300,
                    height=300,
                    border_radius=200)
    rw=ft.Row([txtcolumna,imagen])

    columnaF=ft.Column([rw])
    return columnaF
    # page.add(columnaF)
if __name__=='__main__':
    ft.app(target=main)