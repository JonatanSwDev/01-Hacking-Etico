<?php
    if(isset($_SERVER['HTTP_USER_AGENT']) && isset($_SERVER['REMOTE_ADDR']) && isset($_SERVER['QUERY_STRING'])){
        $ip = $_SERVER['REMOTE_ADDR'];
        $browser = $_SERVER['HTTP_USER_AGENT'];

        $fp = fopen('log.txt', 'a');
        fwrite($fp, $ip . ' ' . $browser . "\n");
        fwrite($fp, urldecode($_SERVER['QUERY_STRING']). " \n\n");
        fclose($fp);
    }
?>   