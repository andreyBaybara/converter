
function cookie_(cook) {
  var data = document.cookie.split('=');
  var index = data.indexOf(cook);
  return data[index+1]
}
function convert_data() {
  var val  = $('#convert_input').val();
  if(val == ''){
    data_ = { 'data': '0' };
  } else {
    data_ = { 'data': val };
  }
  console.log(data_);
  $.ajax({
     url: "/convert",
     type: 'POST',
     data: data_,
     dataType: 'json',
     success: function (json) {
         if (json.result) {
            console.log(json.result);
            $('#converted_input').val(json.result);
         }
     },
     error: function (xhr, ajaxOptions, thrownError) {
      console.log(xhr.status);
      console.log(thrownError);
    }
   });
}
$(window).on('load', function() {
  $.ajaxSetup({
        headers: { "X-CSRFToken": cookie_('csrftoken') }
    });
  data_ = {'data':'None'};
  //$('#convert_btn').on('click', convert_data);
  $('#convert_input').on('keyup', convert_data);
});
