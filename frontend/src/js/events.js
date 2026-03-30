
function __init_events(e){
    // Initialize input textarea sizing on page load
    resize_input();

    // Auto-resize textarea as user types (expands until max height, then CSS handles overflow)
    INPUT_TEXT.addEventListener('input', async function(event) {
        event.preventDefault();
        resize_input();
    }); 

    // Handle chat message submission
    INPUT_FORM.addEventListener('submit', async function(event) {
        event.preventDefault();
        handleUserInput(INPUT_TEXT.value);
    });



    // Toggle settings panel visibility
    SETTINGS_BTN.addEventListener('click', async function(event) {
        SETTINGS.classList.toggle('toggle'); 
        console.log("Toggled");
    });

    // Settings panel navigation - switch between different settings sections
    SETTINGS.querySelectorAll('button[data-panel]').forEach(button => {
        button.addEventListener('click', function(event) {
            changeSettingsDisplay(button); // Switches to panel specified by data-panel attribute (General/Themes/Advanced)
        });
    });

    // Local mode toggle - disable API key input when using local models
    document.getElementById("checkbox-local").addEventListener('change', function(e) {
        const localToggle = document.getElementById("checkbox-local");
        const api = document.getElementById('api-key-input');
        
        // API key input disabled for local mode, enabled for online mode
        api.disabled = localToggle.checked;
    });

    // Global keyboard shortcuts
    document.addEventListener('keydown', async function(event) {
        // Focus input with '/' key
        if (event.key == '/' && !INPUT_TEXT.matches(':focus')) {
            event.preventDefault();
            INPUT_TEXT.focus();
        }
        
        // Escape key clears input focus
        if (event.key == 'Escape') {
            INPUT_TEXT.blur();    
            document.getElementById('chat-container').focus();
        }

        // Submit message with Enter (Shift+Enter for new line)
        if (event.key == 'Enter' && !event.shiftKey) {
            event.preventDefault();
            handleUserInput(INPUT_TEXT.value);
        }
    });
};

