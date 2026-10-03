from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
class Handler(SimpleHTTPRequestHandler):
    extensions_map=SimpleHTTPRequestHandler.extensions_map.copy(); extensions_map.update({'.js':'application/javascript','.css':'text/css','.json':'application/json'})
print('2D DRIVER running at http://127.0.0.1:8000')
ThreadingHTTPServer(('0.0.0.0',8000),Handler).serve_forever()
