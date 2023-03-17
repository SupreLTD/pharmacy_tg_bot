<?php


class SessionUser
{
    private $id;
    function __construct()
    {
        $this->id = $this->sessionStart();
    }

    private static function sessionStart()
    {
        if(isset($_COOKIE['id'])){
            return $_COOKIE['id'];
        }else{
            $id = mt_rand(1000000000, 9999999999);
            setcookie('id',$id,time() + (86400 * 5));
            return $_COOKIE['id'];
        }
    }

    public function getID(){
        return $this->id;
    }
}