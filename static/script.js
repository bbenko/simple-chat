document.addEventListener("DOMContentLoaded", function() {
    var messageInput = document.getElementById("messageInput");

    // Set focus on the message input after page load
    messageInput.focus();

    // Send message when the Enter key is pressed
    messageInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});

function sendMessage() {
    var messageInput = document.getElementById("messageInput");
    var sendButton = document.getElementById("sendButton");
    var spinner = document.getElementById("spinner");
    var message = messageInput.value;

    if (message.trim() === '') {
        return; // Do nothing if the message is empty
    }

    appendMessage(message, 'message'); // Display the sent message in the chat

    // Clear input, hide send button, and show spinner
    messageInput.value = '';
    sendButton.style.display = 'none';
    spinner.style.display = 'inline-block';

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            // Hide spinner, show and enable send button
            spinner.style.display = 'none';
            sendButton.style.display = 'inline-block';

            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                displayChatResponse(response.response); // Display server's response
            }
        }
    };
    var data = JSON.stringify({"message": message});
    xhr.send(data);
}


function displayChatResponse(responseMessage) {
    appendMessage(responseMessage, 'server-response'); // Display server response
}

function appendMessage(text, className) {
    const chatOutput = document.getElementById("chatOutput");
    const messageElement = document.createElement("p");
    messageElement.textContent = text;
    messageElement.className = className;
    chatOutput.appendChild(messageElement);

    chatOutput.scrollTop = chatOutput.scrollHeight; // Scroll to the latest message
}
