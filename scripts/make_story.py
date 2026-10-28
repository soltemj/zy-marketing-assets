"""Convierte una imagen de feed (ej. 1080x1350) en historia 1080x1920 sin recortar.

La imagen se escala al ancho 1080 y se centra verticalmente sobre un fondo del
color de su esquina, dejando el texto fuera de las zonas que tapa la interfaz
de Instagram (arriba y abajo ~250 px).

Uso: python3 scripts/make_story.py ENTRADA.jpg SALIDA.jpg
"""
import sys
from PIL import Image

W, H = 1080, 1920


def make_story(src, dst):
    im = Image.open(src).convert("RGB")
    scale = W / im.width
    if im.height * scale > H - 500:  # deja margen seguro para la UI
        scale = (H - 500) / im.height
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    bg = Image.new("RGB", (W, H), im.getpixel((5, 5)))
    bg.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
    bg.save(dst, "JPEG", quality=92)


if __name__ == "__main__":
    make_story(sys.argv[1], sys.argv[2])
