<?php
// dat typ
print "<br><h1>Datové typy</h1><br>Čísla:";
$x = 5;
var_dump($x);
print "<br>řetězce:";
$x = "Ahoj";
var_dump($x);
print "<br>des. čísla:";
$x = 1.1;
var_dump($x);
print "<br>pravdivostní hod:";
$x = true;
var_dump($x);
print "<br>pole:";
$x = [1, 2, 3];
var_dump($x);
print "<br>objekty:";
class Car {
   public $color;
   public $model;
   public function __construct($color, $model) {
       $this->color = $color;
       $this->model = $model;
   }
   public function message(): string {
       return "Moje auto je " . $this->color . " " . $this->model;
   }
}