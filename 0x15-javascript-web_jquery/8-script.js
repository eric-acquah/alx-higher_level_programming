//  Fetch data from api and list them in an element

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {

  for (const result of data.results) {
    $('#list_movies').append('<li>' + result['title'] + '</li>');
  }
});
