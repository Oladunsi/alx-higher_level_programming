const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr
//
$.getJSON(url, function (body) {
  let hello = body.hello;
  $('DIV#hello').text(hello);
});
