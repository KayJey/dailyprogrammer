import socket
import sys

def parse_netloc(scheme, netloc):
	try:
		h, p = netloc.split(':', 1)
		return h, int(p)
	except ValueError:
		return netloc, 80
	

def main():
	print(sys.argv[0])
	url = sys.argv[1]

	scheme, _, netloc, path = url.split('/', 3)
	if scheme != 'http:':
		raise ValueError("Unsupported scheme")

	path = '/' + path
	host, port = parse_netloc(scheme, netloc)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	msg = 'GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path,netloc)
	s.sendall(msg.encode())

	while 1:
		data = s.recv(1024)
		print(data)
		if not data:
			break
	s.close()

if __name__ == '__main__':
	main()