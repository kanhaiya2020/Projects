<?php

	$testEmail=$_POST['email'];
	$testPasswd=$_POST['pswd'];

	$servername="localhost:3306";
	$user="root";
	$pwd="";
	$dbName="testdb";
	$conn = mysqli_connect($servername, $user, $pwd, $dbName) or die("Conn. failed");
	
	
	$sql="SELECT *from `users` where email='$testEmail' and password='$testPasswd'";
	$res = mysqli_query($conn, $sql) or die("sql error $sql");
	$row=mysqli_num_rows($res);
	$result = mysqli_fetch_array($res);
		 
 	if($row>0)
	{
		header('Location:home_page.php');
		echo "<script type='text/javascript'>alert('Login Success!')</script>";
	
	
			// window.onload= function()
			//setinterval
			//   ajax object
	
	}
	else
		echo "Login Failed!";
	
	
	
	
?>