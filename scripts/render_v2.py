import asyncio, sys, pathlib
from playwright.async_api import async_playwright
from PIL import Image
SRC=pathlib.Path(sys.argv[1]).resolve(); OUT=pathlib.Path(sys.argv[2]).resolve()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1350},device_scale_factor=1)
        await pg.goto(f"file://{SRC}"); await pg.wait_for_timeout(500)
        for el in await pg.query_selector_all("section.slide"):
            i=await el.get_attribute("id"); png=OUT/f"{i}.png"
            await el.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(OUT/f"{i}.jpg",quality=92,optimize=True); png.unlink()
        await b.close()
asyncio.run(main())
