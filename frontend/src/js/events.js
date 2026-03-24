INPUT_TEXT.addEventListener('input', async function(event) {
    event.preventDefault();

    // Resize text input based on entry
    INPUT_TEXT.style.height = '30px';
    INPUT_TEXT.style.height = `${INPUT_TEXT.scrollHeight}px`;
});

INPUT_FORM.addEventListener('submit', async function(event) {
    event.preventDefault();

    // Sends to pywebview log for testing
    pywebview.api.log("Submitted by user: " + INPUT_TEXT.value.trim())
    INPUT_TEXT.value = ''
})