from nicegui import ui

with ui.tabs() as tabs:
    ui.tab("Home", icon="home")
    ui.tab("About", icon="info")

with ui.tab_panels(tabs, value="Home"):
    with ui.tab_panel("Home"):
        ui.label("##Welcome to HenHub!")
    with ui.tab_panel("About"):
        ui.label("Connect with students taking similar courses")


ui.run()