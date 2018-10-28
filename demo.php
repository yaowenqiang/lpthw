<?php
  $file = file('languages.txt');
foreach($file as $line) {
  //$line = explode(' ',$line);
  $len = strlen($line); 
  print_r($len);
  print_r($line);
  //foreach($line as $char) {
   // print_r(mb_ord($char));
  //}
  for($i = 0;$i < $len;$i++) {
    print_r(mb_ord($line[$i]));
  }
  print("\n");
}
?>
