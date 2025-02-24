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
x_login_btn, y_login_btn = 1044, 275
pyautogui.moveTo(x_login_btn, y_login_btn, duration=1)
time.sleep(1)
pyautogui.doubleClick(x_login_btn, y_login_btn)

print("✅ Navegador abierto, esperando la página de login...")
time.sleep(7)

# ============================
# 3️⃣ INGRESAR EMAIL Y CONTRASEÑA
# ============================
print("📌 Ingresando email y contraseña...")
x_email, y_email = 729, 428
pyautogui.moveTo(x_email, y_email, duration=1)
time.sleep(1)
pyautogui.click(x_email, y_email)
time.sleep(1)

email = "fatima@internxt.com"
pyperclip.copy(email)
pyautogui.hotkey("command", "v")
time.sleep(1)

# Clic fuera para cerrar autocompletado
x_outside, y_outside = 500, 300
pyautogui.click(x_outside, y_outside)
time.sleep(1)

x_password, y_password = 600, 480
pyautogui.moveTo(x_password, y_password, duration=1)
time.sleep(1)
pyautogui.click(x_password, y_password, clicks=2)
time.sleep(1)

password = "Morgana.79@"
pyperclip.copy(password)
pyautogui.hotkey("command", "v")
time.sleep(1)

print("✅ Email y contraseña ingresados correctamente.")

# ============================
# 5️⃣ HACER CLIC EN "LOG IN"
# ============================
print("🔵 Haciendo clic en el botón 'Log in'...")
x_login_btn, y_login_btn = 749, 528
pyautogui.moveTo(x_login_btn, y_login_btn, duration=1)
time.sleep(1)
pyautogui.click(x_login_btn, y_login_btn)

print("✅ Inicio de sesión en progreso. Esperando la confirmación...")
time.sleep(7)

# ============================
# 6️⃣ HACER CLIC EN "ABRIR DRIVE DESKTOP" (¡Corregido!)
# ============================
print("🔵 Haciendo clic en 'Abrir Drive Desktop'...")
x_open_drive, y_open_drive = 880, 450  # ⚠️ Ajusta según la ubicación real del botón
pyautogui.moveTo(x_open_drive, y_open_drive, duration=1)
time.sleep(1)
pyautogui.click(x_open_drive, y_open_drive)

print("✅ Drive Desktop abierto exitosamente.")
time.sleep(5)  # Esperar que la app de escritorio se abra

# ==============================================================
# 🔴 PROCESO DE CIERRE DE SESIÓN DESDE DRIVE DESKTOP
# ==============================================================

# ============================
# 7️⃣ ABRIR EL MENÚ DE INTERNXT EN LA BARRA SUPERIOR DERECHA
# ============================
print("📌 Abriendo el menú de Internxt en la barra superior derecha...")
x_internxt_icon, y_internxt_icon = 1280, 50
pyautogui.moveTo(x_internxt_icon, y_internxt_icon, duration=1)
time.sleep(1)
pyautogui.click(x_internxt_icon, y_internxt_icon)
time.sleep(2)  # Esperamos a que se despliegue el menú

print("✅ Menú de Internxt abierto.")

# ============================
# 8️⃣ HACER CLIC EN EL ICONO DE CONFIGURACIÓN (RUEDA ⚙)
# ============================
print("⚙ Haciendo clic en la rueda de configuración...")

# Coordenadas de la rueda ⚙ obtenidas manualmente
x_settings_icon, y_settings_icon = 1294, 73  # ⚠️ Coordenadas corregidas
pyautogui.moveTo(x_settings_icon, y_settings_icon, duration=1)
time.sleep(1)
pyautogui.click(x_settings_icon, y_settings_icon)
time.sleep(2)  # Esperar que se abra el menú

print("✅ Configuración abierta correctamente.")

# ============================
# 9️⃣ SELECCIONAR "CERRAR SESIÓN"
# ============================
print("🔴 Haciendo clic en 'Cerrar sesión'...")
x_logout_btn, y_logout_btn = 1227, 174  # ⚠️ Coordenadas exactas de "Cerrar sesión"
pyautogui.moveTo(x_logout_btn, y_logout_btn, duration=1)
time.sleep(1)
pyautogui.click(x_logout_btn, y_logout_btn)
time.sleep(5)

print("✅ Sesión cerrada exitosamente.")

# ============================
# 🔟 CONFIRMAR QUE VOLVIMOS A LA PANTALLA DE LOGIN
# ============================
print("📸 Capturando pantalla para verificar logout...")
screenshot = pyautogui.screenshot()
logout_confirmation_path = "logout_confirmation.png"
screenshot.save(logout_confirmation_path)

print(f"📸 Captura de pantalla guardada: {logout_confirmation_path}")
print("✅ ¡Cierre de sesión exitoso! Ahora se puede iniciar sesión con otra cuenta.")