function validatePasswords() {
    // Retrieve the values entered by the user in the password and confirm password input fields
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;

    // Access the HTML element that displays the password mismatch error message
    var passwordError = document.getElementById('password-error');

    // Check if the password and confirm password inputs match
    if (password !== confirmPassword) {
        // If passwords do not match, display the error message by setting its display style to 'block'
        passwordError.style.display = 'block';
    } else {
        // If passwords match, hide the error message by setting its display style to 'none'
        passwordError.style.display = 'none';
    }
}


