document.addEventListener("DOMContentLoaded", function() {
    var messageInput = document.getElementById("messageInput");

    // Send message when the Enter key is pressed
    messageInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});

function sendMessage() {
    var message = document.getElementById("messageInput").value;
    if (message.trim() === '') {
        return; // Do nothing if the message is empty or only whitespace
    }

    document.getElementById("spinner").style.display = 'block';

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById("chatOutput").innerHTML += '<p>' + response.response + '</p>';
            document.getElementById("spinner").style.display = 'none';
        }
    };
    var data = JSON.stringify({"message": message});
    xhr.send(data);

    // Clear the message input field and set focus back to it
    var messageInput = document.getElementById("messageInput");
    messageInput.value = '';
    messageInput.focus();
}
