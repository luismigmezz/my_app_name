"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import asyncio
from rxconfig import config


class State(rx.State):
    segundos_restantes: int = 60
    esta_activo: bool = False

    @rx.event(background=True)
    async def iniciar_cuenta_regresiva(self):
        async with self:
            self.esta_activo = True
        while True:
            async with self:
                if not self.esta_activo or self.segundos_restantes <= 0:
                        return
                self.segundos_restantes -= 1
            await asyncio.sleep(1)

    @rx.event
    def detener(self):
        self.esta_activo = False

    @rx.event
    def reiniciar(self):
        self.segundos_restantes = 60
        self.esta_activo = False


def index() -> rx.Component:

    return rx.container(
        rx.hstack(
            rx.color_mode.button(position="top-right"),
            rx.image(src="/logo.png", width="100px", height="auto",position="top-left"),
            rx.heading("OLIMPIADA DE DEBATE", size="9", color_scheme="orange", position="top-center"),
         ),
            rx.heading(f"{State.segundos_restantes} segundos"),
            rx.hstack(
                rx.button("Iniciar", on_click=State.iniciar_cuenta_regresiva),
                rx.button("Detener", on_click=State.detener),
                rx.button("Reiniciar", on_click=State.reiniciar),
            ),
          rx.hstack(
                        rx.link(
                            rx.button("Check out our docs!"),
                            href="https://classroom.google.com/c/NzEwODcxNTQ5NDcy",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button("Check out our docs!"),
                            href="https://classroom.google.com/c/NzEwODcxNTQ5NDcy",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button("Check out our docs!"),
                            href="https://classroom.google.com/c/NzEwODcxNTQ5NDcy",
                            is_external=True,
                        ),
            ),
            rx.vstack(
           
           rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.hstack(
                        rx.link(
                            rx.button("Check out our docs!"),
                            href="https://classroom.google.com/c/NzEwODcxNTQ5NDcy",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button("Check out our docs!"),
                            href="https://classroom.google.com/c/NzEwODcxNTQ5NDcy",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button("Check out our docs!"),
                            href="https://classroom.google.com/c/NzEwODcxNTQ5NDcy",
                            is_external=True,
                        ),
            ),
                                

            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
