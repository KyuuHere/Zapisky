<?php
echo "dostal jsem:".$_POST["uname"]." a ".$_POST["psw"]."<br>";
session_start();
if (isset($_POST["uname"]) && isset($_POST["psw"])) {
$pass=$_SESSION{"psw"};
$user=$_SESSION{"uname"};
  echo "dostal jsem:".$user." a ".$pass."<br>";


  }

?>