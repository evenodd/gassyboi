from gas_sensor import GasSensor
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

co2 = 0
voc = 0

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
          s.send_header("Content-type", "text/html")
          s.end_headers()

    def do_GET(s):
        print(s.path)
          s.send_response(200)
          s.send_header("Content-type", "text/html")
          s.end_headers()
          print("%d,%d" % (co2, voc))
          s.wfile.write(bytes(("%d,%d" % (co2, voc)), 'utf-8'))

server_class = HTTPServer

httpd = server_class(("", 8000), Handler)
threading.Thread(target=lambda: httpd.serve_forever()).start()

gasSensor = GasSensor()

while True:
    time.sleep(1)
    co2, voc = gasSensor.getData()