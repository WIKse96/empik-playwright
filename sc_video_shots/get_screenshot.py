from datetime import datetime

#funcka mająca na celu zapisanie screenshota w przypadku błędu z nazwą w schemacie rokMiesiacDzienGodzinaMinutaSekuna

def screenshot(page, namef):
    page.screenshot(path=f"media/{namef}/sc-{namef}-{datetime.now().strftime('%Y%m%d%H%M%S')}-screenshot.png", full_page=True)