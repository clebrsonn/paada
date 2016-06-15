<?php

require_once './Page.php';

class LoginPO extends PageObject {

    private $loginField;
    private $passwordField;
    private $loginButton;

       protected $elements = array(
         "login button" => ".btn-success",
        // "admin button" => "#acp-menu-listing > li:nth-child(7) > a",
        // "manga button" => "#management a:nth-child(1)",
        // "add new chapter" => "tbody > tr > td:nth-child(3) a",
        // "chapter list" => ".table tr:nth-child(1) > td:nth-child(2) > a:nth-child(3)",
        
        // "ler pasta" => "#div:nth-child(3) > div > button",
        // "enviar" => "form > div:nth-child(4) > div > button",
        // "log out" => "#acp-menu-listing > li:nth-child(8) > a"
    );

    public function insertName($name) {

        self::waitElement($this, '.form-bottom');

        $this->loginField = self::getSession()->getPage()->find('css', '#form-username');

        assert(!is_null($this->loginField));
        $this->loginField->setValue($name);
    }

    public function insertPass($pass) {
        $this->passwordField = self::getSession()->getPage()->find('css', "#form-password");
        assert(!is_null($this->passwordField));
        $this->passwordField->setValue($pass);
    }

    

    public function getLoginField() {
        return $this->loginField;
    }

//    public function clickOnButton($button) {
//
//        //self::getSession()->getPage()->find('css', ".btn-sky");
//        $this->waitElement($this, $this->elements[$button]);
//
//        $utton = $this->getSession()->getPage()->find('css', $this->elements[$button]);
////        echo $utton->gettext();
//
//        assert(!is_null($utton));
//        // if ($button ==  "manga button") {
//        // 	$utton->press();
//        // 	return;
//        // }
//        $utton->click();
//    }


}
