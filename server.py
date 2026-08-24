import http.server
import socketserver
import functools
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PORT = 14000  # 端口被占就改这里，并同步 start.bat 里的端口

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

handler = functools.partial(NoCacheHandler, directory=BASE)

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

server = ThreadingHTTPServer(('127.0.0.1', PORT), handler)
print(f'serving on {PORT} (no-cache)')
server.serve_forever()
