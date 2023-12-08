import flet as ft
import os
from pathlib import Path
import random
from flet import *


def main(page: Page):
    page.theme_mode = ThemeMode.LIGHT
    page.padding = 50
    page.update()

    folder_paths = ["assets/img/xbox/",
                    "assets/img/notebooks/", "assets/img/playstation/"]

    def orderBtn():
        pass

    gridView = ft.GridView(
        child_aspect_ratio=1.0,
        expand=1,
        runs_count=5,
        max_extent=240,
        auto_scroll=True,
        spacing=170,
        padding=10,
        run_spacing=100,
    )

    # Iterar sobre os diretórios
    for folder_path in folder_paths:
        # Obter a lista de arquivos no diretório e ordená-los
        files = sorted(os.listdir(folder_path))

        for file_name in files:
            if os.path.isfile(os.path.join(folder_path, file_name)):
                product_name, ext = os.path.splitext(file_name)
                product = {
                    "name": product_name,
                    "image": os.path.join(folder_path, file_name),
                    "estoque": random.randint(1, 10),
                    "price": random.randint(2400, 5990),
                    # "rating": round(random.uniform(2, 5), 1)
                }

                # Adicionar um Card ao GridView
                gridView.controls.append(
                    ft.Card(

                        elevation=10,
                        content=ft.Container(
                            bgcolor="white",
                            width=230,
                            height=340,
                            content=ft.Column([
                                ft.Image(src=product["image"],

                                         width=160,
                                         height=140),
                                ft.Container(
                                    padding=10,
                                    width=230,
                                    height=175,
                                    bgcolor="#a0a0a0",
                                    border_radius=ft.border_radius.only(
                                        top_left=10, top_right=10
                                    ),
                                    content=ft.Column([
                                        ft.Text(product["name"],
                                                size=16,
                                                weight=ft.FontWeight.BOLD),
                                        ft.Text(f"Preço: R$ {product['price']}",
                                                size=15, weight="bold"),
                                        ft.Text(f"Estoque: {product['estoque']}",
                                                size=14),

                                        ft.Row([

                                            ft.ElevatedButton(
                                                text="Comprar",
                                                bgcolor="#ff6b00",
                                                color="white",
                                                width=180,
                                                height=35,
                                                on_click=orderBtn
                                            ),

                                        ], spacing="spaceBetween"),
                                    ])
                                )
                            ])
                        )
                    )
                )
                page.update()

    page.add(
        AppBar(
            title=Text("TechTemple", size=32),
            bgcolor="#0c4b85",

        ),

        Column([

            gridView,
        ]),
    )


ft.app(target=main, assets_dir="assets")
