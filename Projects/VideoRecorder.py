import cv2
import os

out = None

# Definir el codec y crear el objeto VideoWriter
def start_recording(file_name, cap):
    global out
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec para AVI
    out = cv2.VideoWriter(file_name, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Guardar el fotograma en el archivo de salida
def save_frame(img):
    out.write(img)

# Liberar recursos de VideoWriter
def stop_recording():
    out.release()
    
   

def from_avi_to_mp4(input_path, output_path):
    os.system(f"ffmpeg -i {input_path} -vcodec libx264 {output_path}")
    os.remove(input_path)