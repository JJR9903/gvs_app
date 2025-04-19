
import os
from nicegui import ui, app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.backend.api_router import api_router
from app.frontend import dashboard, auth, tables


fastapi_app = FastAPI()
fastapi_app.include_router(api_router)

icons_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend', 'icons'))
print("📂 Serving /icons from:", icons_path)

app.add_static_files('/icons', icons_path)

# Define your NiceGUI pages
@ui.page('/')
def index():
    #auth.show_login()
    dashboard.build_dashboard()

@ui.page('/dashboard')
def dash():
    dashboard.build_dashboard()

@ui.page('/tables')
def tbl():
    tables.show_tables()



# Make sure this matches the actual path to your icons folder

ui.run(title='NiceGUI Test', host='127.0.0.1', port=8600)
#ui.run_with(
#    fastapi_app,
#    title='NiceGUI Test',
#    host='127.0.0.1',
#    port=8600,
#    storage_secret='supersecret123'
#)