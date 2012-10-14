/*
Filename:	alerts.js
Version:	5.7

 */

/* *** GOODBYE *** */
// function that will run anytime user leaves page via a link on front page
function goodbye(){
	alert("Sorry to see you leave!");
}
/* *** END GOODBYE *** */

/* *** Search Validation *** */
// function will warn the user if they haven't entered anything into the search box
// code-source:	http://www.w3schools.com/JS/js_form_validation.asp
function valid_search(){
	var x=document.forms["engine"]["search"].value
	if (x==null || x==""){
		alert("\t\tWARNING!\nYou haven't searched for anything");
		return false;
	}
}
/* *** END Search Validation *** */

/* *** PAGE OPEN CONFIRMATION *** */
/*	var disclaim = "Disclaimer:\n"+
			"This page has been developed as part of a MSc. Computer Science course work & therefore academic in basis.\n"+
			"All rights & trademarks are reserved by those that may appear in this site.\n"+
			"Please click on OK to continue loading the Meta-Search Engine, or CANCEL to be directed to the DuckDuckGo site.";

	var answer = confirm(disclaim);
	if (!answer){
		goodbye();
		window.location="http://www.duckduckgo.com/";
	}*/
/* *** END PAGE OPEN CONFIRMATION *** */

/* *** SHOW/HIDE items *** */
function showStuff(id) {
	document.getElementById(id).style.display = 'block';
}
function hideStuff(id) {
	document.getElementById(id).style.display = 'none';
}
/* *** END SHOW/HIDE items *** */


/* *** DEAD LINK *** */
// This script prompts a user to confirm that they wish to continue to a webpage & that they have been warned that the webpage may not exist
function dead_link(){
	var link_warn = "&#07;WARNING!!!\\nAn error occured when validating the page you are about to access. It may no longer be active.\\nClick OK to continue anyway or Cancel to remain.";
	var answer = confirm(link_warn);
	if (answer){
		alert("You were warned!");
	}else{
		return false;
	}
}
/* *** END DEAD LINK *** */

/* *** TOO MANY LINKS *** */
// This function alerts the user that they have entered a value too high or too low for the meta-search engine to request
function too_many(){
	var x=document.engine.total.value
	var num = parseInt(x)
	if (num > 100){
		alert("WARNING!\nToo many results");
		return false;
	}else if(num <= 0){
		alert("WARNING!\nToo few results");
		return false;
	}
}
/* *** END TOO MANY LINKS *** */












// SOURCE:	http://andylangton.co.uk/articles/javascript/jquery-show-hide-multiple-elements/
// this tells jquery to run the function below once the DOM is ready
$(document).ready(function() {

	// choose text for the show/hide link - can contain HTML (e.g. an image)
	var showText='Show';	//&#9660;
	var hideText='Hide';	//&#9650;
	// initialise the visibility check
	var is_visible = false;

	// append show/hide links to the element directly preceding the element with a class of "toggle"
	$('.toggle').prev().append(' (<a href="#" class="toggleLink">'+showText+'</a>)');

	// hide all of the elements with a class of 'toggle'
	$('.toggle').hide();

	// capture clicks on the toggle links
	$('a.toggleLink').click(function() {

		// switch visibility
		is_visible = !is_visible;

		// change the link depending on whether the element is shown or hidden
		$(this).html( (!is_visible) ? showText : hideText);

		// toggle the display - uncomment the next line for a basic "accordion" style
		//$('.toggle').hide();$('a.toggleLink').html(showText);
		$(this).parent().next('.toggle').toggle('slow');

		// return false so any link destination is not followed
		return false;

	});
});
