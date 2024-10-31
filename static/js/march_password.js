 function checkPasswordMatch() {
        // Get the password and confirm password fields
        var password = document.getElementById('password').value;
        var confirmPassword = document.getElementById('confirm_password').value;

        // Get the password mismatch warning div
        var passwordMismatchWarning = document.getElementById('password-mismatch');

        // Check if the passwords match and have the same length
        if (password === confirmPassword && password.length === confirmPassword.length) {
            passwordMismatchWarning.style.display = 'none'; // Hide the warning
        } else {
            passwordMismatchWarning.style.display = 'block'; // Show the warning
        }
    }
