

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

    document.addEventListener('keydown', async function(event) {

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
