$(document).ready(function () {
  $('#verify-2fa-form').on('submit', function (e) {
    e.preventDefault();

    const $form = $(this);
    const $btn = $form.find('button[type="submit"]');
    const $btnText = $btn.text();

    $btn.text('Verifying...').prop('disable', true);

    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
      type: 'POST',
      url: '/verify-2fa/',
      data: $form.serialize(),
      dataType: 'json',
      headers: {
        'X-CSRFToken': csrfToken,
      },
      success: function (res) {
        if (res.success) {
          window.location.href = res.redirect_url; // Redirect to home page
        } else {
          iziToast.error({
            title: 'Error',
            message: res.error || 'Invalid OTP.',
            position: 'topLeft',
          });
        }
      },
      error: function (err) {
        iziToast.error({
          title: 'Error',
          message: err.responseJSON.error || 'An unexpected error occurred.',
          position: 'topLeft',
        });
      },
      complete: function () {
        $btn.text($btnText).prop('disable', false);
      },
    });
  });
});
