$(document).ready(function () {
  $('#personal-form').on('submit', function (form) {
    form.preventDefault();
    const $btnText = $('#btn-text');
    const $spinner = $('.spinner-border');
    const $btnPersonal = $('#btn-personal button');

    $btnText.text('Loading');
    $spinner.show();
    $btnPersonal.attr('disabled', true).css({
      'background-color': 'rgba(145, 113, 242, 0.83)',
      cursor: 'not-allowed',
    });

    const $entireForm = $(this);
    // console.log($entireForm.serializeArray());
    // console.log($entireForm.serialize());
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
      type: 'POST',
      url: '/register',
      datatype: 'json',
      data: $entireForm.serialize(),
      success: function (res) {
        console.log('registered successfully');
        // console.log(res);

        iziToast.success({
          title: 'Success',
          message: res.success,
          position: 'topLeft',
        });

        setTimeout(function () {
          window.location = '/verify-email';
        }, 2000);
      },
      error: function (err) {
        console.log(csrfToken);
        // console.log('There was an error registering');
        $btnText.text('Register Now');
        $spinner.hide();
        $btnPersonal.prop('disable', false).css({
          'background-color': '',
          cursor: '',
        });
        console.log(err);

        iziToast.error({
          title: 'Error',
          message: err.responseJSON.error,
          position: 'topLeft',
        });
      },
    });
  });

  // Business logic start here

  $('#business-form').on('submit', function (form) {
    form.preventDefault();
    const $btnText = $('#btn-business-text');
    const $spinner = $('.spinner-border');
    const $btnPersonal = $('#btn-business button');

    $btnText.text('Loading');
    $spinner.show();
    $btnPersonal.attr('disabled', true).css({
      'background-color': 'rgba(145, 113, 242, 0.83)',
      cursor: 'not-allowed',
    });

    const $entireForm = $(this);
    // console.log($entireForm.serializeArray());
    // console.log($entireForm.serialize());

    $.ajax({
      type: 'POST',
      url: '/register',
      datatype: 'json',
      data: $entireForm.serialize(),
      headers: {
        'X-CSRFTOKEN': csrfToken,
      },
      success: function (res) {
        console.log('registered successfully');
        // console.log(res);

        iziToast.success({
          title: 'Success',
          message: res.success,
          position: 'topLeft',
        });
      },
      error: function (err) {
        // console.log('There was an error registering');
        $btnText.text('Register Now');
        $spinner.hide();
        $btnPersonal.prop('disable', false).css({
          'background-color': '',
          cursor: '',
        });
        console.log(err);

        iziToast.error({
          title: 'Error',
          message: err.responseJSON.error,
          position: 'topLeft',
        });
      },
    });
  });
});
