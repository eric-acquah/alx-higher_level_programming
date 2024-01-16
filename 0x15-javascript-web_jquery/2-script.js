// Listen to click event and change the color of an element
$(function () {
  $('#red_header').on('click', () => {
    $('header').css('color', '#FF0000');
  });
});
