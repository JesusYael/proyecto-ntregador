<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
    <body>
    <?php
        try
        {
            $conMySQL=new PDO("mysql:host=localhost; port=3306; dbname=colectivas", "root", "");
            $conMySQL->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $conMySQL->exec("SET CHARACTER SET UTF8");
            $sentenciaSQL="SELECT id_consesionario FROM consesionario WHERE email= :login AND password= :passw";
            $sentenciaPrep = $conMySQL->prepare($sentenciaSQL);
            $log=htmlspecialchars(addslashes($_POST["user"]));
            $pas=htmlspecialchars(md5($_POST["contra"]));
            $sentenciaPrep->execute(array(":login"=>$log,":passw"=>$pas));
            $numRegistros = $sentenciaPrep->rowCount();
            if ($numRegistros !=0)
            {
                session_start();
                $_SESSION["usuario"]=$_POST["user"];
                header("Location:interfaz_prueba.php");
                printf("Bienvenido");
            }
            else
            {
                header("Location:error.html");
            }
        }
        catch(Exception $e)
        {
            die("Error: " . $e->getMessage());
        }
        finally { $conMySQL = null;    }
    ?>
    </body>
</html>