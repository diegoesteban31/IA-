# Uninformed Search
## Funcionamiento:
#### El programa lee un archivo .txt ubicado en la misma carpeta, el cual debe contener el mapa completo del laberinto. Comienza la búsqueda según la estrategia. Al terminar la búsqueda, muestra la ruta tomada por el agente, la cantidad de estados explorados, el tiempo gastado y el costo requerido. 
## Parámetros:
#### Al ejecutar el programa debe tener como parámetro el nombre de la estrategia ("BFS","DFS","UCS").
#### El archivo de texto con la información del laberinto debe ser llamado "juego.txt"
## Pregunta: ¿Cuál es el mejor algoritmo para resolver el problema del laberinto?
#### Si se requiere un tiempo mínimo, la mejor estrategía sería DFS, sin embargo, esta tiene un costo bastante elevado. Por otro lado, la estrategia BFS y UCS, gastan el doble de tiempo pero el costo se reduce un 75% aproximadamente. Para nosotros, la mejor estrategía es BFS. 
