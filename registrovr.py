import flet as ft
import modelo
def main(page:ft.Page):
    tabla=[]
    registros=modelo.Prendas.select()
    for r in registros:
        cel1=ft.DataCell(ft.Text(r.id_prenda))
        cel2=ft.DataCell(ft.Text(r.id_proveedor.nombre))
        cel3=ft.DataCell(ft.Text(r.cantidad))
        cel4=ft.DataCell(ft.Text(r.id_categoria.tipo))
        cel5=ft.DataCell(ft.Text(r.id_categoria.categoria))
        cel6=ft.DataCell(ft.Text(r.talla))
        cel7=ft.DataCell(ft.Text(r.color))
        cel8=ft.DataCell(ft.Text(r.fecha))
        fila=ft.DataRow(cells=[cel1,cel2,cel3,cel4,cel5,cel6,cel7,cel8])
        tabla.append(fila)
    
    encabezado=[ft.DataColumn(ft.Text('ID')),
                ft.DataColumn(ft.Text('PROVEEDOR')),
                ft.DataColumn(ft.Text('CANTIDAD')),
                ft.DataColumn(ft.Text('TIPO')),
                ft.DataColumn(ft.Text('CATEGORIA')),
                ft.DataColumn(ft.Text('TALLA')),
                ft.DataColumn(ft.Text('COLOR')),
                ft.DataColumn(ft.Text('FECHA'))]

    tbl=ft.DataTable(columns=encabezado,
                     rows=tabla,
                     heading_row_color=ft.colors.GREEN,
                     border=ft.border.all(5,"blue"),
                     border_radius=15)
    
    return tbl
    # page.add(tbl)
if __name__=='__main__':
    ft.app(target=main)