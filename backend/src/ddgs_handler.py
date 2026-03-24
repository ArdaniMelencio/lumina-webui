from ddgs import DDGS


class Search_Handler():
    
    def __init__(self):
        self.ddgs = DDGS()
        self.search_engine = 'duckduckgo'
        self.max_results = 5
        self.timeout = 20   # Timeout in seconds
        
    def search(self, query: str) -> []:
        """Search a given query
        
        Args:
            query (str): what to search
            
        Returns:
            [] - Array of search objects"""
        
        # loop to reattempt when search fails
        while True:
            try:
                return self.ddgs.text(
                    query = query,
                    max_results = self.max_results,
                    backend = self.search_engine,
                    timeout = self.timeout
                )
            except Exception as ERR:
                print(ERR)
                
