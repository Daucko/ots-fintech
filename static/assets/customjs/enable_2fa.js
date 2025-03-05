// $(document).ready(function () {
//   $('#enable-2fa-button').click(function () {
//     $.ajax({
//       url: '/enable-2fa/',
//       method: 'POST',
//       headers: {
//         'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(),
//       },
//       success: function (data) {
//         console.log('Full Response:', data); // Debugging log

//         if (data.qr_code) {
//           $('#qr-code-container').show();
//           $('#qr-code').attr('src', data.qr_code); // Set QR code image

//           iziToast.success({
//             title: 'Success',
//             message: data.message,
//             position: 'topLeft',
//           });
//         } else {
//           $('#error-message').text('An unexpected error occurred.');
//         }
//       },
//       error: function (xhr, status, error) {
//         console.log('AJAX Error:', xhr.responseText);
//         $('#error-message').text('An error occurred while enabling 2FA.');
//       },
//     });
//   });
// });

$(document).ready(function () {
  $('#enable-2fa-form').submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    $.ajax({
      url: '/enable-2fa/',
      method: 'POST',
      data: $(this).serialize(), // Serialize form data, including CSRF token
      success: function (data) {
        console.log('Full Response:', data);

        if (data.qr_code) {
          $('#qr-code-container').show();
          $('#qr-code').attr('src', data.qr_code);

          iziToast.success({
            title: 'Success',
            message: data.message,
            position: 'topLeft',
          });
        } else {
          $('#error-message').text('An unexpected error occurred.');
        }
      },
      error: function (xhr, status, error) {
        console.log('AJAX Error:', xhr.responseText);
        $('#error-message').text('An error occurred while enabling 2FA.');
      },
    });
  });
});
