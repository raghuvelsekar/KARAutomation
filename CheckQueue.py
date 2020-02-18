try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys, os
import subprocess
import pyautogui


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

### Execute django website 
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 3
pyautogui.click(207, 67)
pyautogui.click(171, 37)
pyautogui.PAUSE = 1
pyautogui.hotkey('ctrl', 'a')
pyautogui.PAUSE = 5
pyautogui.typewrite('https://p-corp-wasdm-01:9043/ibm/console/logon.jsp')
pyautogui.PAUSE = 5
pyautogui.typewrite(['enter', ])
pyautogui.PAUSE = 5
pyautogui.click(191, 329)
pyautogui.PAUSE = 3
pyautogui.click(330, 510)
pyautogui.PAUSE = 3
pyautogui.click(25, 161)
pyautogui.PAUSE = 1
pyautogui.hotkey('ctrl', 'a')
pyautogui.PAUSE = 1
pyautogui.typewrite('****')
pyautogui.PAUSE = 3
pyautogui.click(78, 194)
pyautogui.PAUSE = 1
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite('****')
pyautogui.PAUSE = 1
pyautogui.click(43, 212)
pyautogui.PAUSE = 10


pyautogui.click(70, 407)
#pyautogui.click(43, 430)
pyautogui.click(70, 407)
#pyautogui.click(44, 430)
#pyautogui.click(44, 430)



pyautogui.click(59, 426)

pyautogui.PAUSE = 5
pyautogui.click(488, 372)
pyautogui.PAUSE = 40
pyautogui.click(1147, 343)
pyautogui.click(526, 351)
##pubpoints
pyautogui.click(1069, 363)
pyautogui.click(504, 344)
##runtime
pyautogui.click(577, 239)
pyautogui.click(930, 309)
# pyautogui.click(740, 333)
# pyautogui.click(488, 258)
# pyautogui.click(762, 329)
pyautogui.PAUSE = 5
pyautogui.scroll(-150)
pyautogui.scroll(-150)
pyautogui.PAUSE = 5
img1 = pyautogui.screenshot(region=(372,198,1118,682))
img1.save("KARscreenshot1.jpg")
pyautogui.PAUSE = 5
pyautogui.click(544, 808)
pyautogui.scroll(-150)
pyautogui.PAUSE = 5
img2 = pyautogui.screenshot(region=(369,297,1126,672))
img2.save("KARscreenshot2.jpg")
pyautogui.PAUSE = 5
#exit() 
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.typewrite('172.22.110.190')
# pyautogui.PAUSE = 1
# pyautogui.click(832, 326)
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.typewrite('RemoteAccess')
# pyautogui.PAUSE = 1


# pyautogui.PAUSE = 1
# pyautogui.click(108, 298)

#pyautogui.PAUSE = 5

#img1 = pyautogui.screenshot(region=(369,297,800,700))
#img1.save("KARscreenshot1.jpg")

#pyautogui.PAUSE = 5


saved_stdout = sys.stdout
sys.stdout = open('file.txt', 'w')
print (pytesseract.image_to_string(Image.open('KARscreenshot1.jpg')))
sys.stdout.close()
sys.stdout = saved_stdout

saved_stdout = sys.stdout
sys.stdout = open('file.txt', 'a')
print (pytesseract.image_to_string(Image.open('KARscreenshot2.jpg')))
sys.stdout.close()
sys.stdout = saved_stdout

# Print list of digits
mylist = [] 
f = open('file.txt', 'r')
for line in f:
        words = line.split()
        for i in words:
                if(i.isdigit()):
                    mylist.append(i)
print (mylist)
count = 0

k = 100
for i in mylist : 
     print (i)
     print (k)
     if int(i) > int(k):
            print ("Greater then 100 on first check ")  
            pyautogui.PAUSE = 5
            img3 = pyautogui.screenshot(region=(369,297,1126,672))
            img3.save("KARscreenshot3.jpg")
            pyautogui.PAUSE = 5   
            pyautogui.click(464,672)
            pyautogui.PAUSE = 5
            pyautogui.scroll(-150)
            pyautogui.scroll(-150)
            pyautogui.PAUSE = 5
            img4 = pyautogui.screenshot(region=(372,198,1118,682))
            img4.save("KARscreenshot4.jpg")
            pyautogui.PAUSE = 5
            saved_stdout = sys.stdout
            sys.stdout = open('file2.txt', 'w')
            print (pytesseract.image_to_string(Image.open('KARscreenshot3.jpg')))
            sys.stdout.close()
            sys.stdout = saved_stdout
          
            saved_stdout = sys.stdout
            sys.stdout = open('file2.txt', 'a')
            print (pytesseract.image_to_string(Image.open('KARscreenshot4.jpg')))
            sys.stdout.close()
            sys.stdout = saved_stdout

            # Print list of digits
            mylist = [] 
            f = open('file2.txt', 'r')
            for line in f:
                    words = line.split()
                    for i in words:
                            if(i.isdigit()):
                                mylist.append(i)
            print (mylist)
            count = 0

            k = 100
            for i in mylist : 
                 print (i)
                 print (k)
                 if int(i) > int(k):
                      print ("Greater then 100 on second check ")  
                      pyautogui.click(1411, 101) 
                      p = subprocess.Popen(["powershell","-ExecutionPolicy","Unrestricted","C:\\Users\\raghuvel.sekar\\Desktop\\sendmail.ps1"], stdout=sys.stdout)
                      p.communicate()
                      exit()        
                 else :
                      print ("Less then 100 on second check ")

            #pyautogui.click(1082, 121)          
            #exit()           
                      #p = subprocess.Popen(["powershell","-ExecutionPolicy","Unrestricted","C:\\Users\\raghuvel.sekar\\Desktop\\sendmail.ps1"], stdout=sys.stdout)
                      #p.communicate()
                      #exit()        
     else :
          print ("Less then 100 on first check")
          
          
          
pyautogui.click(1411, 101)
p = subprocess.Popen(["powershell","-ExecutionPolicy","Unrestricted","C:\\Users\\raghuvel.sekar\\Desktop\\sendmail2.ps1"], stdout=sys.stdout)
p.communicate()          
exit()	



