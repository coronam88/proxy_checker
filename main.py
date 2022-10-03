from asyncio import run
from urllib3 import ProxyManager


def run_check():
    """Check all proxies of a proxy-list.txt file and print the status of each"""
    try:
        ex_list = []
        proxyFile = open('proxy-list.txt', 'r')
        proxyList = []
        good_proxies_counter = 0
        bad_proxies_counter = 0

        for p in proxyFile:
            proxyList.append(p[:-1])


        for i, p in enumerate(proxyList):
            print(f"proxy {i}")
            p = p.split(":")

            http = ProxyManager(f"http://{p[0]}:{p[1]}")
            try:
                r = http.request('GET', 'https://www.google.com')
                good_proxies_counter+=1
                print(f"{p} is a Good Proxy")
            except Exception as ex:
                print(f"{p} is a Bad Proxy")
                bad_proxies_counter+=1
                ex_list.append((p, ex))

        print(f"Good proxies: {good_proxies_counter}", f"Bad proxies: {bad_proxies_counter}")
        
    except Exception as ex:
        # Generate traceback
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        msg = str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        })
        print(msg)



if __name__ == '__main__':
    run_check()
