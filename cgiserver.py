#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos el módulo CGIHTTPServer

from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler


class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/"]


httpd = HTTPServer(("", 8000), Handler)
httpd.serve_forever()
