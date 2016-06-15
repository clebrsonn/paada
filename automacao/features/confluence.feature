#features/confluence.feature

Feature: Criar Usuários


#  Scenario Outline: Criar Usuários
#    Given I am on "http://localhost:8000/login/?next=/"
#    When I login as "admin " with password "admin123"
#    Then I click on "login button"
#    And I stay on "http://localhost:8000/paada_admin/"
#    When I click on "add user"
#    When I insert text "<usuario>" in "user field"
#    When I insert text "paada123" in "pass field"
#    When I insert text "paada123" in "pass field confirm"
#    And I click on "save"
#    When I insert text "<usuario>" in "first name"
#    When I insert text "<last name>" in "last name"
#    When I insert text "<email>" in "email user"
#    And I click on "<funcao>"
#    And I click on "escolher funcao"
#    Then I click on "save"
#    Examples:
#      | usuario  | last name | email          | funcao    |
#      | douglas  | anônimo   | paada@mail.com | professor |
#      | dennis   | anônimo   | paada@mail.com | professor |
#      | gleidson | anônimo   | paada@mail.com | professor |
#      | rodrigo  | anônimo   | paada@mail.com | professor |
#      | mario    | anônimo   | paada@mail.com | pai       |
#      | maria    | anônimo   | paada@mail.com | pai       |
#      | priscila | anônimo   | paada@mail.com | pai       |

#
#  Scenario Outline: Criar Responsaveis
#    Given I am on "http://localhost:8000/login/?next=/"
#    When I login as "admin " with password "admin123"
#    Then I click on "login button"
#    And I stay on "http://localhost:8000/paada_admin/"
#    When I click on "add responsavel"
#    When I insert text "<usuario>" in "nome"
#    When I insert text "<last name>" in "sobrenome"
#    When I insert text "<email>" in "email"
#    When I insert text "1234567809" in "telefone"
#    When I insert text "casa" in "endereco"
#    And I click on "select"
#    When I insert text "<usuario>" in "procurar usuario"
#    And I wait
#    And I click on "selecionar usuario"
#    And I click on "save"
#    Examples:
#      | usuario  | last name | email          |
#      | mario    | anônimo   | paada@mail.com |
#      | maria    | anônimo   | paada@mail.com |
#      | priscila | anônimo   | paada@mail.com |


#  Scenario Outline: Criar Alunos
#    Given I am on "http://localhost:8000/login/?next=/"
#    When I login as "admin " with password "admin123"
#    Then I click on "login button"
#    And I stay on "http://localhost:8000/paada_admin/"
#    When I click on "add aluno"
#    When I insert text "<usuario>" in "nome"
#    When I insert text "<last name>" in "sobrenome"
#    When I insert text "<email>" in "email"
#    When I insert text "1234567809" in "telefone"
#    When I insert text "casa" in "endereco"
#    And I click on "select"
#    When I insert text "<responsavel>" in "procurar usuario"
#    And I wait
#    And I click on "selecionar usuario"
#    And I click on "<serie>"
#    And I click on "data nascimento"
#    And I click on "save"
#    And I wait
#    And I wait
#    Examples:
#      | usuario   | last name | email          | responsavel | serie        |
#      | pedro     | anônimo   | paada@mail.com | mario       | sexta serie  |
#      | aline     | anônimo   | paada@mail.com | mario       | sexta serie  |
#      | jaudilene | anônimo   | paada@mail.com | maria       | quinta serie |
#      | márcio    | anônimo   | paada@mail.com | maria       | quarta serie |
#      | cristiane | anônimo   | paada@mail.com | priscila    | setima serie |
#      | júlia     | anônimo   | paada@mail.com | priscila    | setima serie |
#      | juliana   | anônimo   | paada@mail.com | priscila    | quinta serie |
#
#
#  Scenario Outline: Criar Professores
#    Given I am on "http://localhost:8000/login/?next=/"
#    When I login as "admin " with password "admin123"
#    Then I click on "login button"
#    And I stay on "http://localhost:8000/paada_admin/"
#    When I click on "add professor"
#    When I insert text "<usuario>" in "nome"
#    When I insert text "<last name>" in "sobrenome"
#    When I insert text "<email>" in "email"
#    When I insert text "1234567809" in "telefone"
#    When I insert text "casa" in "endereco"
#    And I click on "select"
#    When I insert text "<usuario>" in "procurar usuario"
#    And I wait
#    And I click on "selecionar usuario"
#    And I click on "save"
#    Examples:
#      | usuario  | last name | email          |
#      | douglas  | anônimo   | paada@mail.com |
#      | dennis   | anônimo   | paada@mail.com |
#      | gleidson | anônimo   | paada@mail.com |
#      | rodrigo  | anônimo   | paada@mail.com |
#

  Scenario Outline: Criar Disciplinas
    Given I am on "http://localhost:8000/login/?next=/"
    When I login as "admin " with password "admin123"
    Then I click on "login button"
    And I stay on "http://localhost:8000/paada_admin/"
    When I click on "add disciplina"
    When I insert text "<disciplina>" in "disciplina"
    And I click on "procurar turma"
    When I insert text "<turma>" in "procurar usuario"
    And I wait
    And I click on "selecionar usuario"
    And I click on "procurar professor"
    When I insert text "<professor>" in "procurar usuario"
    And I wait
    And I click on "selecionar usuario"
    And I click on "save"
    Examples:
      | professor | disciplina | turma |
      | douglas   | artes      | 4     |
      | douglas   | artes      | 5     |
      | douglas   | artes      | 6     |
      | douglas   | artes      | 7     |
      | dennis    | inglês     | 4     |
      | dennis    | inglês     | 5     |
      | dennis    | inglês     | 6     |
      | dennis    | inglês     | 7     |
      | gleidson  | religião   | 4     |
      | gleidson  | religião   | 5     |
      | gleidson  | religião   | 6     |
      | gleidson  | religião   | 7     |
      | rodrigo   | física     | 4     |
      | rodrigo   | física     | 5     |
      | rodrigo   | física     | 6     |
      | rodrigo   | física     | 7     |