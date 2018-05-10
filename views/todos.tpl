<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>User</title>
</head>
<body>
    <table>
        <tr>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Edad</th>
            <th>Universidad</th>
        </tr>
        <!--Tambien se puede usar fors e ifs-->
        %for dato in datos:
        <tr>
            <td>{{dato["nombre"]}}</td>
            <td>{{dato["apellidos"]}}</td>
            <td>{{dato["edad"]}}</td>
            <td>{{dato["universidad"]}}</td>
        </tr>
        %end

    </table>
</body>
</html>