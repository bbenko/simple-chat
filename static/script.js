document.addEventListener("DOMContentLoaded", function() {
    const messageInput = document.getElementById("messageInput");
    messageInput.focus();  // Set focus on the message input

    // Send message when the Enter key is pressed
    messageInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});

function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const sendButton = document.getElementById("sendButton");
    const spinner = document.getElementById("spinner");
    const message = messageInput.value;

    if (message.trim() === '') {
        return; // Do nothing if the message is empty
    }

    appendMessage(message, 'user-message'); // Display the user sent message in the chat

    // Clear input, hide send button, and show spinner
    messageInput.value = '';
    sendButton.style.display = 'none';
    spinner.style.display = 'inline-block';

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            // Hide spinner, show and enable send button
            spinner.style.display = 'none';
            sendButton.style.display = 'inline-block';

            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                appendMessage(response.response, 'server-response'); // Display server response
            }
        }
    };
    const data = JSON.stringify({"message": message});
    xhr.send(data);
}

function appendMessage(text, className) {
    const chatBox = document.getElementById("chatBox");
    const messageElement = document.createElement("p");
    messageElement.textContent = text;
    messageElement.className = className;
    chatBox.appendChild(messageElement);

    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}
