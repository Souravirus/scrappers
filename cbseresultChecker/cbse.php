<?php
	$curl=curl_init();
	$url="cbseresults.nic.in";
	curl_setopt($curl, CURLOPT_URL,$url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
    $number=0;
    $flag=0;
    while($number<2)
	{	
		$result=curl_exec($curl);
		$categories=array();
		$number= preg_match_all('!<a href.*?!', $result);
		echo $number." ";
		$output=0;
		if($number>1)
		{
			$flag=1;
		}
		
		sleep(10);
	}
	if($flag==1)
	$output=shell_exec("play ~/Jenyfa\ Duncan\ -\ Australia.ogg");
	echo $output;
 ?>
