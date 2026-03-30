import ollama
#from transformers import AutoTokenize

class Api_Handler():
    
    def __init__(self):
        self.model = None
        self.api_key = None
        self.messages = []
        
        self.local_client = None
        self.api_client = None
        
        self.current_tokens = 0
        self.total_tokens = 0
        self.tokenizer = None

    def get_models(self):
        pass
    
    
    def init(self, model: str, api_key: str):
        """Create a new handler"""
        
        self.model = model
        
        if api_key != None:
            self.api_key = api_key
            print(api_key)
        
        #self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
            
        self.getClient()
        
            
    def getClient(self):
        """Creates two client objects, one for local usage, and one for API if available"""
        
        self.local_client = ollama.Client()
        
        if self.api_key != '' or self.api_key != '000':
            self.api_client = ollama.Client(
                host = "https://ollama.com",
                headers = {'Authorization': 'Bearer ' + self.api_key}
            )
        
            
    def sendMessage(self, message, client: utilClient) -> stream:
        """Send a query to the selected client"""
        
        self.addToMessages('user', message)
        #self.total_tokens = self._tokenize(message)
        
        
        fullMsg = ''
        cli = self.checkUtil(client)
        self.current_tokens = 0
        
        return client.chat(
            model = self.model,
            messages = self.messages,
            stream = True
        )
            
        
    def addToMessages(self, role, message):
        
        self.messages.append({
            'role' : role,
            'content':message
        })
    
    
    def _tokenize(self, message) -> int:
        """Returns int of tokens"""
        
        return self.tokenizer.tokenize(message)

    
    def checkUtil(self, client: utilClient):
        if client == utilClient.local:
            return self.local_client
        elif client == utilClient.online:
            return self.api_client
        
from enum import Enum
class utilClient(str, Enum):
    local = 'local'
    online = 'online'