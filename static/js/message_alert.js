// Function to show an alert if there's an error message
window.onload = function() {
    var message = document.getElementById("error-message");
    if (message) {
        alert(message.innerText); // Show an alert popup with the error message
    }
}
