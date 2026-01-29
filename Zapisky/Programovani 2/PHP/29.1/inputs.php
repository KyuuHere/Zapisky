<?php
$checkbox=empty($_POST{"name"}) ? "false" : "true";
echo "Checkbox: $checkbox <br>";
echo "color: ".$_POST{"color"};¨
echo "date:".$_POST["date"]."<br>";
echo "datetime".$_POST["datetime"]."<br>";
echo "email:".$_POST["email"]."<br>";
echo "file:".$_POST["file"]."<br>";
echo "hidden".$_POST["hidden"]."<br>";
echo "image:".$_POST["image"]."<br>";
echo "month:".$_POST["month"]."<br>";
echo "password".$_POST["password"]."<br>";
echo "range".$_POST["range"]."<br>";
echo "search:".$_POST["search"]."<br>";
echo "tel:".$_POST["tel"]."<br>";
echo "number:".$_POST["number"]."<br>";
echo "Sex:".$_POST["sex"]."<br>";
?>
