from nicegui import ui
from .layout import default_layout

def show_login():
    default_layout("Login")

    with ui.card().classes('absolute-center'):
        ui.label('Login').classes('text-h4')
        username = ui.input('Username').props('outlined').classes('w-full')
        password = ui.input('Password').props('outlined type=password').classes('w-full')
        ui.button('Login', on_click=lambda: ui.notify(f'Welcome, {username.value}'))