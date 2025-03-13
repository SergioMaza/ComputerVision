Para crear un entorno virual
python -m venv venv #Crear venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass #En caso de error al activar el venv
.venv\Scripts\activate #Activar
deactivate #Desactivar
pip freeze > requirements.txt #Crear requirements.txt

ffmpeg -i output.avi -vcodec libx264 video.mp4 # Pasar videos de .avi a .mp4