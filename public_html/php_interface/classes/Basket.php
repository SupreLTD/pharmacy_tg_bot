<?php


class Basket
{
    private $basket;
    private $id;

    function __construct($id)
    {
        $this->id = $id;
        $this->setBasket();
    }

    public function setBasket()
    {
        $this->basket = json_decode($this->curl('getBasket', $this->id), true);
    }

    public function getBasket()
    {
        return $this->basket;
    }

    public function addCart($product_id){
        $res = $this->curl('addToBasket', $this->id, $product_id, true);
        return $res;
    }

    public function createOrder(){
        $res = $this->curl('makeOrder', $this->id, 0, true);
        return $res;
    }
    private static function curl($method, $id, $product_id = 0, $post = false)
    {
        if( $curl = curl_init() ) {
            $url = API_URL.$method.'?user_id='.$id;
            if($product_id){
                $url .= '&product_id='.$product_id;
            }
            curl_setopt($curl, CURLOPT_URL, $url);
            curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
            if($post){
                curl_setopt($curl, CURLOPT_POST, true);
                curl_setopt($curl, CURLOPT_POSTFIELDS, []);
            }
            $out = curl_exec($curl);
            curl_close($curl);
            return $out;
        }
    }
}