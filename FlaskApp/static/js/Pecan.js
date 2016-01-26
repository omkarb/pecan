//	import twttr;

$(function(){

var topic = "nba";

twttr.widgets.load();

	  // Load the Visualization API and the piechart package.
	  setTimeout(function(){google.load('visualization', '1', {'callback':'', 'packages':['corechart']})}, 2000);

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart);
      var toDraw;
      var title;
      function setToDraw(dat, name) {
          toDraw = dat;
          title = name;
      }

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Date');
        data.addColumn('number', 'Search Volume');
        data.addRows('toDraw');

        // Set chart options
        var options = {'title':title,
                       'width':800,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }

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

console.log(document.getElementById('twitter-timeline'));
twttr.widgets.createTimeline(
  '691193942780571648',
  document.getElementById('twitter-timeline'),
  {
    width: '15%',
    height: '100%',
    theme: "dark",
    related: 'twitterdev,twitterapi'
  }).then(function (el) {
    console.log("Embedded a timeline.")
  });
});
