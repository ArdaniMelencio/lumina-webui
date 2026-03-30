
function __init_events(e){

    resize_input();

    INPUT_TEXT.addEventListener('input', async function(event) {
        event.preventDefault();

        resize_input();
    });

    INPUT_FORM.addEventListener('submit', async function(event) {
        event.preventDefault();

        handleUserInput(INPUT_TEXT.value);
    })

    SETTINGS_BTN.addEventListener('click', async function(event) {SETTINGS.classList.toggle('toggle'); console.log("Toggled")});

    SETTINGS.querySelectorAll('button[data-panel]').forEach(button => {
        button.addEventListener('click', function(event){
            changeSettingsDisplay(button)
        });
    });

    document.getElementById("checkbox-local").addEventListener('change', function(e) {
  
        const localToggle = document.getElementById("checkbox-local");
        const api = document.getElementById('api-key-input');

        api.disabled = localToggle.checked;
    })

    document.addEventListener('keydown', async function(event) {

        if (event.key == '/' && !INPUT_TEXT.matches(':focus')) {
            event.preventDefault();
            INPUT_TEXT.focus();
        }
        
        if (event.key == 'Escape') {
            INPUT_TEXT.blur();    
            document.getElementById('chat-container').focus();
        }

        if (event.key == 'Enter' && !event.shiftKey) {
            event.preventDefault();
            handleUserInput(INPUT_TEXT.value);
        }

    })

};

