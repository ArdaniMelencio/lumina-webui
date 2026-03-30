// Prepares everything when DOM is ready
document.addEventListener('DOMContentLoaded', async function(e) {

    __init_events();
})

window.addEventListener('pywebviewready', async function(e) {

    Settings.init();
    setSettings();
    
});

function handleUserInput(message) {

    INPUT_BTN.classList.add('send');

    if (INPUT_TEXT.value == '') {
        setTimeout(() => {
            INPUT_BTN.classList.remove('send');
        }, 100);
        return;
    }

    if (!CHATBOX.classList.contains('hasMessage')) {
        CHATBOX.classList.add('hasMessage');
        CHATBOX.textContent = '';
    }

    message_handler('user', message);
    resize_input();

    setTimeout(() => {
        INPUT_BTN.classList.remove('send');
    }, 100);
}

function message_handler(sender, message)  {
        
    msgDiv = document.createElement('div');

    // handle different messages
    switch (sender) {
        case 'user':
            user(msgDiv, message);
            break;
        case 'bot':
            bot(msgDiv, message);
            break;
        default: 
            pywebview.api.log("No valid sender", 30)
    }
}

function bot(msgDiv, message) {

    pywebview.api.log("Submitted by bot: " + message, 10);

    msgDiv.textContent = message;
    msgDiv.classList.add('message', 'bot')
    
    CHATBOX.appendChild(msgDiv)
    INPUT_TEXT.value = '';
    
    chatbox.scrollTop = chatbox.scrollHeight;
}

function user(msgDiv, message) {

    pywebview.api.log("Submitted by user: " + message, 10);

    msgDiv.textContent = message;
    msgDiv.classList.add('message', 'user');

    CHATBOX.appendChild(msgDiv)
    INPUT_TEXT.value = '';
    
    chatbox.scrollTop = chatbox.scrollHeight;
}