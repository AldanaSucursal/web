import flet as ft
def main(page:ft.Page):
    page.scroll=True

    txttitulo=ft.Text('BIENVENIDO',
                      size=50,
                      text_align=ft.TextAlign.CENTER,
                      italic=True)
    icono=ft.Icon(ft.icons.HOME,size=50)
    rwIT=ft.Row([txttitulo,icono])
    txtdescripcion=ft.Text('El siguiente software funciona en cuestion para llevar el inventario de nuestros productos',
                           width=450,
                           height=150,
                           size=30,
                           text_align=ft.TextAlign.CENTER,
                           italic=True)
    
    logo=ft.Image(src='logo.png',
                  border_radius=250,
                  width=210,
                  height=210)
    rwDL=ft.Row([txtdescripcion,logo])

    txtmujer=ft.Text('Mujer',size=40)
    imgM=ft.Image(src='mujer.png'
                  ,width=100,
                  height=100,
                  border_radius=200)
    txtcategoriaM=ft.Text('Categoria',size=20,italic=True)
    txt1=ft.Text('BLUSAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img1=ft.Image(src='categoriaM/blusas.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc1=ft.Row([txt1,img1])

    txt2=ft.Text('VESTIDOS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img2=ft.Image(src='categoriaM/vestidos.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc2=ft.Row([txt2,img2])

    txt3=ft.Text('FALDAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img3=ft.Image(src='categoriaM/faldas.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc3=ft.Row([txt3,img3])

    txt4=ft.Text('PLAYERAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img4=ft.Image(src='categoriaM/playeras.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc4=ft.Row([txt4,img4])

    txt5=ft.Text('PANTALONES',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img5=ft.Image(src='categoriaM/pantalones.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc5=ft.Row([txt5,img5])

    txt6=ft.Text('JEANS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img6=ft.Image(src='categoriaM/jeans.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc6=ft.Row([txt6,img6])

    txt7=ft.Text('SUDADERAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img7=ft.Image(src='categoriaM/sudadera.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc7=ft.Row([txt7,img7])

    txt8=ft.Text('ABRIGOS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img8=ft.Image(src='categoriaM/abrigo.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc8=ft.Row([txt8,img8])

    txt9=ft.Text('CHALECOS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    img9=ft.Image(src='categoriaM/chaleco.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwc9=ft.Row([txt9,img9])

    clmmujer=ft.Column([txtmujer,imgM,txtcategoriaM,rwc1,rwc2,rwc3,rwc4,rwc5,rwc6,rwc7,rwc8,rwc9],
                       width=350)

    txthombre=ft.Text('Hombre',size=40)
    imgH=ft.Image(src='hombre.png',
                  width=100,
                  height=100,
                  border_radius=200)
    txtcategoriaH=ft.Text('Categoria',size=20,italic=True)

    txth1=ft.Text('PLAYERAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh1=ft.Image(src='categoriaH/playeras.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh1=ft.Row([txth1,imgh1])

    txth2=ft.Text('CAMISAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh2=ft.Image(src='categoriaH/camisas.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh2=ft.Row([txth2,imgh2])

    txth3=ft.Text('PANTALONES',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh3=ft.Image(src='categoriaH/pantalones.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh3=ft.Row([txth3,imgh3])

    txth4=ft.Text('JEANS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh4=ft.Image(src='categoriaH/jeans.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh4=ft.Row([txth4,imgh4])

    txth5=ft.Text('SUDADERAS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh5=ft.Image(src='categoriaH/sudadera.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh5=ft.Row([txth5,imgh5])

    txth6=ft.Text('ABRIGOS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh6=ft.Image(src='categoriaH/abrigo.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh6=ft.Row([txth6,imgh6])

    txth7=ft.Text('CHALECOS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh7=ft.Image(src='categoriaH/chaleco.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh7=ft.Row([txth7,imgh7])

    txth8=ft.Text('SACOS',
                  size=20,
                  font_family='times new roman',
                  italic=True)
    imgh8=ft.Image(src='categoriaH/sacos.png',
                  width=100,
                  height=100,
                  border_radius=200)
    rwh8=ft.Row([txth8,imgh8])

    txtvacio=ft.Text(width=100,height=100)

    clmhombre=ft.Column([txthombre,imgH,txtcategoriaH,rwh1,rwh2,rwh3,rwh4,rwh5,rwh6,rwh7,rwh8,txtvacio],
                        width=350)

    rwMH=ft.Row([clmmujer,clmhombre],alignment='center')

    columna=ft.Column([rwIT,rwDL,rwMH],alignment='center',scroll=True)
    return columna
    # page.add(columna)
if __name__=='__main__':
    ft.app(target=main)