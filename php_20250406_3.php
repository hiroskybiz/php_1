<?php
// 値段計算をしてみよう
// 代数演算子 + - * / %
// $apple　リンゴの値段
// $apple_num　リンゴを買う数
$apple = 350;
$apple_num = rand(1,10);

echo "りんごの値段：".$apple."円\n";
echo "りんごを買う数：".$apple_num."個\n";

$total = $apple * $apple_num;
echo "合計".$total."円です。";
?>
