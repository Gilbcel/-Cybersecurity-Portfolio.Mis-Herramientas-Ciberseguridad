import re

def analizar_correo(texto_correo):
    print("==================================================")
    print("      INICIANDO ANÁLISIS DE CORREO (PHISHING)     ")
    print("==================================================")
    
    puntos_riesgo = 0
    alertas_detectadas = []
    
    palabras_phishing = [
        r"urgente", r"accion requerida", r"cuenta bloqueada", r"alerta de seguridad",
        r"verifique su cuenta", r"haga clic aqui", r"suspender", r"inicio de sesion no autorizado",
        r"ganador", r"loteria", r"cripto gratis", r"actualizar contrasena", r"inmediato", r"evitar bloqueo"
    ]
    
    for patron in palabras_phishing:
        coincidencias = re.findall(patron, texto_correo.lower())
        if coincidencias:
            cantidad = len(coincidencias)
            puntos_riesgo += cantidad * 15
            alertas_detectadas.append(f"Palabra de alta presión encontrada: '{patron}' (Cantidad: {cantidad})")
            
    enlaces = re.findall(r'https?://[^\s]+', texto_correo.lower())
    
    for url in enlaces:
        if "actualizar" in url or "seguro" in url or "verificar" in url or "login" in url:
            puntos_riesgo += 25
            alertas_detectadas.append(f"Palabra sospechosa dentro del enlace: {url}")
        if "xin" in url or "gratis" in url:
            puntos_riesgo += 30
            alertas_detectadas.append(f"Firma de dominio de alto riesgo detectada: {url}")

    porcentaje_riesgo = min(puntos_riesgo, 100)
    
    print(f"\n[📊 MÉTRICAS] Nivel de Riesgo Calculado: {porcentaje_riesgo}%")
    
    print("\n[🔍 INDICADORES DE ENGAÑO DETECTADOS]")
    if alertas_detectadas:
        for alerta in alertas_detectadas:
            print(f" -> {alerta}")
    else:
        print(" -> No se detectaron firmas obvias de phishing.")
        
    print("\n==================================================")
    print("                VERDICTO FINAL                    ")
    print("==================================================")
    if porcentaje_riesgo >= 50:
        print(f"🚨 ESTADO: CRÍTICO - PROBABLE PHISHING DETECTADO ({porcentaje_riesgo}%)")
        print("⚠️  Recomendación: NO haga clic en ningún enlace. Reporte al equipo de seguridad de inmediato.")
    elif porcentaje_riesgo >= 20:
        print(f"⚠️  ESTADO: SOSPECHOSO - PROCEDA CON PRECAUCIÓN ({porcentaje_riesgo}%)")
        print("💡 Recomendación: Verifique la identidad del remitente por canales oficiales.")
    else:
        print(f"✅ ESTADO: SEGURO - BAJO RIESGO DETECTADO ({porcentaje_riesgo}%)")
        print("👍 No se encontraron patrones de amenaza inmediatos.")
    print("==================================================\n")

if __name__ == "__main__":
    correo_ejemplo = """
    Asunto: ALERTA DE SEGURIDAD: Accion Requerida Inmediata para su cuenta!
    
    Estimado usuario,
    Hemos detectado un inicio de sesion no autorizado en su perfil. Para evitar el 
    bloqueo permanente de sus servicios, debe verifique su cuenta de inmediato.
    
    Por favor haga clic aqui para actualizar contrasena y datos de acceso:
    http://homebrewxin.com
    
    Atentamente,
    Departamento de Seguridad
    """
    
    analizar_correo(correo_ejemplo)
