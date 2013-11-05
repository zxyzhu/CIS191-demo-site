#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import os
import signal
import time

try:
    # If the server is already running, kill it
    try:
        f = open(".cis191pj3.pid")
        pid = int(f.readline())
        if pid > 0:
            os.kill(pid, signal.SIGTERM)
            time.sleep(2)
        f.close()
    except IOError:
        # The file didn't exist
        pass
    except OSError:
        # The server wasn't actually running
        pass

    f = open(".cis191pj3.pid", 'w+')
    f.write("%i\n" % os.getpid())
    f.close()

    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()

finally:
    # Remove the pid file again
    try:
        os.remove(".cis191pj3.pid")
    except OSError:
        pass
