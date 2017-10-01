
        <?php
            $curl=curl_init();
            //my first page
            $url="https://www.a2oj.com/categories";
            curl_setopt($curl, CURLOPT_URL,$url);
            curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
        
            $result=curl_exec($curl);
            $categories=array();
            //match category link
            preg_match_all('!<a href="(category\?ID=.*?)">(.*?)<\/a>!',$result, $match);
            $categories['name']=$match[2];
            print_r($categories['name']);
            
            //function to enter the number through user
            $number=readline("Enter the index of category you want to download");
            
            //Again enter to the category and scrap from them
            $url2="https://www.a2oj.com/".$match[1][$number];
            //echo $url2;
            curl_setopt($curl, CURLOPT_URL,$url2);
            curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
            
            $result2=curl_exec($curl);
            $categories2=array();
            //match question link
            preg_match_all('!<a href="(.*?)" target="_blank">(.*?)<\/a><\/td>!',$result2,$match2);
            
            $categories2['name']=$match2[2];
            print_r($categories2['name']);
            
            //Now i am going to the program page and scrapping its contents to a new .html file
            echo("Now you enter 2 numbers that signifies from which file to which file you want to download\n");
            $start=readline("Enter the starting file number");
            $end=readline("Enter the ending file number");
            for($i=$start;$i<=$end;$i++)
            {
                $url3=$match2[1][$i];
                curl_setopt($curl, CURLOPT_URL,$url3);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
                $result3=curl_exec($curl);
                $filename="questions/cat".$number."/".$match2[2][$i].".html";
                $file=fopen($filename, 'w');
                if($file==false){
                    echo("Error opening file Problem may be less permission to that folder where i want to write");
                    exit();
                }
                $status=fwrite($file, $result3);
                fclose($file);
            }
?>
