#!/usr/bin/env python3

#

# Udacian activity to practice get and post http

#Aisha 



from http.server import HTTPServer, BaseHTTPRequestHandler

from urllib.parse import parse_qs



memory = []

form ='''<!DOCTYPE html>

  <title>Udacian</title>

  <form method="POST" action="http://localhost:8001/">

    <textarea name="name">name</textarea>

    <br>

    <textarea name="city">city</textarea>

    <br>

    <textarea name="enrollment">enrollment</textarea>

    <br>

    <textarea name="nanodegree">nanodegree</textarea>

    <br>

    <textarea name="status">status</textarea>

    <br>

    <button type="submit">Post it!</button>

  </form>

  <pre>

{}

  </pre>

'''



class MessageHandler(BaseHTTPRequestHandler):

    def do_POST(self):

     length = int(self.headers.get('Content-length', 0))

     memory = self.rfile.read(length).decode()

     data =parse_qs(memory)

     name = data['name'][0]

   

     self.wfile.write(memory.encode())

        
    def do_GET(self):
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write(form.encode())



if __name__ == '__main__':

    server_address = ('', 8001)

    httpd = HTTPServer(server_address, MessageHandler)

    httpd.serve_forever()
