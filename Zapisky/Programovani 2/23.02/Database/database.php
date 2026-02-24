<?php
$dsn = "mysql:host=localhost;dbname=Hudec;charset=utf8";
$username="root";
$password="";
try{
    $db=new PDO($dsn, $username, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    echo "Roblox";
}


catch (PDOException $e){
    echo"nelze se pripojit k db:".$e->getmessage();
    
}

function GET ($table,$id){
    $sql="SELECT * FROM $table where id= :id";
    $stmt = $db->prepare($sql) //ochrana pro sql injection
    $stmt->execute(['id'==>$id]); //provedeni přikazu
    return $stmt->fetch(PDO::FETCH_ASSOC);
    
}
function GETALL($table){
    global $db;
    $sql="SELECT * FROM $table";
    $stmt = $db->prepare($sql) //ochrana pro sql injection
    $stmt->execute(); //provedeni přikazu
    return $stmt->fetchALL(PDO::FETCH_ASSOC);
}
?>