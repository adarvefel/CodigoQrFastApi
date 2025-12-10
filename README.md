Generador de Códigos QR con FastAPI + HTML 🎨🖼️

Aplicación web que permite crear códigos QR personalizados, eligiendo el color del QR y el color del fondo mediante RGB, con opción de visualizar y descargar la imagen generada.

🚀 Requisitos Previos

Antes de iniciar, asegúrate de tener instalado:

Python 3.8 o superior

PowerShell (en Windows)

pip actualizado

📦 1️⃣ Activar el entorno virtual

Desde la carpeta raíz del proyecto, ejecuta en PowerShell:

.\Scripts\Activate.ps1


Debes ver algo como esto al inicio de tu terminal:

(QrPython) PS C:\Users\Usuario\Proyecto>

📁 2️⃣ Entrar en la carpeta del proyecto
cd codigoQrHtml





Lista los archivos para verificar:

dir


Debes ver:

main.py
index.html
requirements.txt


📥 3️⃣ Instalar dependencias (solo una vez)

Con el entorno virtual activado, ejecuta:

python -m pip install --upgrade pip
pip install -r requirements.txt


Si falta alguna dependencia (como qrcode[pil], python-multipart o pillow):

pip install qrcode[pil] python-multipart pillow


📌 Dependencias principales del proyecto

Librería	Uso
FastAPI	Backend de la app
Uvicorn	Servidor ASGI
qrcode[pil]	Generación de QR
python-multipart	Soporte para formularios HTML
Pillow	Procesado de imagen
▶️ 4️⃣ Ejecutar el servidor FastAPI

Ejecuta el backend dentro de la carpeta donde está main.py:

python -m uvicorn main:app --reload


Si todo está correcto, aparecerá:

Uvicorn running on http://127.0.0.1:8000
Application startup complete.

🌐 5️⃣ Abrir la aplicación

Abre tu navegador y visita:

http://127.0.0.1:8000


Luego:

📝 Escribe el texto del QR
🎨 Elige colores RGB (QR + fondo)
📸 Visualiza el QR
⬇️ Descárgalo si lo deseas

🛑 6️⃣ Apagar el servidor

Para detener:

CTRL + C


Si el proceso queda activo:

tasklist | findstr uvicorn
taskkill /PID NUMERO /F

💡 Notas Importantes

✔️ Los códigos QR se guardan en la carpeta qrs/
🎨 Puedes modificar el diseño en index.html
⚙️ Puedes cambiar el tamaño del QR desde main.py