const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
//
$.get(url, (data) => {
  for (const movie of  body.results) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  }
});
