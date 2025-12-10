from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import qrcode
import os
from qrcode.image.pil import PilImage

app = FastAPI()

QR_FOLDER = "qrs"
os.makedirs(QR_FOLDER, exist_ok=True)

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
def leer_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/generar-qr/")
def generar_qr(
    texto: str = Form(...),
    color: str = Form("#000000"),
    backColor: str = Form("#ffffff")
):
    file_path = f"{QR_FOLDER}/qr.png"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img: PilImage = qr.make_image(fill_color=color, back_color=backColor)
    img.save(file_path)

    return FileResponse(file_path, media_type="image/png", filename="codigo_qr.png")
