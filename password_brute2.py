import pyautogui
import string
import time
import itertools

chars = string.ascii_letters + string.digits + string.punctuation

pwd =  pyautogui.password("Enter a password")
start_time = time.time()

test_pwd = ""

for combo in itertools.product(chars, repeat=len(pwd)):
  test_pwd = "".join(combo)
  print("<=" + str(test_pwd) + "=>")
  
  if(test_pwd == pwd):
    print("the password is " + "".join(test_pwd))
    end_time = time.time()
    total_time = round(end_time - start_time,2)
    print("It took " + str(total_time) + " seconds.")
    break
