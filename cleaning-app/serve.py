import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.argv = ["http.server", "3000"]
import http.server
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler)
