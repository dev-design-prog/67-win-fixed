import asyncio
import logging
import os
from bot import main as bot_main
from api_server import create_app
from aiohttp import web

logging.basicConfig(level=logging.INFO)

async def run_all():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", "8080")))
    await site.start()
    print(f"API server running on port {os.getenv('PORT', '8080')}")
    
    await bot_main()

if __name__ == "__main__":
    asyncio.run(run_all())
