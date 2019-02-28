#!/usr/bin/env python3

def application(environ, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    #return [b'<h1>Hello, python web.</h1>']
    body='<h1>Hello, %s.</h1>' % (environ['PATH_INFO'][1:] or 'python web')
    return [body.encode('utf-8')]
