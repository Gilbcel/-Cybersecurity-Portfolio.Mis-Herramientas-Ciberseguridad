#!/bin/bash
echo "========================================="
echo "       INICIANDO ESCANEO ÉTICO..."
echo "========================================="

# Ejecuta el escaneo y guarda el resultado en un archivo de texto
nmap scanme.nmap.org > reporte_seguridad.txt

echo "========================================="
echo "  ¡ESCANEO COMPLETADO CON ÉXITO!"
echo "  Tu reporte se guardó en: reporte_seguridad.txt"
echo "========================================="
