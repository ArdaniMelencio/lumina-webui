from backend.src import ddgs_handler

def main():
    searcher = ddgs_handler.Search_Handler()
    
    results = searcher.search("Who is pewdiepie?")    
    print(results)


if __name__ == "__main__":
    main()