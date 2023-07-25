import SpeedTest


test = speedtest.Speedtest()


print("Loading a list of servers...")
test.get_servers() # gets list of servers aval
print("Choosing the best server...")
best = test.get_best_server() # choose best serv
print(f"Found: {best['host']} located in {'country'}.)
      
print("Preforming download test...")
download_result = test.download()
print("Preforming uplaod test...")
upload_result = test.upload()
ping_result = test.results.ping()

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping result: {ping_result:.2f} ms")
