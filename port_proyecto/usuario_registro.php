<?php
include "conexion.php";
$rand=rand(1,1000);
if(isset($_POST['enviar'])){
    $nom= htmlspecialchars($_POST["nombre"]);
    $ap= htmlspecialchars($_POST["AP"]);
    $am= htmlspecialchars($_POST["AM"]);
    $corre= htmlspecialchars($_POST["email"]);
    $numero=(int)($_POST["numero"]);
    $contra= md5($_POST["contra"]);
    $sql= "SELECT id_pasajero FROM pasajeros WHERE email='$corre'";
    $resultado = mysqli_query($conectar, $sql);
    $filas=$resultado->num_rows;
    if($filas >0){
        echo "<script language='javascript'>
        alert('Este correo ya existe');
        location.assign('usuario_registro.php');</script>";
    }else{
        $insertar = "INSERT INTO pasajeros (nombre,primer_ap, segundo_ap, numero_usuario, email, password)
        VALUES ('$nom','$ap','$am','$numero','$corre','$contra')";

        $result=mysqli_query($conectar, $insertar);
        if($result > 0){
           echo "<script language='javascript'>
        alert('Registrado correctamente');
        location.assign('sesionp.php');</script>";
        }else{
           echo "<script language='javascript'>
        alert('Error al registrarse');
        location.assign('usuario_registro.php');</script>";

        }
    }

}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="favicon-16x16.png" type="image/png" sizes="16x16"/>
    <link rel="stylesheet" href="cssregistro.css">
    <title>Registro</title>
    <script>
        if($('form').smockValidateEqualPass('form #pass1', 'form #pass2')){
    // hacer algo ...
  }
    </script>
</head>
    <body>
        <link href='https://fonts.googleapis.com/css?family=Ubuntu:500' rel='stylesheet' type='text/css'>
        <div class="registro">
        <div class="registro-header">
            <h1>Registro de Pasajero</h1>
        </div>
        <div class="registro-form">
            <form action="<?=$_SERVER['PHP_SELF']?>" method="post">  
                <input hidden type="text" name="numero" value="<?php echo $rand;?>">              
                <h3>Nombre:</h3>
                <input type="text" name="nombre" placeholder="Ingresa tu nombre" required>
                <h3>Primer Apellido:</h3>
                <input type="text" name="AP" placeholder="Ingresa tu primer apellido" required>
                <h3>Segundo Apellido:</h3>
                <input type="text" name="AM" placeholder="Ingresa tu segundo apellido">
                <h3>Correo electrónico:</h3>
                <input type="email" name="email" placeholder="Ingresa un email válido" required>
                <h3>Contraseña</h3>
                <input type="password" name="contra" id="pass1" placeholder="Ingrese su contraseña">
                <h3>Confirme su contraseña</h3>
                <input type="password" placeholder="confirme su contraseña" id="pass2" required>
                <br>
                <br>
                <button type="submit" name="enviar">Enviar</button> <input type="reset">
            </form>
        </div> 
    </body>
</html>