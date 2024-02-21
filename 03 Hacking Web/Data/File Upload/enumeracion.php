<?php
function enumerarDirectorio($directorio) {
    $contenido = "";
    if (is_dir($directorio)) {
        if ($dh = opendir($directorio)) {
            while (($archivo = readdir($dh)) !== false) {
                if ($archivo != '.' && $archivo != '..') {
                    $rutaCompleta = "$directorio/$archivo";
                    $contenido .= "<p>$rutaCompleta</p>";
                    if (is_dir($rutaCompleta)) {
                        $contenido .= enumerarDirectorio($rutaCompleta);
                    }
                }
            }
            closedir($dh);
        }
    } else {
        $contenido .= "El directorio $directorio no existe.";
    }
    return $contenido;
}

// Directorio a enumerar
$rutaDirectorio = "../../";

// Llamar a la función para enumerar el directorio
$html = "<html><head><title>Enumeración de Directorio</title></head><body>";
$html .= "<h1>Contenido del directorio $rutaDirectorio</h1>";
$html .= enumerarDirectorio($rutaDirectorio);
$html .= "</body></html>";

echo $html;
?>