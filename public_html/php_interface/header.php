<?php
if(file_exists($_SERVER['DOCUMENT_ROOT'].'/php_interface/autoload.php')){
    require_once $_SERVER['DOCUMENT_ROOT'].'/php_interface/autoload.php';
}
define('API_URL', 'http://185.146.156.222:3001/');
global $user;
global $basket;
$user = new SessionUser();
$basket = new Basket($user->getID());