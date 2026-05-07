from temperature import is_overheating

while True:
    try:
        temp = float(input("Ingrese temperatura: "))
        break
    except ValueError:
        print("❌ Error: solo se permiten números.")

if is_overheating(temp):
    print("⚠️ ALARMA: Temperatura alta")
else:
    print("✅ Temperatura normal")