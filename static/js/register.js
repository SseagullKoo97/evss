$(function () {
    function bindCaptchaBtnClick() {
        $("#captcha-btn").click(function (event) {
            let $this = $(this);
            let email = $("input[name='email']").val();
            if (!email) {
                alert("Please enter your email first!");
                return;
            }
            // Cancel button click event to prevent multiple requests
            $this.off('click');

            // Send AJAX request to the new URL
            $.ajax({
                url: `/auth/send_email_captcha/?email=${encodeURIComponent(email)}`,  // Ensure URL matches your backend route
                method: 'GET',
                success: function(result) {
                    if (result['code'] === 200) {
                        alert("Verification code sent successfully!");
                    } else {
                        alert(result['message'] || "Failed to send verification code.");
                    }
                },
                error: function(error) {
                    console.error("Error:", error);
                    alert("An error occurred while sending the verification code.");
                }
            });

            // Countdown for reactivation of the button
            let countdown = 60;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text('Get CAPTCHA');
                    clearInterval(timer);  // Clear the timer
                    bindCaptchaBtnClick(); // Re-bind the click event
                } else {
                    countdown--;
                    $this.text(countdown + "s");
                }
            }, 1000);
        });
    }

    bindCaptchaBtnClick();
});
