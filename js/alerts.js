/*
Filename:	alerts.js
Version:	6.2

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
// SOURCE:		http://girlswhogeek.com/tutorials/2007/show-and-hide-elements-with-javascript
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
/* *** END TOO MANY LINKS *** *

/* *** CHANGE DISPLAY *** */
// This function allows the user to resubmit the search as a different display
function change_display(){
	document.engine.submit();
}
/* *** END CHANGE DISPLAY */