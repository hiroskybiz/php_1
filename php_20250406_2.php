<?php
$place = rand(1,5); // ‡ˆÊ‚ð1?5‚Ì”ÍˆÍ‚Åƒ‰ƒ“ƒ_ƒ€‚Éì‚ç‚ê‚½”Žš‚ð$place‚É‘ã“ü
echo "place‚Ì’†g:".$place."\n";
if($place == 1){
    // 1ˆÊ‚¾‚Á‚½‚Æ‚«‚Ìˆ—
    echo "‹àÜ";
}elseif($place == 2){
    echo "‹âÜ";
}elseif($place == 3){
    echo "“ºÜ";
}else{
    // ‚»‚êˆÈŠO‚¾‚Á‚½‚Æ‚«‚Ìˆ—
    echo $place."ˆÊ";
}

?>
