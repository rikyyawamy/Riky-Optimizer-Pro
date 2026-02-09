import os
import subprocess
import ctypes
import sys
import threading
import customtkinter as ctk
from tkinter import messagebox

# Configuración Visual Estilo Gamer
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class RikyOptimizer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("RIKY OPTIMIZER v3.0 - THE UNIFICATION")
        self.geometry("750x650")
        self.resizable(False, False)

        # UI
        self.label = ctk.CTkLabel(self, text="RIKY OPTIMIZER PRO", font=("Orbitron", 32, "bold"), text_color="#00FF41")
        self.label.pack(pady=20)

        self.btn_unify = ctk.CTkButton(self, text="EJECUTAR UNIFICACIÓN TOTAL (MODO BESTIA)", 
                                        command=self.start_optimization_thread, 
                                        fg_color="#1DB954", hover_color="#179443",
                                        font=("Roboto", 18, "bold"), height=70)
        self.btn_unify.pack(pady=10, padx=50, fill="x")

        self.btn_restore = ctk.CTkButton(self, text="RESTAURAR MODO SEGURO / TRABAJO", 
                                         command=self.restore_system, 
                                         fg_color="#333333", hover_color="#444444")
        self.btn_restore.pack(pady=10, padx=150, fill="x")

        self.console = ctk.CTkTextbox(self, height=350, font=("Consolas", 12), text_color="#00FF41")
        self.console.pack(pady=20, padx=20, fill="both")
        self.log("SISTEMA LISTO: Esperando orden para liberar potencia...")

    def log(self, message):
        self.console.insert("end", f"> {message}\n")
        self.console.see("end")
        self.update()

    def start_optimization_thread(self):
        # Esto evita que la ventana se congele
        threading.Thread(target=self.mega_optimization, daemon=True).start()

    def mega_optimization(self):
        self.btn_unify.configure(state="disabled")
        self.log("🚀 INICIANDO UNIFICACIÓN TOTAL...")

        # 1. ELIMINAR BLOATWARE Y TELEMETRÍA
        self.log("📦 Eliminando Telemetría y Apps Basura...")
        subprocess.run('powershell -Command "iwr -useb https://christitus.com/win | iex"', shell=True)

        # 2. REPARACIÓN Y LIMPIEZA DE LOGS
        self.log("🛠️ Reparando archivos (SFC) y vaciando logs de eventos...")
        subprocess.run('sfc /scannow', shell=True)
        subprocess.run('for /F "tokens=*" %G in (\'wevtutil.exe el\') do (wevtutil.exe cl "%G")', shell=True)

        # 3. LIMPIEZA HARDCORE (Bajar procesos y RAM)
        self.log("🧹 Deteniendo servicios basura para bajar procesos...")
        servicios_a_matar = ["SysMain", "Spooler", "WSearch", "MapsBroker", "DiagTrack"]
        for svc in servicios_a_matar:
            subprocess.run(f'sc stop {svc}', shell=True, capture_output=True)
            subprocess.run(f'sc config {svc} start= disabled', shell=True, capture_output=True)

        # 4. LIMPIEZA DE BASURA
        self.log("🧹 Purgando archivos temporales...")
        os.system('del /s /f /q %TEMP%\\*.* >nul 2>&1')
        os.system('del /s /f /q C:\\Windows\\Temp\\*.* >nul 2>&1')

        # 5. DESBLOQUEO DE HARDWARE
        self.log("🔥 Sincronizando i5-12600KF (Plan Ultimate Performance)...")
        subprocess.run(['powercfg', '-duplicatescheme', 'e9a42b02-d5df-448d-aa00-03f14749eb61'], capture_output=True)
        subprocess.run(['powercfg', '/setactive', 'e9a42b02-d5df-448d-aa00-03f14749eb61'], capture_output=True)

        self.log("✅ UNIFICACIÓN COMPLETADA.")
        self.log("⚠️ REINICIA PARA APLICAR CAMBIOS EN LA RAM.")
        
        ctypes.windll.user32.MessageBeep(0x00000040)
        messagebox.showinfo("RIKY OPTIMIZER", "Optimización completa. ¡Reinicia tu PC para ver la reducción de procesos!")
        self.btn_unify.configure(state="normal")

    def restore_system(self):
        self.log("🔄 Restaurando servicios básicos...")
        servicios_a_activar = ["SysMain", "Spooler", "WSearch"]
        for svc in servicios_a_activar:
            subprocess.run(f'sc config {svc} start= auto', shell=True, capture_output=True)
            subprocess.run(f'sc start {svc}', shell=True, capture_output=True)
        subprocess.run(['powercfg', '/setactive', '381b4222-f694-41f0-9685-ff5bb260df2e'], capture_output=True)
        self.log("✅ Sistema restaurado.")

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        app = RikyOptimizer()
        app.mainloop()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)