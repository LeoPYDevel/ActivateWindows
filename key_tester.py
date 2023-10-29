import subprocess
import tkinter as tk
from tkinter import messagebox

keys = [
    "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "4CPRK-NM3K3-X6XXQ-RXX86-WXCHW",
    "KTNPV-KTRK4-3RRR8-39X6W-W44T3",
    "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "YTMG3-N6DKC-DKB77-7M9GH-8HVX7",
    "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
    "2B87N-8KFHP-DKV6R-Y2C8J-PKCKT",
    "8N67H-M3CY9-QT7C4-2TR7M-TXYCV",
    "DXG7C-N36C4-C4HTG-X4T3X-2YV77",
    "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
    "WYPNQ-8C467-V2W6J-TX4WX-WT2RQ",
    "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
    "NKJFK-GPHP7-G8C3J-P6JXR-HQRJR",
    "NPPR9-FWDCX-D2C8J-H872K-2YT43",
    "2F77B-TNFGY-69QQF-B8YKP-D69TJ",
    "CKFK9-QNGF2-D34FM-99QX2-8XC4K",
    "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4",
    "NK96Y-D9CD8-W44CQ-R8YTK-DYJWX",
    "RW7WN-FMT44-KRGBK-G44WK-QV7YK",
    "WGGHN-J84D6-QYCPR-T7PJ7-X766F",
    "WNMTR-4C88C-JK8YV-HQ7T2-76DF9",
    "XGVPP-NMH47-7TTHJ-W3FW7-8HV2C",
    "YYVX9-NTFWV-6MDM3-9PT4T-4M68B",
    "6TP4R-GNPTD-KYYHQ-7B7DP-J447Y",
    "GJTYN-HDMQY-FRR76-HVGC7-QPF8P",
    "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
    "84NGF-MHBT6-FXBX8-QWJK7-DRR8H",
    "8PTT6-RNW4C-6V7J2-C2D3X-MHBPB",
    "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    "YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY",
    "YVWGF-BXNMC-HTQYQ-CPQ99-66QFC",
    "9FNHH-K3HBT-3W4TD-6383H-6XYWF",
    "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J",
    "334NH-RXG76-64THK-C7CKG-D3VPT",
    "44RPN-FTY23-9VTTB-MP9BX-T84FV",
    "DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ",
    "MH37W-N47XK-V7XM9-C7227-GCQG9",
    "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "YYVX9-NTFWV-6MDM3-9PT4T-4M68B",
    "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J",
    "PBHCJ-Q2NYD-2PX34-T2TD6-233PK",
    "QFFDN-GRT3P-VKWWX-X7T3R-8B639",
    "VKJG7-NPHTM-C97JM-9MPGT-3V66T"
]

def abrir_archivo():
    with open("archivo.txt", "w") as f:
        for elemento in keys:
            f.write(elemento + "\n\n")

    subprocess.run(["notepad.exe", "archivo.txt"])
    
def confirmar():
    respuesta = messagebox.askyesno("Confirmar", "¿Desea continuar con la apertura de las llaves y abrir cmd?")

    if respuesta:
        abrir_archivo()
        
    else:
        print("Operación cancelada por el usuario.")

ventana = tk.Tk()

etiqueta = tk.Label(ventana, text="Presione el botón para confirmar la acción:")
etiqueta.pack()

boton_confirmar = tk.Button(ventana, text="Confirmar", command=confirmar)
boton_confirmar.pack()

ventana.title("Verificación de CMD Windows 10/11")
ventana.geometry("400x50")
                 
ventana.mainloop()
