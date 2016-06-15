<?php

require('LoginPo.php');
require('Mainpage.php');

use Behat\Behat\Context\Context;
use Behat\Behat\Context\SnippetAcceptingContext;
use Behat\Gherkin\Node\PyStringNode;
use Behat\Gherkin\Node\TableNode;
use Behat\MinkExtension\Context\RawMinkContext;

/**
 * Defines application features from the specific context.
 */
class FeatureContext extends RawMinkContext implements Context, SnippetAcceptingContext {

    private $page;
    /**
     * Initializes context.
     *
     * Every scenario gets its own context instance.
     * You can also pass arbitrary arguments to the
     * context constructor through behat.yml.
     */

    /**
     * @Given I am on :arg1
     */
    public function iAmOn($arg1) {
        $session = $this->getSession();
        $this->visitPath($arg1);

        //$session -> visit("https://contribution-qa-auto.apple.com/");
//        self::spin($this,function($page) {
//            return($page->getSession()->getPage()->find('css', '#accountname'));
//        });
        $this->page = new LoginPO($session);

       // $this->page->waitElement($this->page, '#accountname');

//        self::spin($this->page,function($page) {
//              return($page->getSession()->getPage()->find('css', '#accountname'));
//        });
        // $bool = $session->wait(1000, $this->page->getLoginField());
        //echo($bool);
    }

    /**
     * @When I login as :user with password :password
     */
    public function tryToLogin($user, $password) {

        $this->page->insertName($user);
        $this->page->insertPass($password);
    }

    /**
     * @Then I click on :arg1
     */
    public function iClickOn($arg1) {

//        $this->getSession()->wait(5000);

        $this->page->clickOnButton($arg1);
    }

    /**
     * @Then I wait
     */
    public function iWait() {

        $this->getSession()->wait(1000);

//        $this->page->clickOnButton($arg1);
    }


    /**
     * @Given I stay on :arg1
     */
    public function iStayOn($arg1) {

        $session = $this->getSession();
//        self::spin(function($page) {
//            return($page->getSession()->getPage()->find('css', '.ember-view .button__label'));
//        });
        $this->page = new page($session);
//        self::spin($this->page, function($page) {
//            return($page->getSession()->getPage()->find('css', '.ember-view .button__label'));
//        });
    }

    /**
     * @Then Then I should get :arg1
     */
    public function thenIShouldGet($arg1) {
        $this->page->dateEquals($arg1);
    }

//    public function spin($page, $lambda, $wait = 30) {
//        for ($i = 0; $i < $wait; $i++) {
//            try {
//                if ($lambda($page)) {
//                    return true;
//                }
//            } catch (Exception $e) {
//                // do nothing
//            }
//
//            sleep(1);
//        }
//
//        //$backtrace = debug_backtrace();
//
//        throw new Exception(
//        "Not Found"
//        );
//    }

  /**
     * @When I insert chapter :arg1 number
     */
    public function iInsertChapterNumber($arg1)
    {
//        $this->getSession()->wait(000);

        $this->page->insertNumber($arg1);
    }


    /**
     * @When I insert text :arg1 in :arg2
     */
    public function iInsertText($arg1, $arg2)
    {
//        $this->getSession()->wait(000);

        $this->page->insertText($arg1, $arg2);
    }


}
