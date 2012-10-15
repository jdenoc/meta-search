/*
Filename:	alerts.js
Version:	6.5.1
This file contains all javascript functions are used throughout the meta-search engine
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

/* *** SHOW/HIDE items *** */
// Shows or hides a block of HTML code
// SOURCE:		http://girlswhogeek.com/tutorials/2007/show-and-hide-elements-with-javascript
function showStuff(id) {
	document.getElementById(id).style.display = 'block';
}
function hideStuff(id) {
	document.getElementById(id).style.display = 'none';
}
/* *** END SHOW/HIDE items *** */

/* *** TOO MANY LINKS *** */
// This function alerts the user that they have entered a value too high or too low for the meta-search engine to request
function too_many(){
	var x=document.engine.total.value
	var num = parseInt(x)
	if (num > 100){
		alert("WARNING!\nToo many results entered.\nMaximum number of results that can be entered is 100.");
		return false;
	}else if(num <= 0){
		alert("WARNING!\nToo few results.\nMinimum number of results that can be entered is 1.");
		return false;
	}
}
/* *** END TOO MANY LINKS *** *

/* *** CHANGE DISPLAY *** */
// This function allows the user to resubmit the search as a different display
// provided there is a query & an appropriate value for the amount of results
function change_display(){
	if (too_many() == false){
		return false;
	}else if(valid_search() == false){
		return false;
	}else{
		document.engine.submit();
	}
}
/* *** END CHANGE DISPLAY */