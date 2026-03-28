

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
