from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
    <head>
        <title>LAPTOP STORE⁂</title>
    <body>
		<b><h1 align="center"> NANDA LAPTOP STORE</h1></b>
		
		<b><h3 align="left">NANDAGOPAL.K.K(26017428)</h3></b>

		
   	<table align="center" border="3">
	
		<tr>
			<th>S.NO.</td>
            <th>DEVICE MODEL</td>
			<th>DEVICE TYPE</td>
			<th>Processor</td>
            <th>Installed RAM</td>
            <th>Graphics card</td>
            <th>Storage</td>
            <th>Storage</td>
            <th>Product ID</td>
            <th>System type</td>
            <th>Pen and touch</td>
			<th>PRICE</td>
			
		</tr>
		<tr>
			<td>1</td>
            <td>LAPTOP</td>
			<td>ACER</td>
			<td>NG-THE-GOAT</td> 
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)  </td>
            <td>16.0 GB (15.7 GB usable) </td>
            <td>Intel(R) Graphics (128 MB)</td>
            <td>119 GB of 477 GB used </td>
            <td>00342-42945-51919-AAOEM</td>
            <td>64-bit operating system, x64-based processor</td>
            <td>No pen or touch input is available for this display</td>
			<td>85000/td>
			
		
			
		</tr>
	</table>
    </body>
</html>

"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()