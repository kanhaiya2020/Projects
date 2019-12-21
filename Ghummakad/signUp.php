<?php
	$a=$_POST["first"];
	$b=$_POST["last"];
	$c=$_POST["email"];
	$d=$_POST["pswd"];

	$servername="localhost:3306";
	$user="root";
	$pwd="";
	$dbName="testDB";
	$conn = mysqli_connect($servername, $user, $pwd, $dbName) or die("Conn. failed");
	
	$sql="INSERT INTO users (first, last, email, password) VALUES('$a', '$b', '$c', '$d');";
	
	$result = mysqli_query($conn, $sql);
	if($result)
		echo "<script type='text/javascript'>alert('Account Created!')</script>";
	else
		echo " <script type='text/javascript'>alert('Email already used ---')</script>";
	mysqli_close($conn);


?>