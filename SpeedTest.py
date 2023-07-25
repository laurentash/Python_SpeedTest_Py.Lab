import SpeedTest # CLI speed test download needed to import


test = speedtest.Speedtest()


print("Loading a list of servers...")
test.get_servers() # -> Retreving list of servers avalible
print("Choosing the best server...")
best = test.get_best_server() # -> Chooses best server avalible
print(f"Found: {best['host']} located in {'country'})

print("Preforming download test...")
download_result = test.download()  # -> Tests download speed of connection
print("Preforming uplaod test...")
upload_result = test.upload() # -> Tests upload speed of connection
ping_result = test.results.ping() # -> Tests ping of connection

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping result: {ping_result:.2f} ms")
