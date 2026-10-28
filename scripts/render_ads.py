import asyncio, sys, pathlib
from playwright.async_api import async_playwright
SRC = pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2]).resolve()
IDS = ["a1","a2","a3","a4","c1","c2","c3","c4","c5","c6"]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i in IDS:
            await pg.goto(f"file://{SRC}#{i}")
            await pg.reload()
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(OUT/f"{i}.png"))
        await b.close()
asyncio.run(main())
