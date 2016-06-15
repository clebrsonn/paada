<?php

class PageObject
{

    private $session;
    private $locator;

    protected $elements = array('teste' => "",);

    public function __construct($session)
    {
        $this->session = $session;
    }

    public function getSession()
    {
        return $this->session;
    }

    public function waitElement($page, $locator)
    {
        $this->locator = $locator;

        $this->waitForElement($page, function ($pageWait) {
            return ($pageWait->getSession()->getPage()->find('css', $this->locator));
        });
    }

    private function waitForElement($page, $lambda, $wait = 30)
    {
        for ($i = 0; $i < $wait; $i++) {
//            var_dump($lambda);
            try {
                if ($lambda($page)) {
                    return true;
                }
            } catch (Exception $e) {
                // do nothing
            }

            sleep(1);
        }

        //$backtrace = debug_backtrace();

        throw new Exception(
            "Not Found"
        );
    }

    public function clickOnButton($button)
    {

        //self::getSession()->getPage()->find('css', ".btn-sky");
        //$this->waitElement($this, $this->elements[$button]);
        $utton = $this->getSession()->getPage()->find('css', $this->elements[$button]);
//        echo $utton->gettext();

        assert(!is_null($utton));
        // if ($button ==  "manga button") {
        // 	$utton->press();
        // 	return;
        // }
        $utton->click();
    }

    public function insertText($text, $input)
    {
        $utton = self::getSession()->getPage()->find('css', $this->elements[$input]);
        self::waitElement($this, $this->elements[$input]);
        assert(!is_null($utton));

        $utton->setValue($text);

    }


}
