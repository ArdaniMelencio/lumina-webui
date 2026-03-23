import webview, json, time, pathlib, datetime

class Api:
    
    def __init__(self):
        self.window = None
        self.model  = 'deepseek-v3.1:671b-cloud'
        
        
    def _set_window(self, window):
        self.window = window
        
        
    def close_app(self):
        import sys
        if webview.windows:
            webview.windows[0].destroy()
        sys.exit(0)
 
def launch_webview(use_debug: bool = False):
    """Launches pywebview with/out debugging"""
    
    
    print(pathlib.Path.cwd() / "frontend")
    
    api = Api()
    window = webview.create_window(
        'Lumina Web UI',
        '../../frontend/index.html',
        frameless=True,
        easy_drag=True,
        js_api=api,
        min_size=(420, 420)
    )
    
    api._set_window(window=window)
    webview.start(debug=use_debug, gui='gtk')
    
    
        
if __name__ == "__main__":
    
    launch_webview(True)