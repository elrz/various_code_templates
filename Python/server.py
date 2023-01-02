import http.server
import socketserver
import socket
import datetime
import requests

def get_external_ip():
    r = requests.get("http://checkip.dyndns.com")
    text = r.text
    ip = text.split(": ")[1].split("</body>")[0]
    return ip

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        a = datetime.datetime.today().strftime("%d.%m.%Y")
        b = datetime.datetime.today().strftime("%H:%M:%S")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        hostname = socket.gethostname()
        external_ip = get_external_ip()
        #now = datetime.datetime.now()
        time = b
        date = a
        message = f"<html><body><p>Hostname: {hostname}  External IP: {external_ip} Time: {time} Date: {date}</p></body></html>"
        self.wfile.write(message.encode())

PORT = 8000

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
