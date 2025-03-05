$(document).ready(function () {
  $('#login-personal-form').on('submit', function (form) {
    form.preventDefault();

    const $form = $(this);
    const $btn = $('#btn-personal-login');
    const $spinner = $('.spinner-border');
    const $btnText = $('#login-personal-text');

    $btnText.text('Logging you in...');
    $spinner.show();

    $btn.prop('disabled', true).css({
      'background-color': '#9888c7',
      cursor: 'not-allowed',
    });

    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
      type: 'POST',
      url: '/login',
      data: $form.serialize(),
      dataType: 'json',
      headers: {
        'X-CSRFToken': csrfToken,
      },
      success: function (res) {
        if (res.error === '2fa_required') {
          // Redirect to 2FA verification page
          window.location.href = '/verify-2fa/';
        } else if (res.success) {
          iziToast.success({
            title: 'Success',
            message: res.success,
            position: 'topLeft',
          });

          // Redirect to home page after successful login
          window.location.href = '/home/';
        } else {
          iziToast.error({
            title: 'Error',
            message: res.error || 'An unexpected error occurred.',
            position: 'topLeft',
          });
        }

        $form[0].reset();
        $spinner.hide();
        $btn.prop('disabled', false).css({
          'background-color': '',
          cursor: '',
        });
        $btnText.text('Log In');
      },
      error: function (err) {
        console.log(err);

        iziToast.error({
          title: 'Error',
          message: err.responseJSON.error || 'An unexpected error occurred.',
          position: 'topLeft',
        });

        $form[0].reset();
        $spinner.hide();
        $btn.prop('disabled', false).css({
          'background-color': '',
          cursor: '',
        });
        $btnText.text('Log In');
      },
    });
  });
});
