// Loading script just in time to fetch data from api

document.addEventListener('DOMContentLoaded', () => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('#hello').text(data.hello);
  });
});
