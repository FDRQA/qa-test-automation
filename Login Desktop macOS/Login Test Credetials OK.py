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
x_login_btn, y_login_btn = 1044, 275  # Coordenadafatima@internxt.coms del botón
pyautogui.moveTo(x_login_btn, y_login_btn, duration=1)
time.sleep(1)
pyautogui.doubleClick(x_login_btn, y_login_btn)

print("✅ Navegador abierto, esperando la página de login...")
time.sleep(7)  # Esperar a que el navegador cargue

# ============================
# 3️⃣ INGRESAR EMAIL
# ============================
print("📌 Escribiendo email...")
x_email, y_email = 729, 428  # Coordenadas del campo email
pyautogui.moveTo(x_email, y_email, duration=1)
time.sleep(1)
pyautogui.click(x_email, y_email)
time.sleep(1)

email = "fatima@internxt.com"
pyperclip.copy(email)
pyautogui.hotkey("command", "v")  # Pegar el email
time.sleep(1)

print(f"✅ Email ingresado correctamente: {email}")

# ============================
# 4️⃣ INGRESAR CONTRASEÑA
# ============================
print("🔐 Escribiendo contraseña...")
x_password, y_password = 736, 480  # Coordenadas del campo contraseña
pyautogui.moveTo(x_password, y_password, duration=1)
time.sleep(1)
pyautogui.click(x_password, y_password)
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

print("✅ Inicio de sesión en progreso. Esperando la confirmación...")
time.sleep(7)  # Esperar a que el login se procese

# ============================
# 6️⃣ HACER CLIC EN "OPEN THE DESKTOP APP"
# ============================
print("🔵 Haciendo clic en 'Open the desktop app'...")
x_open_app, y_open_app = 726, 514  # Coordenadas del botón "Open the desktop app"
pyautogui.moveTo(x_open_app, y_open_app, duration=1)
time.sleep(1)
pyautogui.click(x_open_app, y_open_app)

print("✅ Aplicación de escritorio abierta exitosamente.")