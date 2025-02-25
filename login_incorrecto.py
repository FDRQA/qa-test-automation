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
x_email, y_email = 1735, 982
print("📧 Haciendo doble clic en el campo de email...")
pyautogui.moveTo(x_email, y_email, duration=1)
pyautogui.doubleClick()
time.sleep(1)

# 3️⃣ BORRAR TEXTO EXISTENTE EN EL EMAIL
print("🧹 Borrando texto en email...")
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")
time.sleep(1)

# 4️⃣ ESCRIBIR EMAIL INCORRECTO USANDO `CTRL + V`
print("❌ Escribiendo email incorrecto...")
pyperclip.copy("email_incorrecto@internxt.com")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 5️⃣ HACER CLIC EN EL CAMPO DE CONTRASEÑA
x_password, y_password = 1937, 1168
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
pyperclip.copy("Morgana.79@")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 8️⃣ HACER CLIC EN "INICIAR SESIÓN"
x_login, y_login = 1997, 1378
print("✅ Haciendo clic en el botón de login...")
pyautogui.moveTo(x_login, y_login, duration=1)
pyautogui.click()
time.sleep(3)

# 9️⃣ VERIFICAR SI APARECE UN MENSAJE DE ERROR
print("🔎 Buscando mensaje de error...")

screenshot = pyautogui.screenshot()
error_x, error_y = 1800, 1450  # Coordenadas aproximadas del mensaje de error
color_pixel = screenshot.getpixel((error_x, error_y))  # Obtener el color del pixel

# ⚠️ Ajusta el color esperado si es diferente en tu sistema
color_error_esperado = (255, 0, 0)  # Ejemplo: rojo

if color_pixel == color_error_esperado:
    print("✅ TEST PASADO: Se detectó el mensaje de error correctamente.")
else:
    print("❌ TEST FALLADO: No se detectó el mensaje de error.")

print("🚀 Test de login con email incorrecto completado.")
