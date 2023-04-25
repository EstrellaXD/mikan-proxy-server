from fastapi import FastAPI
from fastapi.responses import Response

from server import get_rss_proxy, PORT

app = FastAPI()


@app.get("/RSS/MyBangumi")
async def get_rss(token: str):
    content = get_rss_proxy(token)
    return Response(content=content, media_type="application/xml")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=PORT)
