def main():
    
    model = 'deepseek-v3.1:671b-cloud'
    local_model = 'gemma3:270m'

    print("Importing ollama_handler.py...")
    from backend.src import ollama_handler
    from pathlib import Path

    print("Trying to open API_KEY file")
    if Path('API_KEY').exists():
        with open('API_KEY' , 'r') as file:
            API_KEY = file.read()
            print(f"Opened succesfully: {API_KEY[0:5]}...")
    else:
        API_KEY = ''
        print("File not found")
    
    api = ollama_handler.Api_Handler()

    print("Initiating new handler item")
    api.init(model, API_KEY)
    
    print("\n\nAttempting online message")
    #attemptMessage(api, model, ollama_handler.utilClient.online)
    
    print("\n\nAttempting local message")
    attemptMessage(api, local_model, ollama_handler.utilClient.local)
    

def attemptMessage(api, model, mode: api.utilClient):
    
    api.model = model
    
    chunks = api.sendMessage("Why is the sky blue? (short answer)", mode)
    
    msg = ''
    
    for chunk in chunks:
        print(chunk['message']['content'], flush=True, end='')
        api.current_tokens += 1
        msg += chunk['message']['content']
    else: 
        api.total_tokens += api.current_tokens
        print(chunks)
        print(f"Current tokens: {api.current_tokens}")
        print(f"Total tokens: {api.total_tokens}")
    
if __name__ == "__main__":
    main()
