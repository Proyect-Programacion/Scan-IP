# Scan-IP
Projecto de programacion

1. Coordinador del Proyecto y Módulo Principal (Participante 1)
	•	Diseñar la estructura principal del programa (archivo principal que une todos los módulos).
	•	Implementar la lógica para coordinar el escaneo de IPs y puertos.
	•	Integrar los módulos desarrollados por los demás participantes.
	•	Realizar pruebas iniciales para asegurarse de que todo funcione de manera conjunta.

2. Módulo de Escaneo de IPs (Participante 2)
	•	Implementar el escaneo de rangos de IPs (e.g., 192.168.1.1 a 192.168.1.255).
	•	Usar ping o ICMP requests para detectar IPs activas.
	•	Optimizar el manejo de respuestas lentas o nulas para evitar bloqueos.
	•	Devolver una lista de IPs activas al módulo principal.

3. Módulo de Escaneo de Puertos (Participante 3)
	•	Crear la lógica para escanear los puertos abiertos de una IP dada.
	•	Usar sockets para enviar y recibir datos de los puertos.
	•	Soportar rangos de puertos especificados por el usuario.
	•	Optimizar el escaneo con concurrencia (hilos o asincronía).

4. Interfaz de Usuario (CLI o GUI) (Participante 4)
	•	Diseñar una interfaz para que el usuario:
	•	Ingrese rangos de IPs y puertos.
	•	Elija opciones como tipo de escaneo (rápido, completo, etc.).
	•	Vea los resultados en tiempo real o al final.
	•	Trabajar en la salida del programa (tabla de resultados, exportar a un archivo, etc.).

5. Pruebas y Optimización de Código (Participante 5)
	•	Diseñar casos de prueba para verificar cada módulo por separado (IPs, puertos, interfaz).
	•	Implementar herramientas para medir el rendimiento del programa (tiempo de escaneo, uso de recursos).
	•	Buscar y corregir errores en la integración de los módulos.
	•	Documentar las funciones y sugerir optimizaciones.

Metodología de Trabajo
	•	Colaboración: Usar un repositorio en GitHub para que todos trabajen en el mismo código y gestionen versiones.
	•	Daily Meetings: Reunirse brevemente cada día para discutir avances y problemas.
	•	Integración Continua: El coordinador (Participante 1) se asegura de integrar los módulos conforme están listos.