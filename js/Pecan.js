import twttr;

var topic = "nba";

$(document).ready(function(){

twttr.widgets.load()


/*
Code from Twitter:

Assign a HTML element ID of twitter-wjs to easily identify if the JavaScript file already exists on the page. Exit early if the ID already exists.

Asynchronously load Twitter’s widget JavaScript.

Initialize an asynchronous function queue to hold functions dependent on Twitter’s widgets JavaScript until the script is available.

*/
window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);
 
  t._e = [];
  t.ready = function(f) {
    t._e.push(f);
  };
 
  return t;
}(document, "script", "twitter-wjs"));


/*
Twitter Code to dynamically create a timeline
*/

window.twttr(this,topic,'691193942780571648')

twttr.widgets.createTimeline(
  '691193942780571648',
  document.getElementById('twitter-timeline'),
  {
    width: '15%',
    height: '100%',
    theme="dark",
    related: 'twitterdev,twitterapi'
  }).then(function (el) {
    console.log("Embedded a timeline.")
  });
}