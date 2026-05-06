# 🚀 PORTFOLIO TÉCNICO - EXPOEMPLEO IESA 2026

**Ingeniero de Sistemas | Trading Algorítmico | Ciberseguridad | Machine Learning**

---

## 📋 DESCRIPCIÓN

Portfolio técnico integrado con **5 prototipos funcionales** desarrollados 100% en Python, diseñados para demostrar habilidades a empresas participantes en la ExpoEmpleo IESA 2026.

---

## 🎯 PROTOTIPOS INCLUIDOS

### 1. 🛡️ ShieldVZLA - Detector de Amenazas Tipo Lotus Wiper
- **Categoría**: Ciberseguridad
- **Tecnologías**: Python, Windows API simulation, SQLite
- **Demo**: Detección de comandos destructivos (diskpart clean, robocopy /MIR, fsutil)
- **Empresas Objetivo**: Intelix, Netconsult, PwC, Deloitte

### 2. 📈 TradeGuard - Dashboard de Trading + Análisis de Riesgo
- **Categoría**: Finanzas Cuantitativas
- **Tecnologías**: Pandas, Plotly, Streamlit
- **Demo**: Gráficos de velas japonesas, VaR, métricas de riesgo
- **Empresas Objetivo**: Banesco, Mercantil, EY, KPMG

### 3. 🤖 FinRisk AI - Clasificador de Riesgo Crediticio
- **Categoría**: Machine Learning
- **Tecnologías**: Scikit-learn (Random Forest), Pandas
- **Demo**: Predicción de riesgo crediticio con probabilidades
- **Empresas Objetivo**: Deloitte, KPMG, Banesco, Bancaribe

### 4. 📦 InventoryBot - Gestión Inteligente de Inventarios
- **Categoría**: Retail Tech / ERP
- **Tecnologías**: SQLite, Pandas, Predicción de series temporales
- **Demo**: CRUD de inventario, alertas de stock, predicción de demanda
- **Empresas Objetivo**: Farmatodo, Central Madeirense, Droguería Nena, SOFtech

### 5. 📄 DocuVerify - Verificador de Documentos
- **Categoría**: Blockchain-Lite / Seguridad
- **Tecnologías**: SHA-256 hash, SQLite
- **Demo**: Registro y verificación de documentos con hash criptográfico
- **Empresas Objetivo**: HLB, PwC, Deloitte, KPMG

---

## ⚙️ STACK TECNOLÓGICO

- **Python 3.9+**
- **Streamlit** - Framework de UI
- **SQLite** - Base de datos embebida
- **Plotly** - Visualización interactiva
- **Pandas** - Manipulación de datos
- **Scikit-learn** - Machine Learning
- **NumPy** - Computación numérica

---

## 🚀 INSTRUCCIONES DE EJECUCIÓN

### Paso 1: Instalar Dependencias
```bash
cd "prototipo para la feria"
pip install -r requirements.txt
```

### Paso 2: Ejecutar Aplicación
```bash
streamlit run expoempleo_iesa_demo.py
```

### Paso 3: Abrir en Navegador
La aplicación se abrirá automáticamente en:
- **Local**: http://localhost:8501
- **Network**: http://192.168.x.x:8501 (para compartir en la feria)

---

## 📱 GUÍA DE USO EN LA FERIA

### Preparación (5 minutos antes)
1. Abrir terminal en la carpeta del proyecto
2. Ejecutar: `streamlit run expoempleo_iesa_demo.py`
3. Verificar que se abre en el navegador
4. Maximizar ventana del navegador (F11 para pantalla completa)

### Durante la Feria
1. **Sidebar**: Navegar entre los 5 prototipos
2. **Demo interactiva**: Mostrar funcionalidades a reclutadores
3. **Prueba en vivo**: Permitir que el reclutador interactúe

### Flujo Recomendado por Empresa

| Empresa | Prototipo a Mostrar | Tiempo |
|---------|---------------------|--------|
| **Intelix** | ShieldVZLA (Ciberseguridad) | 3-5 min |
| **Netconsult** | ShieldVZLA + InventoryBot | 5 min |
| **Banesco** | TradeGuard + FinRisk AI | 5 min |
| **Mercantil** | TradeGuard (Trading) | 3 min |
| **PwC** | FinRisk AI + DocuVerify | 5 min |
| **Deloitte** | FinRisk AI (ML) | 3 min |
| **EY** | TradeGuard (Fintech) | 3 min |
| **KPMG** | FinRisk AI + DocuVerify | 5 min |
| **HLB** | DocuVerify (Auditoría) | 3 min |
| **Farmatodo** | InventoryBot (Retail) | 3 min |
| **Central Madeirense** | InventoryBot (Stock) | 3 min |
| **SOFtech** | InventoryBot (ERP) | 3 min |

---

## 💡 TIPS PARA RECLUTADORES

### Pitch de Elevador (30 segundos)
> "Soy Ingeniero de Sistemas en 9no semestre con experiencia en trading algorítmico y ciberseguridad. He desarrollado este portfolio técnico con 5 prototipos funcionales: detección de malware tipo Lotus que afectó Venezuela, dashboard de trading con análisis de riesgo, scoring crediticio con Machine Learning, gestión de inventarios inteligente, y verificación documental con blockchain-lite. Todo desarrollado 100% en Python."

### Puntos Destacar por Empresa

**Bancos (Banesco, Mercantil):**
- TradeGuard: "Experiencia en trading + ingeniería = perfil fintech"
- FinRisk AI: "Modelos de scoring de riesgo"

**Consultoras (Big 4):**
- FinRisk AI: "Machine Learning para auditoría predictiva"
- DocuVerify: "Integridad documental garantizada"
- ShieldVZLA: "Ciberseguridad para clientes"

**Tecnología (Intelix, Netconsult):**
- ShieldVZLA: "Conocimiento específico de amenazas venezolanas"
- Todo el stack: "Full-stack Python developer"

**Retail (Farmatodo, Central Madeirense):**
- InventoryBot: "Predicción de demanda y optimización de stock"

---

## 🛠️ TROUBLESHOOTING

### Problema: Puerto 8501 ocupado
```bash
streamlit run expoempleo_iesa_demo.py --server.port 8502
```

### Problema: Error de dependencias
```bash
pip install --upgrade streamlit plotly pandas numpy scikit-learn
```

### Problema: Base de datos corrupta
```bash
del expoempleo_demo.db
streamlit run expoempleo_iesa_demo.py  # Se recrea automáticamente
```

---

## 📊 DATOS TÉCNICOS

- **Líneas de código**: ~700
- **Módulos**: 5 prototipos integrados
- **Base de datos**: SQLite embebida
- **Tiempo de desarrollo**: ~2 días
- **Framework UI**: Streamlit
- **100% Python puro**: Sin JavaScript ni HTML manual

---

## 🎓 CRÉDITOS

**Desarrollado por:** [Tu Nombre]  
**Perfil:** Ingeniero de Sistemas - 9no Semestre  
**Evento:** ExpoEmpleo IESA 2026  
**Fecha:** 5 y 6 de Mayo de 2026  
**Ubicación:** Campus IESA, San Bernardino, Caracas

---

## 📞 CONTACTO

- **LinkedIn**: [tu-linkedin]
- **GitHub**: [tu-github]
- **Email**: [tu-email]

---

**¡Éxito en la ExpoEmpleo IESA 2026! 🚀**
