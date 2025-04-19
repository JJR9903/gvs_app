from nicegui import ui
from .layout import default_layout

def show_tables():
    default_layout("Interactive Table")

    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
    ]

    table = ui.table(columns=[
        {'name': 'name', 'label': 'Name', 'field': 'name'},
        {'name': 'age', 'label': 'Age', 'field': 'age'},
    ], rows=data, row_key='name').classes('w-full')