# DESAFIO - Conseguir via pyautogui resolver o captcha do google nessa url https://www.google.com/recaptcha/api2/demo?_gl=1*n5ki6w*_ga*MTM0NzE1NjkxOS4xNzIxOTI3MjYy*_ga_37GXT4VGQK*MTczMTY3MzcwMC4xNC4xLjE3MzE2NzQ4NjYuMC4wLjA.

import pyautogui as py

captcha = py.locateCenterOnScreen('captcha.png')
py.click(captcha[0],captcha[1],duration=1)