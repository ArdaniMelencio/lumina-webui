// Prepares everything when DOM is ready
document.addEventListener('DOMContentLoaded', async function(e) {

    __init_events();
})


function handleUserInput(message) {

    if (INPUT_TEXT.value == '') return;

        if (!CHATBOX.classList.contains('hasMessage')) {
            CHATBOX.classList.add('hasMessage');
            CHATBOX.textContent = '';
        }

    
    message_handler('user', message);
    resize_input();
}

function message_handler(sender, message)  {
        
    msgDiv = document.createElement('div');

    // handle different messages
    switch (sender) {
        case 'user':
            user(msgDiv, message)
            break;
        default: 
            pywebview.api.log("No valid sender", 30)
    }
}

function user(msgDiv, message) {

    pywebview.api.log("Submitted by user: " + message, 10);

    msgDiv.textContent = message;
    msgDiv.classList.add('message', 'user')
    
    CHATBOX.appendChild(msgDiv)
    INPUT_TEXT.value = '';
    
    chatbox.scrollTop = chatbox.scrollHeight;
}