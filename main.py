from subprocess import Popen, PIPE
import subprocess
import time

output = Popen(["acpi"],stdout=PIPE)
response = output.communicate()
print(response)

def take_acpi_response():
  output = Popen(["acpi"],stdout=PIPE)
  response = str(output.communicate())
  for i in range(len(response)):
    if response[i] == "%":
      if response[i-3:i-1] == "100":
        return 100
      if response[i-2:i-1].isdigit():
        return int(response[i-2:i])
      else:
        return int(response[i-1])
  
def main():
  while True:
    response = take_acpi_response()
    if(response > 60 and response < 70):
      print("The charge is between 60 and 70, shutdown..")
      subprocess.call(['shutdown', 'now'])
      break
    if(response < 60):
      print("The battery charge is too low, waiting for charging..")
      time.sleep(300)

    if(response > 70):
      print("The charge is too high, waiting for discharge..")
      time.sleep(300)

if __name__ == '__main__': 
  main()
