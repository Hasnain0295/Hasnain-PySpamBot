# import pyautogui
# import time
# import random
#
# messages = [
#     "Hello There, Hasnain is here!",
#     "How are you today?",
#     "What's up?",
#     "Hope you're having a great day!"
# ]
#
# while True:
#     time.sleep(random.randint(3, 5))
#     message = random.choice(messages)
#     pyautogui.typewrite(message)
#     time.sleep(random.randint(1, 3))
#     pyautogui.press('enter')
#
#     # Log message sent to a file
#     with open("sent_messages.txt", "a") as log_file:
#         log_file.write(f"Sent: {message}\n")
