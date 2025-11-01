# proyecto
import flet as ft
import json

inventario = "info.json"

#def leer_json(json: str) -> dict :
#    """
#    lee un archivo
#    """
#    productos = {}
#
#    with open("C:\\Users\\FLIA RODRIGUEZ\\Desktop\\pythoon\\Proyecto Final Organisador de Negocio\\json\\inf","r") as file:
#        productos = json.load(file)
#    return productos
#def escribir_json(file_name: str, producto: list[dict]) -> None:
#    """
#    Permite escribir en el archivo
#    """
#    with open(file_name,"w") as file:
#        json.dump(producto, file)

def crear_producto(nombre, precio_vent, precio_comp, cantidad):
    producto = ft.Container(
        content=ft.Column([
            ft.Text(value= {nombre}, size=16, weight=ft.FontWeight.BOLD),
            ft.Text(value= {precio_vent}, size=14),
            ft.Text(value= {precio_comp}, size=12),
            ft.Text(value= {cantidad}, size=14),
            ft.ElevatedButton(text="vender", color=ft.Colors.WHITE)
        ]),
        bgcolor = ft.Colors.BLUE_500,
        border_radius=10,
        padding=20,
        alignment= ft.alignment.center,
    )
    return producto
def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "inventario"
    titulo = ft.Text(value="TOTO NOVEDADES", size=54, weight=ft.FontWeight.BOLD)
    app_bar = ft.AppBar(
        title = titulo,
        center_title = True,
        bgcolor = ft.Colors.BLUE_800,
    )
    inventario = ft.ListView(padding=20)

    def boton_agr(e):
        
        if not nom_producto.value:
            nom_producto.error_text = "por favor ingrese un texto"
            precio_vnt.error_text = "ingrese precio de venta"
            cantidad.error_text = "ingrese una cantidad"
        else:
            
            page.update()
            return
            
    def crear_producto(
            nom_producto, 
            precio_vnt, 
            precio_comp, 
            cantidad):
        producto = ft.Container(
        content=ft.Column([
            ft.Text(value= nom_producto, size=16, weight=ft.FontWeight.BOLD),
            ft.Text(value= precio_vnt, size=14),
            ft.Text(value= precio_comp, size=12),
            ft.Text(value= cantidad, size=14),
            ft.ElevatedButton(text="vender", color=ft.Colors.WHITE)
        ]),
        bgcolor = ft.Colors.BLUE_500,
        border_radius=10,
        padding=20,
        alignment= ft.alignment.center,
        )
        inventario.controls.append(producto)
#        with open("C:\\Users\\FLIA RODRIGUEZ\\Desktop\\pythoon\\Proyecto Final Organisador de Negocio\\info.json","r+"):
#            json.dump(producto)
        page.update()

    nom_producto = ft.TextField(label= "nombre del producto", width= True)
    precio_vnt = ft.TextField(label= "precio de venta", width= True)
    precio_comp = ft.TextField(label= "presio de compra", width= True)
    cantidad = ft.TextField(label= "cantidad", width= True)
#    examinar = ft.ElevatedButton(text="examinar", on_click=boton_agr)
#    crear_producto(nom_producto, precio_vnt, precio_comp, cantidad)    
    anadir_prod = ft.ElevatedButton(text="añadir producto", on_click=boton_agr)
    agregar_productos = ft.Column([
                        ft.Text(value="producto", size= 20, weight= ft.FontWeight.BOLD),
                        nom_producto,
                        precio_vnt,
                        precio_comp,
                        cantidad,
                        anadir_prod
                        ], spacing=20
                        )
    
    ganancias = ft.ListView(padding=20)

    def destino(e):
        index = e.control.selected_index
        contenido.controls.clear()
        if index == 0:
            contenido.controls.append(inventario)
        elif index == 1:
            contenido.controls.append(agregar_productos)
        elif index == 2:
            contenido.controls.append(ganancias)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(icon= ft.Icons.LIST_ALT, label = "inventario"),
            ft.NavigationRailDestination(icon= ft.Icons.ADD_CIRCLE, label = "agregar producto"),
            ft.NavigationRailDestination(icon= ft.Icons.ATTACH_MONEY, label = "ganancias"),
        ], on_change= destino,
    )
    contenido = ft.Column([inventario], expand=True)

    page.add(app_bar, ft.Row([rail, ft.VerticalDivider(width=1), contenido], expand=True))
crear_producto("esfera de luz", 10000, 4000, 10)
ft.app(target=main)

