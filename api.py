from fastapi import FastAPI
from fastapi.responses import Response, FileResponse

from server import get_rss_proxy,get_file_proxy, PORT

app = FastAPI()


@app.get("/RSS/MyBangumi")
async def get_rss(token: str):
    content = get_rss_proxy(token)
    return Response(content=content, media_type="application/xml")


@app.get("/Download/{file_path:path}")
async def get_file(file_path: str):
    print(file_path)
    content = get_file_proxy(file_path)
    # return torrent file
    return Response(content=content, media_type="application/x-bittorrent")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=PORT)
