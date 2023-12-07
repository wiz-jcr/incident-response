function sendMessage() {
    var userInput = document.getElementById('user-input');
    var messageContainer = document.getElementById('chat-messages');

    // Get user input
    var userMessage = userInput.value.trim();

    if (userMessage !== '') {
        // Display user message
        var userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user-message';
        userMessageDiv.textContent = userMessage;
        messageContainer.insertBefore(userMessageDiv, messageContainer.firstChild);

        // Clear the input field
        userInput.value = '';

        // Simulate a simple response (you can replace this with actual server communication)
        setTimeout(function() {
            var responseMessageDiv = document.createElement('div');
            responseMessageDiv.className = 'message';
            responseMessageDiv.textContent = 'This is a simple response.';
            messageContainer.appendChild(responseMessageDiv);
            messageContainer.insertBefore(responseMessageDiv, messageContainer.firstChild);

            // Scroll to the bottom to show the latest message
            chatContainer = document.getElementById('chat-container');
            chatContainer.scrollTop = messageContainer.scrollHeight;
        }, 500);
    }
}