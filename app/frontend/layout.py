from nicegui import ui
import js

drawer_open = True


def layout_wrapper(content_function):

    ui.add_head_html('''
        <style type="text/tailwindcss">
            .q-btn:before {
                    box-shadow: none !important; /* Elimina el sombreado */
                        }
            .hover-row {
                transition: background-color 0.3s ease; /* Smooth transition */
            }
            .hover-row:hover {
                background-color: #4a7550 !important; /* Unified hover color */
                cursor: pointer; /* Change cursor to pointer */
            }
                     
            @media (max-width: 800px) {
                    #c24 {
                        width: 100px !important;
                    }
                    .left-drawer-label {
                        display: none !important; 
                    }
                    .left-drawer-icon {
                        margin: 5px 38px 0px 38px !important;
                    }
                    .main-content {
                        margin-left: 100px !important; 
                    }
                    
            }
                     
            @media (max-width: 700px) {
                    #c7 {
                        display: none !important;
                    }
                    #c24 {
                        width: 100px !important;
                    }
                    .left-drawer-label {
                        display: none !important; 
                    }
                    .left-drawer-icon {
                        margin: 5px 38px 0px 38px !important;
                    }
                    .main-content {
                        margin-left: 100px !important; 
                    }
                    
            }
                     
            @media (max-width: 500px) {
                    #c7 {
                        display: none !important;
                    }
                    #c24 {
                        width: 100px !important;
                    }
                    .left-drawer-label {
                        display: none !important; 
                    }
                    .left-drawer-icon {
                        margin: 5px 38px 0px 38px !important;
                    }
                    .main-content {
                        margin-left: 0px !important; 
                    }
                    
            }
                     
            
        </style>
    ''')

    ui.add_head_html(''' 
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=genetics" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        ''')


    with ui.header().style('height:60px; BACKGROUND-COLOR: rgb(44, 95, 52);  color:white; top:0; width:100%; margin:0 0 0 0; padding:0; display:flex; align-items:center; justify-content:center'):
        with ui.row().classes('header-row').style('height:70px; BACKGROUND-COLOR:#2C5F34; color:white; top:0; width:100%; margin:0 0 0 0; padding:0; display:flex; align-items:center; justify-content:space-between'):
            ui.image('/icons/gvs_logo.png').classes('logo').style('width: 60px; margin: 20px')
            with ui.row().classes('header-row').style('height:60px; BACKGROUND-COLOR:#2C5F34; color:white; top:0; margin:0 0 0 0; padding:0; display:flex; align-items:center; justify-content:center'):
                #ui.button('Click me!', on_click=lambda:  toggle_drawer(ld))
                ui.label('Acerca').style('font-size: 1.5em;')
                ui.label('Servicios').style('font-size: 1.5em;')
                ui.label('Contacto').style('font-size: 1.5em;')

            with ui.row().classes('header-row'):
                with ui.dropdown_button(icon='language', color='#2C5F34', split=False).style('padding:0px; font-size: 17px; align-items: center;'):
                    with ui.column():
                        ui.button('Español', color='white').style('padding:10px ; font-size: 14px; color:#283618; align-items: center; text-align: center; text-transform: none; display: block; width: 100%; margin: 0 auto;')
                        ui.button('English', color='white').style('padding:10px ; font-size: 14px; color:#283618; align-items: center; text-align: center; text-transform: none; display: block; width: 100%; margin: 0 auto;')
                with ui.dropdown_button(icon='notifications', color='#2C5F34', split=False, auto_close=True).style('padding:0px; font-size: 17px;'):
                    with ui.column():
                        ui.label('')
                with ui.dropdown_button(icon='account_circle', color='#2C5F34', split=False, auto_close=True).style('padding:0px; font-size: 17px;'):
                    with ui.column():
                        ui.button('Perfil', icon='perm_identity').style('padding:10px ; font-size: 14px; background-color:white !important; color:#283618 !important; text-align: center; text-transform: none; display: block; width: 100%; margin: 0; border-radius: 0px;')
                        ui.button('Configuración', icon='settings').style('padding:10px ; font-size: 14px; background-color:white !important; color:#283618 !important; text-align: center; text-transform: none; display: block; width: 100%; margin: 0; border-radius: 0px;')
                        ui.button('Cerrar sesión', icon='logout').style('padding:10px ; font-size: 14px; background-color:white !important; color:#283618 !important; text-align: center; text-transform: none; display: block; width: 100%; margin: 0; border-radius: 0px;')

    ld = ui.left_drawer(value=True, top_corner=False, bottom_corner=True).props('breakpoint=500 width="220px"').style('background-color: #2C5F34; width: 220px; max-width: 220px; color:white;  padding: 0px; margin: 0px;')
    with ld:
        with ui.column().style('padding: 0px; margin: 10px 0px 10px 0px; width: 100%;'):
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('analytics').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Dashboard', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('medical_information').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Perfil Animal', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('genetics').classes('left-drawer-icon').classes('material-symbols-outlined').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Genetica y Crianza', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('fence').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Gestión de Cercados', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('balance').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Registro de Peso', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('monitor_heart').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Historial de Salud', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('grass').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Nutrición', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('local_shipping').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Gestión de Transporte', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')
            with ui.row().classes('hover-row').style('width:100%'):
                ui.icon('handyman').classes('left-drawer-icon').style('font-size: 24px; color: #e3e3e3; margin: 5px 10px 0px 10px;')
                ui.button('Gestión de Operaciones', color='#2C5F34').classes('left-drawer-label').style('width: 160px; max-width: 160px; font-size: 14px; background-color:#2C5F34 !important; color:white !important; text-transform: none; text-align: left !important; display: block; margin: 0; border-radius: 0px; padding: 0px')

    with ui.column().classes('main-content').style('margin-left: 220px;'):
            content_function()

def toggle_drawer(ld):
    global drawer_open
    drawer_open = not drawer_open
    ld.set_value(drawer_open)
    ui.update() 
    ui.notify(f'You clicked me!{drawer_open}')

    
def default_layout(title: str):
    with ui.header().classes('bg-primary text-white'):
        ui.label(title).classes('text-h5')
    with ui.left_drawer().classes('bg-grey-2'):
        ui.link('Dashboard', '/dashboard')
        ui.link('Tables', '/tables')
        ui.link('Home', '/')