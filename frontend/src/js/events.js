

function __init_events(e){

    resize_input();

    INPUT_TEXT.addEventListener('input', async function(event) {
        event.preventDefault();

        resize_input();
    });
