<?php

require_once('./Page.php');

/**
 * Description of page
 *
 * @author cleberson
 */
class page extends PageObject
{

    private $dateField;

    public $elements = array(
        "add user" => ".model-user .addlink",
        "add responsavel" => ".model-responsavel .addlink",
        "add aluno" => ".model-aluno .addlink",
        "add professor" => ".model-professor .addlink",
        "add disciplina" => ".model-disciplina .addlink",
        //usuario
        "user field" => "#id_username",
        "pass field" => "#id_password1",
        "pass field confirm" => "#id_password2",
        "save" => "input.default",
        "first name" => "#id_first_name",
        "last name" => "#id_last_name",
        "email user" => "#id_email",
        "pai" => "option:contains('pais')",
        "professor" => "option:contains('professores')",
        "escolher funcao" => "#id_groups_add_link",
        //

        "nome" => "#id_nome",
        "sobrenome" => "#id_sobrenome",
        "email" => "#id_e_mail",
        "telefone" => "#id_telefone",
        "endereco" => "#id_endereco",

        "select" => ".select2-selection__arrow",
        "procurar usuario" => ".select2-search__field",
        "selecionar usuario" => "li:nth-child(1)",
        "data nascimento" => ".field-data_nascimento a:contains('Hoje')",
        "quinta serie" => "#id_turmas option:contains('5')",
        "quarta serie" => "#id_turmas option:contains('4')",
        "setima serie" => "#id_turmas option:contains('7')",
        "sexta serie" => "#id_turmas option:contains('6')",

        "disciplina" => "#id_nome_disciplina",
        "procurar turma" => ".field-turma .select2-selection__arrow",
        "procurar professor" => ".field-professor .select2-selection__arrow",


    );


    public function dateEquals($date)
    {

        $this->waitElement($this, '.ember-view .button__label');

        $this->dateField = self::getSession()->getPage()->find('css', '.ember-view .button__label');


        //  assert(!is_null($this->dateField));
        echo($this->dateField->getText());
        if ($this->dateField->getText() != $date) {
            throw new Exception("Valor da data atual: " . $this->dateField->getText() . "\n Valor esperado: " . $date);
        }
    }

    public function insertNumber($number)
    {
        $this->dateField = self::getSession()->getPage()->find('css', "#chapterNumber");
        self::waitElement($this, "#chapterNumber");
        assert(!is_null($this->dateField));

        $this->dateField->setValue($number);

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
