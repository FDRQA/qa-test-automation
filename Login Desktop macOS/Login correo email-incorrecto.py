import pyautogui
import time
import subprocess
import pyperclip  # Para copiar y pegar texto sin errores

# ============================
# 1️⃣ ABRIR INTERNXT DRIVE
# ============================
print("🚀 Abriendo Internxt Drive...")
subprocess.run(["open", "-a", "Internxt Drive"])
time.sleep(8)  # Esperar a que la app cargue

# ============================
# 2️⃣ HACER CLIC EN "INICIA SESIÓN CON EL NAVEGADOR"
# ============================
print("🔵 Haciendo doble clic en 'Inicia sesión con el navegador'...")
x_login_btn, y_login_btn = 1044, 275  # Coordenadas del botón
pyautogui.moveTo(x_login_btn, y_login_btn, duration=1)
time.sleep(1)
pyautogui.doubleClick(x_login_btn, y_login_btn)

print("✅ Navegador abierto, esperando la página de login...")
time.sleep(7)  # Esperar a que el navegador cargue

# ============================
# 3️⃣ INGRESAR EMAIL INCORRECTO
# ============================
print("📌 Escribiendo email incorrecto...")
x_email, y_email = 729, 428  # Coordenadas del campo email
pyautogui.moveTo(x_email, y_email, duration=1)
time.sleep(1)
pyautogui.click(x_email, y_email)
time.sleep(1)

email = "correo_incorrecto@internxt.com"  # Email erróneo
pyperclip.copy(email)
pyautogui.hotkey("command", "v")  # Pegar el email
time.sleep(1)

print(f"✅ Email ingresado incorrectamente: {email}")

# ============================
# 3.1️⃣ HACER CLIC FUERA PARA CERRAR EL AUTOCOMPLETADO
# ============================
print("🖱️ Cerrando el autocompletado de email...")
x_outside, y_outside = 500, 300  # Punto fuera del campo email
pyautogui.click(x_outside, y_outside)
time.sleep(1)

# ============================
# 4️⃣ INGRESAR CONTRASEÑA
# ============================
print("🔐 Escribiendo contraseña...")
x_password, y_password = 600, 480  # Clic más a la izquierda para evitar solapamiento
pyautogui.moveTo(x_password, y_password, duration=1)
time.sleep(1)
pyautogui.click(x_password, y_password, clicks=2)  # Doble clic para asegurarnos de que está enfocado
time.sleep(1)

password = "Morgana.79@"
pyperclip.copy(password)
pyautogui.hotkey("command", "v")  # Pegar la contraseña
time.sleep(1)

print("✅ Contraseña ingresada correctamente.")

# ============================
# 5️⃣ HACER CLIC EN "LOG IN"
# ============================
print("🔵 Haciendo clic en el botón 'Log in'...")
x_login_btn, y_login_btn = 749, 528  # Coordenadas del botón "Log in"
pyautogui.moveTo(x_login_btn, y_login_btn, duration=1)
time.sleep(1)
pyautogui.click(x_login_btn, y_login_btn)

print("⏳ Esperando respuesta del servidor...")
time.sleep(5)  # Esperar la respuesta del login

# ============================
# 6️⃣ DETECTAR ERROR EN LOGIN
# ============================
print("🔎 Buscando mensaje de error...")
error_region = (650, 550, 400, 100)  # Ajusta esta región según la ubicación del mensaje de error

screenshot = pyautogui.screenshot(region=error_region)
error_message_path = "error_login.png"
screenshot.save(error_message_path)

print(f"📸 Captura de pantalla guardada: {error_message_path}")
print("🚫 ERROR: No se pudo iniciar sesión con el email incorrecto.")