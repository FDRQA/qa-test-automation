import pyautogui
import time

print("📌 Mueve el cursor sobre la rueda ⚙ y observa las coordenadas en la terminal.")
print("⏳ Espera... La posición se actualizará cada 2 segundos.")
print("🔎 Cuando tengas la coordenada exacta, anótala y presiona CTRL + C para salir.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"📍 Coordenadas actuales: X={x}, Y={y}")
        time.sleep(2)  # ⏳ Esperar 2 segundos antes de actualizar (ajústalo si necesitas más tiempo)
except KeyboardInterrupt:
    print("\n✅ Coordenadas obtenidas. Ahora puedes usarlas en el script.")