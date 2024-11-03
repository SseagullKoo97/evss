// When the document (HTML page) is fully loaded and ready, execute the following function
$(document).ready(function () {

    // Attach an 'input' event listener to the input field with the id 'dob' (date of birth field)
    $('#dob').on('input', function (e) {

        // Get the current value of the 'dob' input field
        var input = $(this).val();

        // Remove all non-numeric characters from the input (only keep numbers)
        var formattedDate = input.replace(/[^0-9]/g, '');

        // If the length of the numeric input is 2 or more characters, insert a '/' after the second character (to format it as 'dd/')
        if (formattedDate.length >= 2) {
            formattedDate = formattedDate.slice(0, 2) + '/' + formattedDate.slice(2);
        }

        // If the length of the formatted input is 5 or more characters, insert another '/' after the fifth character (to format it as 'dd/mm/yyyy')
        if (formattedDate.length >= 5) {
            formattedDate = formattedDate.slice(0, 5) + '/' + formattedDate.slice(5, 9);
        }

        // Set the value of the 'dob' input field to the newly formatted date
        $(this).val(formattedDate);
    });
});

