def main():
    """Test logging_handler values"""
    
    from backend.src import logging_handler
    
    # Setup main class
    logger = logging_handler.Logger()
    
    # Set logging level
    logger.set_level(10)
    
    # Check main class
    print(f"Logger: {logger}")
    
    # Check handler types
    print(f"Python handler: {logger.pyHandler}")
    print(f"Js handler: {logger.jsHandler}")
    
    # Check logger types
    print(f"Python logger: {logger.pyLogger}")
    print(f"--Handler - {logger.pyLogger.handlers}")
    print(f"--Level   - {logger.pyLogger.level}")
    
    print("\n")
    
    print(f"Js logger:  {logger.jsLogger}")
    print(f"--Handler - {logger.jsLogger.handlers}")
    print(f"--Level   - {logger.jsLogger.level}")
    
    print("\n")
    
    # Testing output
    testMessage = "Error Message #"
    
    for i in range(1,6):
        logger.log_handler((testMessage + str(i)), i*10, logging_handler.handlerType.TEST)
    
    
if __name__ == "__main__":
    main()