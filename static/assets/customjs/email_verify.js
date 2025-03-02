// console.log('inside email_verify js');
$(document).ready(function () {
  $('#verify-form').on('submit', function (e) {
    e.preventDefault();
    const $form = $(this);
    const $btn = $('#btn-verify');
    const $spinner = $('.spinner-border');
    const $btnText = $('#verify-text');

    $btnText.text('Verifying...');
    $spinner.show();

    console.log('inside email_verify js');
    console.log($btn);

    $btn.prop('disabled', true).css({
      'background-color': '#9888c7',
      cursor: 'not-allowed',
    });

    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
      type: 'POST',
      url: '/verify-email',
      data: $form.serialize(),
      dataType: 'json',
      headers: {
        X_CSRFToken: csrfToken,
      },
      success: function (res) {
        iziToast.success({
          title: 'Success',
          message: res.success,
          position: 'topLeft',
        });

        $form[0].reset();
        $spinner.hide();
        $btn.prop('disable', false).css({
          'background-color': '',
          'background-color': '',
        });
        $btnText.text('Verify Now');
      },
      error: function (err) {
        iziToast.error({
          title: 'Error',
          message: err.responseJSON.error,
          position: 'topLeft',
        });

        $form[0].reset();
        $spinner.hide();
        $btn.prop('disable', false).css({
          'background-color': '',
          'background-color': '',
        });
        $btnText.text('Verify Now');
      },
    });
  });
});
