function __init_events(e){
    // Initialize input textarea sizing on page load
    resize_input();
    pywebview.api.log("Input textarea initialized", 10);

    // Initialize settings on function call
    Settings.init();
    setSettings();
    pywebview.api.log("Settings initialized", 10);

    // Auto-resize textarea as user types
    INPUT_TEXT.addEventListener('input', async function(event) {
        event.preventDefault();
        resize_input();
    }); 

    // Handle chat message submission
    INPUT_FORM.addEventListener('submit', async function(event) {
        event.preventDefault();
        pywebview.api.log("Message submission triggered", 10);
        handleUserInput(INPUT_TEXT.value);
    });

    // Toggle settings panel visibility
    SETTINGS_BTN.addEventListener('click', async function(event) {
        SETTINGS.classList.toggle('toggle');
        const isVisible = SETTINGS.classList.contains('toggle');
        pywebview.api.log(`Settings panel ${isVisible ? 'opened' : 'closed'}`, 10);
    });

    // Settings panel navigation
    SETTINGS.querySelectorAll('button[data-panel]').forEach(button => {
        button.addEventListener('click', function(event) {
            changeSettingsDisplay(button);
            pywebview.api.log(`Switched to ${button.dataset.panel} settings panel`, 10);
        });
    });

    // Local mode toggle
    document.getElementById("checkbox-local").addEventListener('change', function(e) {
        const localToggle = document.getElementById("checkbox-local");
        const api = document.getElementById('api-key-input');
        
        api.disabled = localToggle.checked;
        pywebview.api.log(`Local mode ${localToggle.checked ? 'enabled' : 'disabled'}`, 10);
    });

    // Global keyboard shortcuts
    document.addEventListener('keydown', async function(event) {
        // Focus input with '/' key
        if (event.key == '/' && !INPUT_TEXT.matches(':focus')) {
            event.preventDefault();
            INPUT_TEXT.focus();
            pywebview.api.log("Input focused with '/' key", 20);
        }
        
        // Escape key clears input focus
        if (event.key == 'Escape') {
            INPUT_TEXT.blur();    
            document.getElementById('chat-container').focus();
            pywebview.api.log("Input focus cleared with Escape key", 20);
        }

        // Submit message with Enter (Shift+Enter for new line)
        if (event.key == 'Enter' && !event.shiftKey) {
            event.preventDefault();
            pywebview.api.log("Message submitted with Enter key", 10);
            handleUserInput(INPUT_TEXT.value);
        }
    });
    
    pywebview.api.log("All event listeners initialized successfully", 10);
};