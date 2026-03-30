"""
Lumina Web UI - Python Backend API
Provides the bridge between the JavaScript frontend and Ollama/API services
"""

import webview, json, time, pathlib, datetime, sys, os
import logging_handler, ollama_handler

class Api:
    """
    Main API class that handles communication between frontend and backend services
    """
    
    def __init__(self):
        """Initialize the API with default settings and handlers"""
        self.window = None
        self.logger = logging_handler.Logger()
        self.ollama = ollama_handler.Api_Handler()
        
        # Default application settings - will be updated from frontend
        self.settings = {
            'model': 'deepseek-v3.1:671b-cloud',
            'api_key': '000', 
            'use_local': False
        }
        
        
    def update_settings(self, new_settings):
        """
        Update multiple settings from frontend and propagate changes to handlers
        
        Args:
            new_settings (dict): Dictionary of setting key-value pairs to update
        """
        self.settings.update(new_settings)
        self.logger.log_handler(f"Settings updated: {new_settings}", 10, logging_handler.handlerType.PYTHON)
        
        # Update Ollama handler with new model and API key configuration
        self.ollama.init(self.settings['model'], self.settings['api_key'])
    
        
    def _set_window(self, window: webview.create_window()):
        """
        Store reference to the main application window
        
        Args: 
            window (webview.create_window): Main window instance for the application
        """
        self.window = window
        self.logger.log_handler(f"Starting application at {window}", 10, logging_handler.handlerType.PYTHON)
        
    
    def _set_log_level(self, level):
        """
        Set the logging level based on command line arguments
        
        Args:
            level (int): Logging level (10 for debug, 30 for normal)
        """
        self.logger.set_level(level)
        
    def log(self, log, logLevel):
        """
        Handle log messages received from JavaScript frontend
        
        Args:
            log (str): The log message content
            logLevel (int): Severity level of the log message
        """
        print(f"[{logLevel}] FROM JS: {log}")
        self.logger.log_handler(f"{log}", logLevel, logging_handler.handlerType.JS)
        
        
    def send(self, message):
        """
        Send user message to the appropriate API client (local Ollama or cloud API)
        
        Args:
            message (str): User input message to process
        """
        reply = ''
        
        # Determine which client to use based on settings
        if self.settings['use_local']:
            chunks = self.ollama.sendMessage(message, self.ollama.local_client)
            
            for chunk in chunks:
                print(chunk['message']['content'], flush=True, end='')
                reply += chunk['message']['content']
        else:
            chunks = self.ollama.sendMessage(message, self.ollama.api_client)
            
            for chunk in chunks:
                print(chunk['message']['content'], flush=True, end='')
                reply += chunk['message']['content']
            
        # Add assistant's response to message history
        self.ollama.addToMessages('assistant', reply)           
        
        
    def close_app(self):
        """Gracefully close the application and cleanup resources"""
        import sys
        if webview.windows:
            self.logger.log_handler(f"Closing application at {self.window}", 10, logging_handler.handlerType.PYTHON)
            webview.windows[0].destroy()
        sys.exit(0)    
        
def launch_webview(use_debug: bool = False):
    """
    Initialize and launch the pywebview application
    
    Args:
        use_debug (bool): Whether to enable debug mode with devtools
    """
    
    # Temporary workaround for graphics rendering issues
    os.environ['LIBGL_ALWAYS_SOFTWARE'] = '0'
    
    print(f"Frontend path: {pathlib.Path.cwd() / 'frontend'}")
    
    # Create API instance and configure window
    api = Api()
    window = webview.create_window(
        'Lumina Web UI',
        '../../frontend/index.html',
        frameless=True,
        easy_drag=True,
        js_api=api,
        min_size=(420, 420)
    )
    
    # Set appropriate log level based on debug mode
    level = 10 if use_debug else 30
    
    api._set_log_level(level=level)
    api._set_window(window=window)
    
    # Start the webview application
    webview.start(debug=use_debug, gui='gtk', storage_path='./data', private_mode=False)

   

if __name__ == "__main__":
    """
    Main entry point for the application
    
    Command line argument handling:
    --debug: Enables debug mode with verbose logging and webview devtools
    (no args): Normal operation with minimal logging
    Example: python api.py --debug
    """
    
    try:
        command = sys.argv[1]
    except:
        command = ''  # No additional arguments provided
        
    # Launch application with appropriate debug settings
    match (command):
        case '--debug':
            launch_webview(use_debug=True)
        case _:
            launch_webview(use_debug=False)