import pyautogui
import time
import webbrowser 
import mouseinfo


link=webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(10) 

pyautogui.click(440,226)
time.sleep(5)

pyautogui.click(472,350)
pyautogui.click(625,224)
# mouseinfo.MouseInfoWindow()


# inbox_position=pyautogui.locateOnScreen('Screenshot from 2023-08-29 11-32-53.png')
# if inbox_position is not None:
#     inbox_x, inbox_y = inbox_position
#     pyautogui.click(inbox_x, inbox_y)  # Click on the inbox icon
#     time.sleep(1) 



# email_subject_position = pyautogui.locateOnScreen('Screenshot from 2023-08-29 12-13-16.png')  # Replace with your email subject image

# if email_subject_position is not None:
#     email_x, email_y, _, _ = email_subject_position
#     pyautogui.click(email_x, email_y)  # Click on the email's subject
#     time.sleep(1)  # Wait for the email to open (adjust as needed)

#     # Now, simulate marking the email as read (if applicable)
#     # This example uses the 'R' key to mark the email as read
# else:
#     print("Unread email subject not found on the screen.")