import webview, json, time, pathlib, datetime, sys
import logging_handler

class Api:
    
    def __init__(self):
        self.window = None
        self.model  = 'deepseek-v3.1:671b-cloud'
        self.logger = logging_handler.Logger()
        
        
    def _set_window(self, window: webview.create_window()):
        """Sets current window
        
        Args: 
            window (webview.createwindow): Main window for application"""
        
        self.window = window
        self.logger.log_handler(f"Starting application at {window}", 10, logging_handler.handlerType.PYTHON)
        
    
    def _set_log_level(self, level):
        """Set logging level depending on argv
        
        Args:
            level(int): [10|30]"""
        
        self.logger.set_level(level)
        
    def log(self, log):
        """Prints {log} from script, src dictates which language it is from"""
        
        self.logger.log_handler(f"{log}", 20, logging_handler.handlerType.JS)
        
        
    def close_app(self):
        import sys
        if webview.windows:
            self.logger.log_handler(f"Closing application at {self.window}", 10, logging_handler.handlerType.PYTHON)
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
    
    if use_debug: level = 10
    else: level = 30
    
    api._set_log_level(level=level)
    api._set_window(window=window)
    
    webview.start(debug=use_debug, gui='gtk')
    
        
if __name__ == "__main__":
    
    # Add explanation later
    try:
        command = sys.argv[1]
    except:
        command = ''
        
    match (command):
        case '--debug':
            launch_webview(True)
        case _:
            launch_webview(False)