from nicegui import ui

with ui.tabs() as tabs:
    ui.tab("Home", icon="home")
    ui.tab("About", icon="info")
    ui.tab("Help", icon="help")

with ui.tab_panels(tabs, value="Home"):
    with ui.tab_panel("Home"):
        ui.markdown('''##Welcome to HenHub!''')
        ui.label("")
        ui.input(label='Enter your canvas id:')
    with ui.tab_panel("About"):
        ui.label("Connect with students taking similar courses")
    with ui.tab_panel("Help"):
        ui.markdown("##Follow this guid to learn how to set up the API")


ui.run()