

window.addEventListener('pywebviewready', async function(e) {
    // Initialize event listeners on startup
    __init_events();
});

function handleUserInput(message) {
    // Handle 
    INPUT_BTN.classList.add('send');

    if (INPUT_TEXT.value == '') { 
        setTimeout(() => { 
            INPUT_BTN.classList.remove('send'); }, 
            100); 
        return; 
    }

    if (!CHATBOX.classList.contains('hasMessage')) {
        CHATBOX.classList.add('hasMessage');
        CHATBOX.textContent = '';
    }

    message_handler('user', message);
    resize_input();

    message_handler('bot', message);

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

async  function bot(msgDiv, message) {

    //pywebview.api.log("Submitted by bot: " + message, 10);

    msgDiv.textContent = 'Processing...';
    msgDiv.classList.add('message', 'bot')
    
    CHATBOX.appendChild(msgDiv)
    INPUT_TEXT.value = '';
    
    await pywebview.api.send(message);

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