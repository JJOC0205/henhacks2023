from nicegui import ui    
import canvas_api
import server

def run_server(key:str):
    server.server(key)
def grab_data(key:str):
    server.grab_database_values(key)
    
    
with ui.tabs() as tabs:
    ui.tab("Home", icon="home")
    ui.tab("About", icon="info")
    ui.tab("Help", icon="help")


with ui.tab_panels(tabs, value="Home"):
    with ui.tab_panel("Home"):
        ui.markdown("#Welcome to HenHome!").style('color: #6E93D6')
        ui.label("To learn how to generate your Canvas access token, check out our help tab!")
        ui.label("Remember: Do not share your token with others!")
        result = ui.label()
        ui.label("Enter your 1. name, 2. email, and 3. All seperated by commas, no spaces.")
        ui.textarea(label='Press button below when finished:', on_change=lambda e: result.set_text(e.value))
        ui.button("Click here when finished typing", on_click=lambda: run_server(result.text))
        ui.button("Click here when you want data", on_click=lambda: grab_data(result.text))
    with ui.tab_panel("About"):
        ui.markdown("###Looking for a study group, project members, tutors, or friends in your major?")
        ui.markdown("###At HenHome, we connect you to students with a similar courseload!")
        ui.markdown("Through the Canvas API, we match you with peers that contain a similar courseload ")
    with ui.tab_panel("Help"):
        ui.markdown("#How to set up the API:") 
        ui.markdown("###1. Open User Settings")
        ui.image("https://media.screensteps.com/image_assets/assets/003/849/598/original/db51db90-7eb7-4482-ae89-461b84f2b7db.png")
        ui.label("Click Account, then Settings.").style("font-size: 200%")
        ui.markdown("###2. View Access Tokens")
        ui.image("https://media.screensteps.com/image_assets/assets/002/784/051/medium/033d4573-b8e4-4b72-8d8e-4574fbc7447a.png")
        ui.label("Scroll to the Approved Integrations section [1]. For each access token, you can view the name [2], purpose [3], expiration date [4], and date of last use [5]")
        ui.markdown("###3. Add Access Token")
        ui.image("https://media.screensteps.com/image_assets/assets/002/093/519/original/a8efe835-1f4b-4eb0-80a3-8e10df982df3.png")
        ui.label("to manually add an access token, click the Add New Access Token button.")
        ui.markdown("###4. Add Token Details")
        ui.image("https://media.screensteps.com/image_assets/assets/002/093/517/original/d324a9dc-95d2-4a78-9704-9102da2b8766.png")
        ui.label("Enter a description for your access token in the Purpose field [1]. You can also select an expiration date by clicking the Calendar icon [2]. To generate a token with no expiration, leave the Expires field empty. To generate a new access token, click the Generate Token button [3].")
        ui.markdown("###5. View Token Details")
        ui.image("https://media.screensteps.com/image_assets/assets/002/093/530/original/20ec3fae-b100-4469-8c22-514ab3f31479.png")
        ui.label("The access token details include a token that can be used to make API calls on your behalf [1]. To regenerate an access token, click the Regenerate Token button [2].")
        

ui.run()
