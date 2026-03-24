import logging, logging.handlers, os
from enum import Enum
from datetime import datetime

RED = '\033[91m'
YELLOW = '\033[93m'  
GRAY = '\033[90m'
RESET = '\033[0m'

class Logger():
    """A logging import handler class
    
    Attributes:
        log_dir (PATH): Location for the log folder
    
    Methods:
        set_level (level): Sets the log level all the loggers
        log_handler (msg, lvl, hlr): Handles incoming log messages"""
    
    def __init__(self):
        
        # Log dir
        self.log_dir    = os.path.join(os.path.dirname(__file__), '../../logs')
        
        # Setup python logger
        self.pyHandler  = logging.handlers.RotatingFileHandler(os.path.join(self.log_dir, 'app.py.log'), maxBytes=10_000_000, backupCount=5)
        self.pyLogger   = logging.getLogger('py.log')
        self.pyLogger.addHandler(self.pyHandler)
        
        # Setup js logger
        self.jsHandler  = logging.handlers.RotatingFileHandler(os.path.join(self.log_dir, 'app.js.log'), maxBytes=10_000_000, backupCount=5)
        self.jsLogger   = logging.getLogger('js.log')
        self.jsLogger.addHandler(self.jsHandler)
        
        
    def set_level(self, level):
        """Set logging level
        
        Args:
            level (int): [10|30]"""
        
        if level == 10:
            self.pyLogger.setLevel(logging.DEBUG)
            self.jsLogger.setLevel(logging.DEBUG)
        else:
            self.pyLogger.setLevel(logging.WARNING)
            self.jsLogger.setLevel(logging.WARNING)
        
    def log_handler(self, message, level, handler):
        """Handles incomming log messages
        
        Args:
            message (str): Log message
            level (int): Log level
            handler (handlerType): [python|javascript]"""
        
        if handler == handlerType.PYTHON:
            self._log_python(message, level)
        elif handler == handlerType.JS:
            self._log_js(message, level)
        elif handler == handlerType.TEST:
            print(f"Received test message: {message} ")
            print(f"|--Level   - {level}")
            print(f"---Handler - {handler}")
        
    
    
    def _log_python(self, message, level):
        """Logs into python logs"""
        
        match (level):
            case 10:
                self.pyLogger.debug(f"[{datetime.now()}] DEBUG: {message}")
            case 20:
                self.pyLogger.info(f"[{datetime.now()}] INFO: {message}")
            case 30:
                self.pyLogger.warning(f"[{datetime.now()}] WARNING: {message}")
            case 40:
                self.pyLogger.error(f"[{datetime.now()}] ERROR: {message}")
            case 50:
                self.pyLogger.critical(f"[{datetime.now()}] CRITICAL: {message}")

    
    def _log_js(self, message, level):
        """Logs into javascript logs"""
        
        match (level):
            case 10:
                self.jsLogger.debug(f"[{datetime.now()}] DEBUG: {message}")
            case 20:
                self.jsLogger.info(f"[{datetime.now()}] INFO: {message}")
            case 30:
                self.jsLogger.warning(f"[{datetime.now()}] WARNING: {message}")
            case 40:
                self.jsLogger.error(f"[{datetime.now()}] ERROR: {message}")
            case 50:
                self.jsLogger.critical(f"[{datetime.now()}] CRITICAL: {message}")

    
    
class handlerType(str, Enum):
    PYTHON  = 'python'
    JS      = 'javascript'
    TEST    = 'test'