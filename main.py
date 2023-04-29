from nicegui import ui

with ui.tabs() as tabs:
    ui.tab("Home", icon="home")
    ui.tab("About", icon="info")
    ui.tab("Help", icon="help")

with ui.tab_panels(tabs, value="Home"):
    with ui.tab_panel("Home"):
        ui.markdown('''##Welcome to HenHub!''')
        ui.label('''To learn how to access your Canvas User ID, check out our help tab!\n
                 Remember: Do not share your User ID with anyone!''')
        ui.input(label='Enter your Canvas ID:')
    with ui.tab_panel("About"):
        ui.label("Connect with students taking similar courses!")


ui.run()