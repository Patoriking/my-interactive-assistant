import sys
from pathlib import Path
import webview
 
def resource_path(relative_path: str) -> Path:
    if getattr(sys, '_MEIPASS', None):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).resolve().parent / relative_path
 
class API:
    def hello(self, name):
        return f'Olá {name}! Python respondeu.'
 
index_file = resource_path('web/index.html')

window = webview.create_window(
    'Meu App',
    index_file.as_uri(),
    js_api=API(),
)

webview.start()#debug=True)