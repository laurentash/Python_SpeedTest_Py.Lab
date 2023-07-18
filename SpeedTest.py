import SpeedTest


test = speedtest.Speedtest()


print("loading server list")
test.get_servers() # gets list of servers aval
print("choosing best server")
best = test.get_best_server() # choose best serv
print(f"Found: {best['host']} located in {'country'})
      
print("preforming download test")
download_result = test.download()
print("preforming uplaod")
upload_result = test.upload()
ping_result = test.results.ping()

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping result: {ping_result:.2f} ms")
