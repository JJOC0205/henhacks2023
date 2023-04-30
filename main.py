from nicegui import ui    
import canvas_api
import server
    
with ui.tabs() as tabs:
    ui.tab("Home", icon="home")
    ui.tab("About", icon="info")
    ui.tab("Help", icon="help")

    
with ui.tab_panels(tabs, value="Home"):
    with ui.tab_panel("Home"):
        ui.markdown("#Welcome to HenHub!")
        ui.label("To learn how to generate your Canvas access token, check out our help tab!\nRemember: Do not share your token with anyone!")
        ui.input(label='Enter your Canvas access token:', on_change=lambda e: server.server(e.value))
    with ui.tab_panel("About"):
        ui.label("Connect with students taking similar courses!")
    with ui.tab_panel("Help"):
        ui.markdown("##Follow this guide to learn how to set up the API") 

ui.run()
