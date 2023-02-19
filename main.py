#import module

import speedtest

#create speedtest object

test=speedtest.Speedtest()

print("server Loading .....")

#get a list of servers
test.get_servers()



#choose ideal server
print("Choosing ideal server....")

ideal=test.get_best_server()
print(ideal)

#call the downloaded function
print("Executing download server....  ")
download_outcodme=test.download()

#upload function
print("Executing upload server....  ")
upload_outcodme=test.upload()

ping_outcodme=test.results.ping
print(download_outcodme)
print(upload_outcodme)
print(ping_outcodme)

#convert Mbps
print(f"Download speed: {download_outcodme/1024/1024: .3f} Mbps")
print(f"Upload speed: {upload_outcodme/1024/1024: .3f} Mbps")
print(f"ping: {ping_outcodme:.3f} ms")

