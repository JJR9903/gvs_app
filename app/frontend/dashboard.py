from app.frontend.layout import layout_wrapper
from nicegui import ui

def build_dashboard():
    def content():
        ui.label('Contenido del dashboard').classes('text-h4')
    
    layout_wrapper(content)