import asyncio, sys, pathlib
from playwright.async_api import async_playwright
SRC=pathlib.Path(sys.argv[1]).resolve(); OUT=pathlib.Path(sys.argv[2]).resolve(); OUT.mkdir(parents=True,exist_ok=True)
DUR=float(sys.argv[3]); FPS=int(sys.argv[4])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto(f"file://{SRC}"); await pg.wait_for_timeout(500)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        n=int(DUR*FPS)
        for i in range(n):
            t=i*1000/FPS
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t})")
            await pg.screenshot(path=str(OUT/f"f{i:05d}.jpg"),type="jpeg",quality=90)
        await b.close()
asyncio.run(main())
