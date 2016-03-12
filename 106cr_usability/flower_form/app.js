$(document).ready(function(){
  $('#cp_sen:checkbox').change(function(){
    if ($('#cp_sen').is(':checked')) {
      $('#rec_name').val($('#sen_name').val());
      $('#rec_phone').val($('#sen_phone').val());
      $('#rec_addr').val($('#sen_addr').val());
    } else {
      $('#rec_name').val('');
      $('#rec_phone').val('');
      $('#rec_addr').val('');
    }
  });

  $('#cp_rec:checkbox').change(function(){
    if ($('#cp_rec').is(':checked')) {
      $('#sen_name').val($('#rec_name').val());
      $('#sen_phone').val($('#rec_phone').val());
      $('#sen_addr').val($('#rec_addr').val());
    } else {
      $('#sen_name').val('');
      $('#sen_phone').val('');
      $('#sen_addr').val('');
    }
  });
  $('#other:checkbox').change(function(){
    if ($('#other:checkbox').is(':checked')) {
      $('#other-reveal').slideDown();
    } else {
      $('#other-reveal').slideUp();
    }
  });
  var modal = $('.modal');
  var order_btn = $('#order_btn');
  var overlay = $('.outer-wrapper');
  var close_modal = $('#close_modal');
  var pay_1 = $('#credit');
  var pay_2 = $('#paypal');
  order_btn.click( function(){
    modal.css('display', 'block');
    overlay.css('display', 'block');
  });
  close_modal.click( function(){
    modal.css('display', 'none');
    overlay.css('display', 'none');
  });
  $('#credit:radio').change(function(){
    if ($('#credit:radio').is(':checked')) {
      $('.option2').slideUp();
      $('.option1').slideDown();
    }
  });
  $('#paypal:radio').change(function(){
    if ($('#paypal:radio').is(':checked')) {
      $('.option1').slideUp();
      $('.option2').slideDown();
    }
  });

});
