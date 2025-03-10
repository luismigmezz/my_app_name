"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:

    return rx.container(
        rx.hstack(
            rx.color_mode.button(position="top-right"),
            rx.image(src="/logo.png", width="100px", height="auto",position="top-left"),
            rx.heading("OLIMPIADA DE DEBATE", size="9", color_scheme="orange", position="top-center"),
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
