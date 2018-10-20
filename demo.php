<?php
//$str = '你';
//print_r(strlen($str));
//print_r(mb_strlen($str));
//print_r($str);
//print_r(mb_ord($str[0],'utf-8'));
//exit;
$file = file('languages.txt');
foreach($file as $line) {
  print_r("\n");
echo '--------';
  print_r("\n");
  //$line = str_split($line);
$line = str_split_unicode($line);
  print_r($line);
  //$len = strlen($line); 
  //print_r($len);
  foreach($line as $char) {
    print_r(mb_ord($char));
	print_r(' ');
  }
  //for($i = 0;$i < $len;$i++) {
 //   print_r(mb_ord($line[$i],'utf-8'));
  //}
  //print_r($line);
  print_r("\n");
echo '--------';
}
function str_split_unicode($str, $l = 0) {
    if ($l > 0) {
        $ret = array();
        $len = mb_strlen($str, "UTF-8");
        for ($i = 0; $i < $len; $i += $l) {
            $ret[] = mb_substr($str, $i, $l, "UTF-8");
        }
        return $ret;
    }
    return preg_split("//u", $str, -1, PREG_SPLIT_NO_EMPTY);
}
?>
