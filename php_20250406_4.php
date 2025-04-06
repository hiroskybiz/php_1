
<?php
// 標準入力を短いコードでGET！
while($input = fgets(STDIN)){
    $array[] = trim($input);
    
}
print_r($array);
$max = count($array)-1;
$key = rand(0,$max);
echo $array[$key];

?>

