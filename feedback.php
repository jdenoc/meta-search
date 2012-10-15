<?php
// Filename:	feedback.php
// Version:		6.5
// This file is a feedback form that is used to retrieve details on user experience of the meta-search engine
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<script type="text/javascript" src="js/alerts.js"></script>
<link rel="stylesheet" href="css/feedB.css" />
<link rel="icon" href="imgs/icons/meta.ico" type="image/x-icon" />
<title>Feedback & Evaluation</title>
</head>

<body><div id="container">
<div id="opening_address">
	<h1>Meta-Search Feedback & Evaluation</h1>

	<p>Thank you for taking the time to fill out this feedback/evaluation form.</p>
	<p>With your assistance I will be able to retrieve some very useful information on how my engine has performed when used by the average user.</p>
	<p>Please note: all fields marked with a <span class="important">*</span> must be filled out.</p>
	<hr/>
	<br/>
</div><div id="feed_form">
	<?php if (!empty($_POST["Submit"])){
		$error=array();

// Error Checking & Messaging
		// (Q1) 
		if (empty($_POST['engine'])){
			$error['engine']='Please Answer Question 1';
		}else if($_POST['engine']=='Other'){
			if(empty($_POST['engine_other'])){
				$error['engine_other'] = 'Please enter a search engine name';
			}else{
				$_POST['engine_other'] = trim($_POST['engine_other']);
			}
		}
		// (Q2)
		if (empty($_POST['result_quality'])){
			$error['result_quality'] = 'Please choose a value for Q.2';
		}
		// (Q3)
		if (empty($_POST['easy_to_use'])){
			$error['easy_to_use'] = 'Please choose a value for Q.3';
		}
		// (Q4)
		if (empty($_POST['results_presented'])){
			$error['result_presented'] = 'Please choose a value for Q.4';
		}
		// (Q5)
		if (empty($_POST['speed'])){
			$error['speed'] = 'Please choose a value for Q.5';
		}
		// (Q6)
		if (empty($_POST['make_default'])){
			$error['make_default'] = 'Please choose a value for Q.6';
		}
		// (Q7)
		if (empty($_POST['clustering'])){
			$error['clustering'] = 'Please choose a value for Q.7';
		}
		// (Q8)
		if (empty($_POST['display'])){
			$error['display'] = 'Please choose a value for Q.8';
		}
		// (Q9)
		if (empty($_POST['aggrigation'])){
			$error['aggrigation'] = 'Please choose a value for Q.9';
		}
		// (Q10)
		if (empty($_POST['pre-pro'])){
			$error['pre-pro'] = 'Please choose a value for Q.10';
		}
		// (Q11)
		if (empty($_POST['num_results'])){
			$error['num_results'] = 'Please choose a value for Q.11';
		}
		// (Age Group)
		if (empty($_POST['age'])){
			$error['age'] = 'Please choose an age group from the drop-down menu';
		}
		// (Gender)
		if (empty($_POST['sex'])){
			$error['sex'] = 'Please choose a Gender';
		}
		// (Name)
		if (!empty($_POST['name'])){
			$_POST['name'] = trim($_POST['name']);
		}
		// (Errors/Problems discovered)
		if (!empty($_POST['probs'])){
			$_POST['probs'] = trim($_POST['probs']);
		}
		// (Additional Comments)
		if (!empty($_POST['comments'])){
			$_POST['comments'] = trim($_POST['comments']);
		}
		// if no errors, then send email
		if(!$error){
			$ToEmail = '10972081@ucdconnect.ie'; 
			$EmailSubject = 'Feedback Form'; 
			$mailheader = "From: meta-search\r\n"; 
			$mailheader .= "Content-type: text/html; charset=iso-8859-1\r\n"; 
			$MESSAGE_BODY = "Name: ".$_POST["name"]."<br/>"; 
			$MESSAGE_BODY .= "Age: ".$_POST["age"]."<br/>";
			$MESSAGE_BODY .= "Gender: ".$_POST["sex"]."<br/>";
			$MESSAGE_BODY .= "Q1. : ".$_POST["engine"]." - ".$_POST["engine_other"]."<br/>";
			$MESSAGE_BODY .= "Q2. : ".$_POST["result_quality"]."<br/>";
			$MESSAGE_BODY .= "Q3. : ".$_POST["easy_to_use"]."<br/>";
			$MESSAGE_BODY .= "Q4. : ".$_POST["results_presented"]."<br/>";
			$MESSAGE_BODY .= "Q5. : ".$_POST["speed"]."<br/>";
			$MESSAGE_BODY .= "Q6. : ".$_POST["make_default"]."<br/>";
			$MESSAGE_BODY .= "Q7. : ".$_POST["clustering"]."<br/>";
			$MESSAGE_BODY .= "Q8. : ".$_POST["display"]."<br/>";
			$MESSAGE_BODY .= "Q9. : ".$_POST["aggrigation"]."<br/>";
			$MESSAGE_BODY .= "Q10. : ".$_POST["pre-pro"]."<br/>";
			$MESSAGE_BODY .= "Q11. : ".$_POST["num_results"]."<br/>";
			$MESSAGE_BODY .= "Errors/Problems. : ".$_POST["probs"]."<br/>";
			$MESSAGE_BODY .= "Comments: ".nl2br($_POST["comments"])."<br>"; 
			mail($ToEmail, $EmailSubject, $MESSAGE_BODY, $mailheader) or die ("Failure");?>
			<meta HTTP-EQUIV="REFRESH" content="0; url=sent.html">
		<?php }
	}
	// Displays Error messages (if any)
	if (isset($error)) {
		echo "<ul>";
		foreach ($error as $alert) {
			echo "<li class='important'>".$alert."</li>\n";
		}
		echo '</ul>';
	}?>

	<form action="feedback.php" method="post" name="feedback">
	<table border="0"><tr>
		<td colspan="10">
			1.&nbsp;&nbsp;&nbsp;Which search engine do you normally use?
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td><input type="radio" name="engine" value="google" <?php if (isset($_POST['engine']) && $_POST['engine'] == 'google'){ echo 'checked'; } ?> onclick="hideStuff('more_engines')" />Google</td>
		<td><input type="radio" name="engine" value="Bing" <?php if (isset($_POST['engine']) && $_POST['engine'] == 'Bing'){ echo 'checked'; } ?> onclick="hideStuff('more_engines')" />Bing</td>
		<td><input type="radio" name="engine" value="Yahoo" <?php if (isset($_POST['engine']) && $_POST['engine'] == 'Yahoo'){ echo 'checked'; } ?> onclick="hideStuff('more_engines')" />Yahoo</td>
		<td><input type="radio" name="engine" value="Other" <?php if (isset($_POST['engine']) && $_POST['engine'] == 'Other'){ echo 'checked'; } ?> onclick="showStuff('more_engines')" />Other</td>
	</tr><tr>
		<td colspan="3">&nbsp;</td>
		<td colspan="3" id="more_engines" <?php if(isset($_POST['engine']) && $_POST['engine'] == 'Other'){ echo 'style="display:block"'; }else{echo 'style="display:none"';}?>>
			<input type="text" name="engine_other" value="<?php echo $_POST['engine_other']?>" />
		</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td>&nbsp;</td>
		<td colspan="10">Please answer the following, and where appropriate use the following as a guide:<br/>
			&nbsp;&nbsp;&nbsp;
			<strong>1</strong> = 'strongly disagree'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<strong>2</strong> = 'disagree'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<strong>3</strong> = 'neither agree or disagree'<br/>
			&nbsp;&nbsp;&nbsp;
			<strong>4</strong> = 'agree'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<strong>5</strong> = 'strongly agree'
		</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="10">
			2.&nbsp;&nbsp;&nbsp;In general, I found that the quality of the results returned were comparable to your normal search engine of choice (as indicated in Question1 above).
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td><input type="radio" name="result_quality" value="1" <?php if (isset($_POST['result_quality']) && $_POST['result_quality'] == '1'){ echo'checked'; } ?> />1</td>
		<td><input type="radio" name="result_quality" value="2" <?php if (isset($_POST['result_quality']) && $_POST['result_quality'] == '2'){ echo'checked'; } ?> />2</td>
		<td><input type="radio" name="result_quality" value="3" <?php if (isset($_POST['result_quality']) && $_POST['result_quality'] == '3'){ echo'checked'; } ?> />3</td>
		<td><input type="radio" name="result_quality" value="4" <?php if (isset($_POST['result_quality']) && $_POST['result_quality'] == '4'){ echo'checked'; } ?> />4</td>
		<td><input type="radio" name="result_quality" value="5" <?php if (isset($_POST['result_quality']) && $_POST['result_quality'] == '5'){ echo'checked'; } ?> />5</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="10">
			3.&nbsp;&nbsp;&nbsp;I found the interface very easy to use.
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td><input type="radio" name="easy_to_use" value="1" <?php if (isset($_POST['easy_to_use']) && $_POST['easy_to_use'] == '1'){ echo'checked'; } ?> />1</td>
		<td><input type="radio" name="easy_to_use" value="2" <?php if (isset($_POST['easy_to_use']) && $_POST['easy_to_use'] == '2'){ echo'checked'; } ?> />2</td>
		<td><input type="radio" name="easy_to_use" value="3" <?php if (isset($_POST['easy_to_use']) && $_POST['easy_to_use'] == '3'){ echo'checked'; } ?> />3</td>
		<td><input type="radio" name="easy_to_use" value="4" <?php if (isset($_POST['easy_to_use']) && $_POST['easy_to_use'] == '4'){ echo'checked'; } ?> />4</td>
		<td><input type="radio" name="easy_to_use" value="5" <?php if (isset($_POST['easy_to_use']) && $_POST['easy_to_use'] == '5'){ echo'checked'; } ?> />5</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="10">
			4.&nbsp;&nbsp;&nbsp;I liked how the results were presented. 
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td><input type="radio" name="results_presented" value="1" <?php if (isset($_POST['results_presented']) && $_POST['results_presented'] == '1'){ echo'checked'; } ?> />1</td>
		<td><input type="radio" name="results_presented" value="2" <?php if (isset($_POST['results_presented']) && $_POST['results_presented'] == '2'){ echo'checked'; } ?> />2</td>
		<td><input type="radio" name="results_presented" value="3" <?php if (isset($_POST['results_presented']) && $_POST['results_presented'] == '3'){ echo'checked'; } ?> />3</td>
		<td><input type="radio" name="results_presented" value="4" <?php if (isset($_POST['results_presented']) && $_POST['results_presented'] == '4'){ echo'checked'; } ?> />4</td>
		<td><input type="radio" name="results_presented" value="5" <?php if (isset($_POST['results_presented']) && $_POST['results_presented'] == '5'){ echo'checked'; } ?> />5</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="10">
			5.&nbsp;&nbsp;&nbsp;The speed of the meta engine is comparable to that of my typical engine of choice.
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td><input type="radio" name="speed" value="1" <?php if (isset($_POST['speed']) && $_POST['speed'] == '1'){ echo'checked'; } ?> />1</td>
		<td><input type="radio" name="speed" value="2" <?php if (isset($_POST['speed']) && $_POST['speed'] == '2'){ echo'checked'; } ?> />2</td>
		<td><input type="radio" name="speed" value="3" <?php if (isset($_POST['speed']) && $_POST['speed'] == '3'){ echo'checked'; } ?> />3</td>
		<td><input type="radio" name="speed" value="4" <?php if (isset($_POST['speed']) && $_POST['speed'] == '4'){ echo'checked'; } ?> />4</td>
		<td><input type="radio" name="speed" value="5" <?php if (isset($_POST['speed']) && $_POST['speed'] == '5'){ echo'checked'; } ?> />5</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="10">
			6.&nbsp;&nbsp;&nbsp;If given the option, would you make this your default search engine?
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td>&nbsp;</td>
		<td><input type="radio" name="make_default" value="yes" <?php if (isset($_POST['make_default']) && $_POST['make_default'] == 'yes'){ echo'checked'; } ?> />YES</td>
		<td><input type="radio" name="make_default" value="no" <?php if (isset($_POST['make_default']) && $_POST['make_default'] == 'no'){ echo'checked'; } ?> />NO</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="3">
			7.&nbsp;&nbsp;&nbsp;I found the alternative searches useful.
			<span class="important">*</span>
		</td>
		<td><a href="imgs/feed_img1.jpg" target="_blank" title="Alternative Searches">Example1</a></td>
		<td><a href="imgs/feed_img2.jpg" target="_blank" title="Alternative Searches">Example2</a></td>
	</tr><tr>
		<td><input type="radio" name="clustering" value="1" <?php if (isset($_POST['clustering']) && $_POST['clustering'] == '1'){ echo'checked'; } ?> />1</td>
		<td><input type="radio" name="clustering" value="2" <?php if (isset($_POST['clustering']) && $_POST['clustering'] == '2'){ echo'checked'; } ?> />2</td>
		<td><input type="radio" name="clustering" value="3" <?php if (isset($_POST['clustering']) && $_POST['clustering'] == '3'){ echo'checked'; } ?> />3</td>
		<td><input type="radio" name="clustering" value="4" <?php if (isset($_POST['clustering']) && $_POST['clustering'] == '4'){ echo'checked'; } ?> />4</td>
		<td><input type="radio" name="clustering" value="5" <?php if (isset($_POST['clustering']) && $_POST['clustering'] == '5'){ echo'checked'; } ?> />5</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="3">
			8.&nbsp;&nbsp;&nbsp;Which display did you find the best?
			<span class="important">*</span>
		</td>
		<td><a href="imgs/feed_img3.jpg" target="_blank" title="Display Choice Front page">Example3</a></td>
		<td><a href="imgs/feed_img4.jpg" target="_blank" title="Display Choice Results page">Example4</a></td>
	</tr><tr>
		<td><input type="radio" name="display" value="all" <?php if (isset($_POST['display']) && $_POST['display'] == 'all'){ echo'checked'; } ?> />Standard</td>
		<td><input type="radio" name="display" value="col" <?php if (isset($_POST['display']) && $_POST['display'] == 'col'){ echo'checked'; } ?> />Columned</td>
		<td><input type="radio" name="display" value="bing" <?php if (isset($_POST['display']) && $_POST['display'] == 'bing'){ echo'checked'; } ?> />Bing<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only</td>
		<td><input type="radio" name="display" value="ddgo" <?php if (isset($_POST['display']) && $_POST['display'] == 'ddgo'){ echo'checked'; } ?> />DuckDuckGo<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only</td>
		<td><input type="radio" name="display" value="yahoo" <?php if (isset($_POST['display']) && $_POST['display'] == 'yahoo'){ echo'checked'; } ?> />Yahoo!<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only</td>
		<td><input type="radio" name="display" value="n/a" <?php if (isset($_POST['display']) && $_POST['display'] == 'n/a'){ echo'checked'; } ?> />Don't<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Know</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="4">
			9.&nbsp;&nbsp;&nbsp;A better set of results were obtained with <em>aggrigation</em> turned:
			<span class="important">*</span>
		</td>
		<td><a href="imgs/feed_img5.jpg" title="Turn On/Off Aggrigation Front page" target="_blank">Example5</a></td>
		<td><a href="imgs/feed_img6.jpg" title="Turn On/Off Aggrigation Results Page" target="_blank">Example6</a></td>
	</tr><tr>
		<td>&nbsp;</td>
		<td><input type="radio" name="aggrigation" value="on" <?php if (isset($_POST['aggrigation']) && $_POST['aggrigation'] == 'on'){ echo'checked'; } ?> />ON</td>
		<td><input type="radio" name="aggrigation" value="off" <?php if (isset($_POST['aggrigation']) && $_POST['aggrigation'] == 'off'){ echo'checked'; } ?> />OFF</td>
		<td><input type="radio" name="aggrigation" value="n/a" <?php if (isset($_POST['aggrigation']) && $_POST['aggrigation'] == 'n/a'){ echo'checked'; } ?> />Don't Know</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="4">
			10.&nbsp;&nbsp;&nbsp;A better set of results were obtained with <em>Pre-Processing</em> turned:
			<span class="important">*</span>
		</td>
		<td><a href="imgs/feed_img7.jpg" title="Turn On/Off Pre-Processing Front page" target="_blank">Example7</a></td>
		<td><a href="imgs/feed_img8.jpg" title="Turn On/Off Pre-Processing Results Page" target="_blank">Example8</a></td>
	</tr><tr>
		<td>&nbsp;</td>
		<td><input type="radio" name="pre-pro" value="on" <?php if (isset($_POST['pre-pro']) && $_POST['pre-pro'] == 'on'){ echo'checked'; } ?> />ON</td>
		<td><input type="radio" name="pre-pro" value="off" <?php if (isset($_POST['pre-pro']) && $_POST['pre-pro'] == 'off'){ echo'checked'; } ?> />OFF</td>
		<td><input type="radio" name="pre-pro" value="n/a" <?php if (isset($_POST['pre-pro']) && $_POST['pre-pro'] == 'n/a'){ echo'checked'; } ?> />Don't Know</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="10">
			11.&nbsp;&nbsp;&nbsp;An adequate number of results were produced.
			<span class="important">*</span>
		</td>
	</tr><tr>
		<td><input type="radio" name="num_results" value="1" <?php if (isset($_POST['num_results']) && $_POST['num_results'] == '1'){ echo'checked'; } ?> />1</td>
		<td><input type="radio" name="num_results" value="2" <?php if (isset($_POST['num_results']) && $_POST['num_results'] == '2'){ echo'checked'; } ?> />2</td>
		<td><input type="radio" name="num_results" value="3" <?php if (isset($_POST['num_results']) && $_POST['num_results'] == '3'){ echo'checked'; } ?> />3</td>
		<td><input type="radio" name="num_results" value="4" <?php if (isset($_POST['num_results']) && $_POST['num_results'] == '4'){ echo'checked'; } ?> />4</td>
		<td><input type="radio" name="num_results" value="5" <?php if (isset($_POST['num_results']) && $_POST['num_results'] == '5'){ echo'checked'; } ?> />5</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td colspan="3">
			12.&nbsp;&nbsp;&nbsp;Any Errors/Problems found during evaluation:<br/>(Please be as detailed as possible)
		</td>
		<td colspan="7"><textarea cols="35" rows="4" name="probs" value="<?php echo $_POST['probs'];?>"></textarea></td>
	</tr><tr>
		<td colspan="10"><hr/></td>
	</tr><tr>
		<td>
			&nbsp;Gender:
			<span class="important">*</span>
		</td>
		<td><input type="radio" name="sex" value="m" <?php if (isset($_POST['sex']) && $_POST['sex'] == 'm'){ echo'checked'; } ?> />Male</td>
		<td><input type="radio" name="sex" value="f" <?php if (isset($_POST['sex']) && $_POST['sex'] == 'f'){ echo'checked'; } ?> />Female</td>
		<td><input type="radio" name="sex" value="?" <?php if (isset($_POST['sex']) && $_POST['sex'] == '?'){ echo'checked'; } ?> />Other</td>
	</tr><tr>
		<td align="center">Name:</td>
		<td colspan="2"><input type="text" name="name" value="<?php echo $_POST['name'];?>" /></td>
		<td>
			&nbsp;Age Group
			<span class="important">*</span>
		</td>
		<td colspan="2"><select name="age">
			<option value=""></option>
			<option value="<12" <?php if (isset($_POST['age']) && $_POST['age'] == '<12'){ echo'selected'; } ?> > < 12 </option>
			<option value="13-15" <?php if (isset($_POST['age']) && $_POST['age'] == '13-15'){ echo'selected'; } ?> > 13 - 15 </option>
			<option value="16-19" <?php if (isset($_POST['age']) && $_POST['age'] == '16-19'){ echo'selected'; } ?> > 16 - 19 </option>
			<option value="20-24" <?php if (isset($_POST['age']) && $_POST['age'] == '20-24'){ echo'selected'; } ?> > 20 - 24 </option>
			<option value="25-29" <?php if (isset($_POST['age']) && $_POST['age'] == '25-29'){ echo'selected'; } ?> > 25 - 29 </option>
			<option value="30-34" <?php if (isset($_POST['age']) && $_POST['age'] == '30-34'){ echo'selected'; } ?> > 30 - 34 </option>
			<option value="35-39" <?php if (isset($_POST['age']) && $_POST['age'] == '35-39'){ echo'selected'; } ?> > 35 - 39 </option>
			<option value="40-44" <?php if (isset($_POST['age']) && $_POST['age'] == '40-44'){ echo'selected'; } ?> > 40 - 44 </option>
			<option value="45-49" <?php if (isset($_POST['age']) && $_POST['age'] == '45-49'){ echo'selected'; } ?> > 45 - 49 </option>
			<option value="50+" <?php if (isset($_POST['age']) && $_POST['age'] == '50+'){ echo'selected'; } ?> > 50 + </option>
		</select></td>
	</tr><tr>
		<td colspan="2" align="center">Any other Comments:</td>
		<td colspan="8"><textarea cols="35" rows="4" name="comments" value="<?php echo $_POST['comments'];?>"></textarea></td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr><tr>
		<td>&nbsp;</td>
		<td colspan="3" align="center">
			<input type="submit" name="Submit" value="Send" class="button"/>&nbsp;&nbsp;&nbsp;
			<input type="reset" class="button" />
		</td>
	</tr><tr>
		<td>&nbsp;</td>
	</tr></table>
</form></div>
</div></body>
</html>