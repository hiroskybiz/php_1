<?php
$place = rand(1,5); // ���ʂ�1?5�͈̔͂Ń����_���ɍ��ꂽ������$place�ɑ��
echo "place�̒��g:".$place."\n";
if($place == 1){
    // 1�ʂ������Ƃ��̏���
    echo "����";
}elseif($place == 2){
    echo "���";
}elseif($place == 3){
    echo "����";
}else{
    // ����ȊO�������Ƃ��̏���
    echo $place."��";
}

?>
