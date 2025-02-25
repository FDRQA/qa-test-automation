import pyautogui
import pyperclip  # Para copiar y pegar texto (pip install pyperclip)
import time
import subprocess

# 1️⃣ ABRIR LA APLICACIÓN INTERNXT DRIVE
ruta_app = r"C:\Users\fatim\AppData\Local\Programs\internxt-drive\Internxt.exe"

print("🚀 Abriendo Internxt Drive...")
subprocess.Popen(ruta_app)  
time.sleep(8)  # Esperar a que la app cargue completamente

# 2️⃣ HACER CLIC EN EL CAMPO DE EMAIL
x_email, y_email = 1735, 982  # REEMPLAZA con las coordenadas correctas del campo email
print("📧 Haciendo doble clic en el campo de email...")
pyautogui.moveTo(x_email, y_email, duration=1)
pyautogui.doubleClick()
time.sleep(1)

# 3️⃣ BORRAR TEXTO EXISTENTE EN EL EMAIL
print("🧹 Borrando texto en email...")
pyautogui.hotkey("ctrl", "a")  # Seleccionar todo el texto
pyautogui.press("backspace")   # Borrar
time.sleep(1)

# 4️⃣ ESCRIBIR EL EMAIL USANDO `CTRL + V`
print("✉️ Escribiendo email...")
pyperclip.copy("fatima@internxt.com")  # Copiar email al portapapeles
pyautogui.hotkey("ctrl", "v")  # Pegar email en el campo
time.sleep(1)

# 5️⃣ HACER CLIC EN EL CAMPO DE CONTRASEÑA
x_password, y_password = 1937, 1168  # REEMPLAZA con las coordenadas correctas del campo contraseña
print("🔐 Haciendo doble clic en el campo de contraseña...")
pyautogui.moveTo(x_password, y_password, duration=1)
pyautogui.doubleClick()
time.sleep(1)

# 6️⃣ BORRAR TEXTO EXISTENTE EN CONTRASEÑA
print("🧹 Borrando texto en contraseña...")
pyautogui.hotkey("ctrl", "a")  
pyautogui.press("backspace")
time.sleep(1)

# 7️⃣ ESCRIBIR LA CONTRASEÑA USANDO `CTRL + V`
print("🔐 Escribiendo contraseña...")
pyperclip.copy("Morgana.79@")  # Copia la contraseña al portapapeles
pyautogui.hotkey("ctrl", "v")  # Pega la contraseña en el campo
time.sleep(1)

# 8️⃣ HACER CLIC EN "INICIAR SESIÓN"
x_login, y_login = 1997, 1378  # REEMPLAZA con las coordenadas correctas del botón "Iniciar sesión"
print("✅ Haciendo clic en el botón de login...")
pyautogui.moveTo(x_login, y_login, duration=1)
pyautogui.click()

print("🚀 Login automatizado completado.")

