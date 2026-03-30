
function resize_input(){
    // Resize text input based on entry
    INPUT_TEXT.style.height = '30px';
    INPUT_TEXT.style.height = `${INPUT_TEXT.scrollHeight + 2}px` ;
}


function scroll_down(){
    // Moves scroll box down to lowest
    CHATBOX.scrollTop = CHATBOX.scrollHeight;
}

function changeSettingsDisplay(button){
    const panelName = button.dataset.panel;
    const templateId = `${panelName}-panel`;
    const template = document.getElementById(templateId);

    const display =  document.getElementById('settings-display');
    const panels = display.querySelectorAll('[class="display"]');
    panels.forEach(panel => {
        panel.style.display = 'none';
    })
    template.style.display = 'block';
}
