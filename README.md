"Versión inicial Riky Optimizer"
# 🚀 RIKY OPTIMIZER PRO v3.0
Optimización extrema para Windows 11 / 10 enfocada en Gaming y FPS.

## 🛠️ ¿Qué hace este script?
- **Limpieza de Bloatware:** Usa la herramienta de Chris Titus para eliminar basura.
- **Power Plan:** Activa el modo "Ultimate Performance" para CPUs como el i5-12600KF.
- **RAM Boost:** Detiene servicios innecesarios (SysMain, Telemetría).
- **Transparencia:** Este código es abierto para que revises que no hay malware.

## ⚠️ Nota sobre Antivirus
Al ser una herramienta que modifica registros del sistema, algunos antivirus pueden dar "Falsos Positivos". Revisa el código fuente aquí mismo para tu tranquilidad.

🔍 Explicación Detallada del Código (Análisis Técnico)
Para los usuarios que desean saber exactamente qué cambios realiza este optimizador en su sistema, aquí desglosamos el funcionamiento del "Modo Bestia":

1. Gestión de Bloatware y Configuración Global
El script utiliza el comando de Chris Titus Tech, una herramienta de código abierto reconocida por la comunidad. Este comando abre una interfaz que permite eliminar aplicaciones preinstaladas de Windows que consumen recursos en segundo plano.

2. Mantenimiento y Salud del Sistema
sfc /scannow: Escanea y repara archivos del sistema dañados que podrían estar causando inestabilidad o caídas de FPS.

Limpieza de Eventos (wevtutil): Vacía los registros de eventos de Windows. Esto no borra archivos personales, pero elimina registros antiguos que ocupan espacio y pueden ralentizar el visor de eventos.

3. Optimización Real de Procesos y RAM
El código detiene y deshabilita servicios que no son esenciales para jugar, liberando ciclos de CPU y espacio en la memoria RAM:

SysMain (Superfetch): Se deshabilita para evitar el uso excesivo de disco y CPU.

WSearch (Windows Search): Detiene la indexación de archivos mientras juegas.

Spooler: Detiene el servicio de cola de impresión (innecesario para jugar).

MapsBroker & DiagTrack: Elimina servicios de mapas y telemetría (rastreo de datos) de Microsoft.

4. Purgado de Archivos Temporales
El script limpia las carpetas %TEMP% y C:\Windows\Temp\. Estos son archivos que Windows crea "de paso" y que muchas veces se quedan ahí ocupando espacio innecesario en tu unidad de almacenamiento.

5. Desbloqueo de Hardware (Poder Total)
Para procesadores de alto rendimiento como el i5-12600KF, el script ejecuta:

powercfg -duplicatescheme ...: Desbloquea el plan oculto de Windows llamado "Máximo Rendimiento" (Ultimate Performance).

Este plan elimina cualquier límite de ahorro de energía en el procesador y asegura que los núcleos funcionen a su frecuencia máxima sin "dormirse".

¿Cómo puedo verificar esto?
Puedes abrir el archivo Rikyoptimizer.py con cualquier editor de texto (Bloc de notas, VS Code) y verás que estos son exactamente los comandos que se ejecutan al presionar el botón de Unificación Total.

Análisis de Funciones del "Modo Bestia"
Gestión de Energía: El script utiliza powercfg para duplicar y activar el esquema de energía e9a42b02..., que corresponde al modo Máximo Rendimiento (Ultimate Performance), eliminando latencias de ahorro de energía en el CPU.

Optimización de Memoria RAM: Se ejecutan comandos de consola (sc stop y sc config ... start= disabled) para detener servicios como SysMain, WSearch y DiagTrack, reduciendo drásticamente los procesos en segundo plano.

Mantenimiento del Sistema: Ejecuta sfc /scannow para reparar archivos corruptos y utiliza wevtutil para limpiar los registros de eventos de Windows, liberando carga del procesador.

Limpieza de Archivos: Automatiza la eliminación de archivos temporales mediante comandos de sistema en las rutas %TEMP% y C:\Windows\Temp\.

⚠️ Nota sobre el EXE:
Algunos antivirus pueden marcar el ejecutable como sospechoso
debido a que modifica servicios y configuraciones del sistema.
El código fuente está disponible para verificación completa.

