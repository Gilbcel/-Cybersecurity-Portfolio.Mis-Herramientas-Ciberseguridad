import json
import urllib.request

def analizar_indicador(ip_o_dominio):
    print(f"[+] Iniciando análisis SOAR para el indicador: {ip_o_dominio}")
    url = f"https://ripe.net{ip_o_dominio}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                print(f"[⚡] Enriquecimiento exitoso: Datos de red obtenidos para {ip_o_dominio}")
                enviar_alerta_simulada(ip_o_dominio, "ALTA", "IP asociada a tráfico anómalo detectado por Recon-Script.")
    except Exception:
        print(f"[!] No se pudo automatizar la consulta externa, procediendo con alerta local.")
        enviar_alerta_simulada(ip_o_dominio, "CRÍTICA", "IoC no registrado o bloqueo preventivo requerido.")

def enviar_alerta_simulada(indicador, severidad, detalles):
    payload = {
        "event": "INCIDENT_ALERT_SOAR",
        "severity": severidad,
        "target": indicador,
        "description": detalles,
        "action_taken": "LOGGED_AND_QUEUED_FOR_CONTAINMENT"
    }
    print("\n================ ALERT DISPATCHED (SOAR) ================")
    print(json.dumps(payload, indent=4))
    print("=========================================================\n")
    print("[+] Tarea finalizada: Alerta enviada al equipo de Blue Team.")

if __name__ == "__main__":
    ip_sospechosa = "8.8.8.8" 
    analizar_indicador(ip_sospechosa)
