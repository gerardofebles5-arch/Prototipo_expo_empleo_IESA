"""
================================================================================
EXPOEMPLEO IESA 2026 - PORTFOLIO TÉCNICO PROFESIONAL v2.0
================================================================================
Nivel: Profesional 2026 | Enterprise-Grade Demonstration

Autor: [Tu Nombre]
Perfil: Ingeniero de Sistemas 9no Semestre - Trading & Ciberseguridad
Evento: ExpoEmpleo IESA 2026 - 5 y 6 de Mayo

Stack: Python, Streamlit, SQLite, Scikit-learn, Plotly, Pandas, NumPy
UI/UX: Glassmorphism, Dark/Light Mode, Animaciones, Responsive Design
Features: Real-time Data, AI-Powered Insights, Interactive Visualizations

5 Módulos Enterprise:
1. ShieldVZLA Pro - Ciberseguridad Avanzada (EDR Simulation)
2. TradeGuard Pro - Trading Algorítmico (Real-time Analytics)
3. FinRisk AI Pro - ML Avanzado (Explainable AI)
4. InventoryBot Pro - ERP Inteligente (Predictive Analytics)
5. DocuVerify Pro - Blockchain Enterprise (Smart Contracts)
================================================================================
"""

import streamlit as st
import sqlite3
import hashlib
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random
import json
import os
import time
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# Configuración de página profesional
st.set_page_config(
    page_title="Portfolio Técnico Profesional | ExpoEmpleo IESA 2026",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com',
        'Report a bug': 'mailto:tu-email@example.com',
        'About': 'Portfolio Técnico Profesional v2.0 - ExpoEmpleo IESA 2026'
    }
)

# ================================================================================
# CSS PROFESIONAL 2026 - GLASSMORPHISM + DARK MODE
# ================================================================================
st.markdown("""
<style>
    /* Reset y base */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Variables de color 2026 - Modo Claro */
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --secondary: #06b6d4;
        --accent: #f59e0b;
        --success: #10b981;
        --danger: #ef4444;
        --warning: #f59e0b;
        --info: #3b82f6;
        --bg-primary: #ffffff;
        --bg-secondary: #f8fafc;
        --bg-card: rgba(255, 255, 255, 0.95);
        --text-primary: #1e293b;
        --text-secondary: #64748b;
        --border: rgba(226, 232, 240, 0.8);
        --shadow: rgba(0, 0, 0, 0.08);
        --glass: rgba(255, 255, 255, 0.7);
    }
    
    /* Modo Oscuro */
    [data-theme="dark"] {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-card: rgba(30, 41, 59, 0.95);
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --border: rgba(51, 65, 85, 0.8);
        --shadow: rgba(0, 0, 0, 0.3);
        --glass: rgba(30, 41, 59, 0.7);
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: var(--glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 8px 32px var(--shadow);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 60px var(--shadow);
    }
    
    /* Headers Profesionales */
    .hero-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .gradient-subtitle {
        background: linear-gradient(90deg, var(--text-secondary), var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 500;
    }
    
    /* Métricas Premium */
    .metric-container {
        background: var(--bg-card);
        border-radius: 20px;
        padding: 24px;
        border: 1px solid var(--border);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .metric-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--text-primary);
        margin: 8px 0;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: var(--text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .metric-delta {
        font-size: 0.9rem;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-top: 8px;
    }
    
    .metric-delta.positive {
        background: rgba(16, 185, 129, 0.15);
        color: var(--success);
    }
    
    .metric-delta.negative {
        background: rgba(239, 68, 68, 0.15);
        color: var(--danger);
    }
    
    /* Alert Cards Premium */
    .alert-premium {
        border-radius: 16px;
        padding: 20px 24px;
        margin: 16px 0;
        display: flex;
        align-items: flex-start;
        gap: 16px;
        border: 1px solid;
        animation: slideIn 0.4s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .alert-critical {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(239, 68, 68, 0.05));
        border-color: rgba(239, 68, 68, 0.3);
        color: #dc2626;
    }
    
    .alert-warning {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05));
        border-color: rgba(245, 158, 11, 0.3);
        color: #d97706;
    }
    
    .alert-success {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.05));
        border-color: rgba(16, 185, 129, 0.3);
        color: #059669;
    }
    
    .alert-info {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(59, 130, 246, 0.05));
        border-color: rgba(59, 130, 246, 0.3);
        color: #2563eb;
    }
    
    /* Botones Premium */
    .btn-primary {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
    }
    
    /* Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 24px;
        margin-top: 24px;
    }
    
    .feature-card {
        background: var(--bg-card);
        border-radius: 20px;
        padding: 28px;
        border: 1px solid var(--border);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        opacity: 0.1;
        border-radius: 0 0 0 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        border-color: var(--primary);
        box-shadow: 0 20px 40px var(--shadow);
    }
    
    .feature-icon {
        width: 56px;
        height: 56px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin-bottom: 20px;
    }
    
    /* Status Badges */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .status-active {
        background: rgba(16, 185, 129, 0.15);
        color: var(--success);
    }
    
    .status-pending {
        background: rgba(245, 158, 11, 0.15);
        color: var(--warning);
    }
    
    /* Code Blocks */
    .code-block {
        background: #1e293b;
        border-radius: 12px;
        padding: 20px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        color: #e2e8f0;
        overflow-x: auto;
        border: 1px solid #334155;
    }
    
    /* Progress Bars */
    .progress-container {
        background: var(--bg-secondary);
        border-radius: 12px;
        height: 12px;
        overflow: hidden;
        margin: 8px 0;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        transition: width 0.6s ease;
    }
    
    /* Animaciones */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .pulse {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    /* Sidebar Profesional */
    .sidebar-profile {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border-radius: 20px;
        padding: 24px;
        margin: 16px;
        color: white;
        text-align: center;
    }
    
    .sidebar-avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        margin: 0 auto 16px;
        backdrop-filter: blur(10px);
    }
    
    /* Tables */
    .data-table {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid var(--border);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-header {
            font-size: 2rem;
        }
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# ================================================================================
# BASE DE DATOS SQLITE PROFESIONAL
# ================================================================================
@st.cache_resource
def init_database():
    """Inicializa base de datos SQLite con tablas enterprise"""
    conn = sqlite3.connect('expoempleo_demo_v2.db', check_same_thread=False)
    cursor = conn.cursor()
    
    # Tabla de inventario con tracking completo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category TEXT,
            sku TEXT UNIQUE,
            quantity INTEGER DEFAULT 0,
            min_stock INTEGER DEFAULT 10,
            max_stock INTEGER DEFAULT 1000,
            unit_price REAL,
            cost_price REAL,
            supplier TEXT,
            location TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    # Tabla de movimientos de inventario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            transaction_type TEXT,
            quantity_change INTEGER,
            previous_quantity INTEGER,
            new_quantity INTEGER,
            reference TEXT,
            user TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES inventory(id)
        )
    ''')
    
    # Tabla de alertas de seguridad enterprise
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS security_alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_id TEXT UNIQUE,
            severity TEXT,
            category TEXT,
            threat_type TEXT,
            source_ip TEXT,
            target_system TEXT,
            command_detected TEXT,
            description TEXT,
            status TEXT DEFAULT 'active',
            assigned_to TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            resolved_at TIMESTAMP
        )
    ''')
    
    # Tabla de documentos blockchain
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id TEXT UNIQUE,
            file_name TEXT,
            file_type TEXT,
            file_size INTEGER,
            hash_sha256 TEXT UNIQUE,
            hash_md5 TEXT,
            uploaded_by TEXT,
            department TEXT,
            classification TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_verified TIMESTAMP,
            verification_count INTEGER DEFAULT 0,
            status TEXT DEFAULT 'verified'
        )
    ''')
    
    # Tabla de trades
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trade_id TEXT UNIQUE,
            symbol TEXT,
            trade_type TEXT,
            entry_price REAL,
            exit_price REAL,
            quantity INTEGER,
            stop_loss REAL,
            take_profit REAL,
            pnl REAL,
            pnl_percent REAL,
            strategy TEXT,
            status TEXT,
            opened_at TIMESTAMP,
            closed_at TIMESTAMP
        )
    ''')
    
    # Insertar datos demo si están vacíos
    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:
        products = [
            ('Paracetamol 500mg', 'Medicamentos', 'MED-001', 150, 50, 500, 5.50, 3.20, 'Farmacéutica ABC', 'A-01'),
            ('Ibuprofeno 400mg', 'Medicamentos', 'MED-002', 45, 60, 400, 8.25, 4.80, 'Farmacéutica XYZ', 'A-02'),
            ('Amoxicilina 500mg', 'Antibióticos', 'ANT-001', 200, 30, 300, 12.00, 7.50, 'Genfar Venezuela', 'B-01'),
            ('Loratadina 10mg', 'Antihistamínicos', 'ANT-002', 30, 40, 350, 6.75, 3.90, 'Farmacéutica ABC', 'B-02'),
            ('Omeprazol 20mg', 'Gastroprotectores', 'GAS-001', 80, 25, 250, 9.50, 5.60, 'Novartis Venezuela', 'C-01'),
            ('Metformina 850mg', 'Diabetes', 'DIA-001', 25, 35, 200, 15.00, 9.20, 'Genfar Venezuela', 'C-02'),
            ('Atorvastatina 20mg', 'Cardiología', 'CAR-001', 120, 45, 400, 18.50, 11.30, 'Pfizer Venezuela', 'D-01'),
            ('Aspirina 100mg', 'Cardiología', 'CAR-002', 300, 100, 600, 3.25, 1.90, 'Bayer Venezuela', 'D-02'),
        ]
        cursor.executemany('''
            INSERT INTO inventory (product_name, category, sku, quantity, min_stock, max_stock, unit_price, cost_price, supplier, location)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', products)
    
    # Insertar alertas de seguridad demo
    cursor.execute("SELECT COUNT(*) FROM security_alerts")
    if cursor.fetchone()[0] == 0:
        alerts = [
            ('ALT-2026-001', 'CRITICAL', 'Malware', 'Lotus Wiper Pattern', '192.168.1.100', 'WS-01', 'diskpart clean all', 'Intento de borrado total de disco detectado', 'blocked'),
            ('ALT-2026-002', 'HIGH', 'Data Exfiltration', 'Suspicious File Copy', '192.168.1.105', 'FILE-01', 'robocopy /MIR C:\\ D:\\backup', 'Copia masiva de archivos detectada', 'investigating'),
            ('ALT-2026-003', 'CRITICAL', 'Backup Destruction', 'Shadow Copy Deletion', '192.168.1.110', 'WS-02', 'vssadmin delete shadows /all', 'Eliminación de backups de sistema', 'blocked'),
            ('ALT-2026-004', 'MEDIUM', 'Lateral Movement', 'NETLOGON Access', '192.168.1.115', 'DC-01', 'Access to NETLOGON share', 'Acceso no autorizado a share de dominio', 'investigating'),
            ('ALT-2026-005', 'HIGH', 'Persistence', 'Registry Modification', '192.168.1.120', 'WS-03', 'reg add HKLM\\...\\Run', 'Modificación de registro para persistencia', 'active'),
        ]
        cursor.executemany('''
            INSERT INTO security_alerts (alert_id, severity, category, threat_type, source_ip, target_system, command_detected, description, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', alerts)
    
    conn.commit()
    return conn

# Inicializar base de datos
db_conn = init_database()

# ================================================================================
# FUNCIONES UTILITARIAS PROFESIONALES
# ================================================================================
def get_db_connection():
    return sqlite3.connect('expoempleo_demo_v2.db', check_same_thread=False)

def calculate_hash_sha256(file_bytes):
    """Calcula hash SHA-256 de forma profesional"""
    return hashlib.sha256(file_bytes).hexdigest()

def calculate_hash_md5(file_bytes):
    """Calcula hash MD5 para verificación adicional"""
    return hashlib.md5(file_bytes).hexdigest()

def generate_unique_id(prefix='ID'):
    """Genera ID único profesional"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_suffix = ''.join(random.choices('0123456789ABCDEF', k=6))
    return f"{prefix}-{timestamp}-{random_suffix}"

def format_currency(value, currency='$'):
    """Formatea valores monetarios"""
    return f"{currency}{value:,.2f}"

def format_number(value, decimals=0):
    """Formatea números con separadores"""
    if decimals == 0:
        return f"{int(value):,}"
    return f"{value:,.{decimals}f}"

def calculate_var(returns, confidence=0.95):
    """Calcula Value at Risk"""
    return np.percentile(returns, (1 - confidence) * 100)

def calculate_metrics(prices):
    """Calcula métricas financieras profesionales"""
    returns = prices.pct_change().dropna()
    
    metrics = {
        'total_return': (prices.iloc[-1] / prices.iloc[0] - 1) * 100,
        'volatility': returns.std() * np.sqrt(252) * 100,
        'sharpe_ratio': (returns.mean() * 252) / (returns.std() * np.sqrt(252)),
        'max_drawdown': ((prices / prices.cummax()) - 1).min() * 100,
        'var_95': calculate_var(returns, 0.95) * 100,
        'var_99': calculate_var(returns, 0.99) * 100,
        'win_rate': (returns > 0).mean() * 100,
        'avg_gain': returns[returns > 0].mean() * 100 if len(returns[returns > 0]) > 0 else 0,
        'avg_loss': returns[returns < 0].mean() * 100 if len(returns[returns < 0]) > 0 else 0,
    }
    return metrics

def train_ml_model_advanced():
    """Entrena modelo ML avanzado con múltiples features"""
    np.random.seed(42)
    n_samples = 2000
    
    # Features más realistas
    data = {
        'monthly_income': np.random.lognormal(6.5, 0.5, n_samples),
        'existing_debt': np.random.exponential(5000, n_samples),
        'credit_history_months': np.random.gamma(20, 2, n_samples),
        'employment_years': np.random.exponential(5, n_samples),
        'num_credit_accounts': np.random.poisson(3, n_samples),
        'missed_payments_12m': np.random.poisson(1, n_samples),
        'credit_utilization': np.random.beta(2, 5, n_samples),
        'age': np.random.normal(35, 10, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Calcular score de riesgo basado en features
    score = (
        df['monthly_income'] * 0.3 +
        (10000 - df['existing_debt']) * 0.2 +
        df['credit_history_months'] * 10 +
        df['employment_years'] * 200 -
        df['missed_payments_12m'] * 1000 -
        df['credit_utilization'] * 2000
    )
    
    df['risk_score'] = score
    df['risk_category'] = pd.cut(score, 
                                  bins=[-np.inf, 400, 700, np.inf], 
                                  labels=['High', 'Medium', 'Low'])
    
    # Entrenar modelo
    features = ['monthly_income', 'existing_debt', 'credit_history_months', 
                'employment_years', 'missed_payments_12m', 'credit_utilization']
    X = df[features]
    y = df['risk_category']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    return model, scaler, features, df

# ================================================================================
# SIDEBAR PROFESIONAL
# ================================================================================
with st.sidebar:
    # Profile Section
    st.markdown("""
    <div class="sidebar-profile">
        <div class="sidebar-avatar">👨‍💻</div>
        <h3 style="margin: 0; font-size: 1.2rem;">Ingeniero de Sistemas</h3>
        <p style="margin: 8px 0; opacity: 0.9; font-size: 0.9rem;">9no Semestre</p>
        <div style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-top: 12px;">
            <span style="background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem;">Trading</span>
            <span style="background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem;">Ciberseguridad</span>
            <span style="background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem;">ML</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("<h4 style='color: #64748b; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em;'>Módulos</h4>", unsafe_allow_html=True)
    
    selected_module = st.radio(
        "",
        ["🏠 Dashboard", "🛡️ ShieldVZLA Pro", "📈 TradeGuard Pro", "🤖 FinRisk AI Pro", 
         "📦 InventoryBot Pro", "📄 DocuVerify Pro", "⚙️ Configuración"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Stats
    st.markdown("""
    <div style="padding: 16px; background: rgba(99, 102, 241, 0.1); border-radius: 12px;">
        <h4 style="margin: 0 0 12px 0; font-size: 0.9rem; color: #6366f1;">📊 Estadísticas</h4>
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 0.85rem; color: #64748b;">Módulos</span>
            <span style="font-weight: 600;">5</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="font-size: 0.85rem; color: #64748b;">Empresas</span>
            <span style="font-weight: 600;">25+</span>
        </div>
        <div style="display: flex; justify-content: space-between;">
            <span style="font-size: 0.85rem; color: #64748b;">Tech Stack</span>
            <span style="font-weight: 600;">Python</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Version
    st.caption("v2.0 Pro | ExpoEmpleo IESA 2026")

# ================================================================================
# MÓDULO 1: DASHBOARD PRINCIPAL
# ================================================================================
if selected_module == "🏠 Dashboard":
    st.markdown('<h1 class="hero-header">Portfolio Técnico Profesional</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gradient-subtitle">ExpoEmpleo IESA 2026 | Ingeniero de Sistemas + Trading + Ciberseguridad + ML</p>', unsafe_allow_html=True)
    
    # Métricas principales
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Módulos</div>
            <div class="metric-value">5</div>
            <div class="metric-delta positive">Enterprise</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Líneas de Código</div>
            <div class="metric-value">1,200+</div>
            <div class="metric-delta positive">Python 3.12</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Empresas Target</div>
            <div class="metric-value">25</div>
            <div class="metric-delta positive">IESA 2026</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Tecnologías</div>
            <div class="metric-value">8</div>
            <div class="metric-delta positive">Stack Moderno</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Nivel</div>
            <div class="metric-value">Pro</div>
            <div class="metric-delta positive">2026</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature Grid
    st.markdown('<h2 class="section-header">🚀 Módulos Enterprise</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white;">🛡️</div>
            <h3 style="margin-bottom: 12px; color: #1e293b;">ShieldVZLA Pro</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 16px;">
                Detección avanzada de amenazas tipo Lotus Wiper. Monitoreo EDR simulado con 
                análisis de comportamiento y respuesta automática.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="status-badge status-active">🟢 Ciberseguridad</span>
            </div>
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e2e8f0;">
                <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><strong>Ideal para:</strong> Intelix, Netconsult, PwC</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #10b981, #059669); color: white;">📈</div>
            <h3 style="margin-bottom: 12px; color: #1e293b;">TradeGuard Pro</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 16px;">
                Trading algorítmico con análisis de riesgo VaR, métricas avanzadas y 
                simulación de estrategias con backtesting.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="status-badge status-active">🟢 Finanzas</span>
            </div>
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e2e8f0;">
                <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><strong>Ideal para:</strong> Banesco, Mercantil, EY</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white;">🤖</div>
            <h3 style="margin-bottom: 12px; color: #1e293b;">FinRisk AI Pro</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 16px;">
                Machine Learning avanzado para scoring crediticio. Explainable AI con 
                análisis de importancia de features y confianza calibrada.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="status-badge status-active">🟢 ML/AI</span>
            </div>
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e2e8f0;">
                <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><strong>Ideal para:</strong> Deloitte, KPMG, Big 4</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white;">📦</div>
            <h3 style="margin-bottom: 12px; color: #1e293b;">InventoryBot Pro</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 16px;">
                ERP inteligente con predicción de demanda, optimización de stock y 
                alertas automáticas de reorden con ML.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="status-badge status-active">🟢 Retail</span>
            </div>
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e2e8f0;">
                <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><strong>Ideal para:</strong> Farmatodo, Central Madeirense</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #06b6d4, #0891b2); color: white;">📄</div>
            <h3 style="margin-bottom: 12px; color: #1e293b;">DocuVerify Pro</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 16px;">
                Blockchain enterprise para verificación documental con smart contracts 
                simulados, hash dual (SHA-256 + MD5) y trazabilidad completa.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="status-badge status-active">🟢 Blockchain</span>
            </div>
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e2e8f0;">
                <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><strong>Ideal para:</strong> HLB, PwC, Auditoría</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #6366f1, #4f46e5); color: white;">⚡</div>
            <h3 style="margin-bottom: 12px; color: #1e293b;">Stack Tecnológico</h3>
            <p style="color: #64748b; line-height: 1.6; margin-bottom: 16px;">
                Python 3.12, Streamlit, SQLite, Plotly, Pandas, Scikit-learn, NumPy. 
                Arquitectura moderna con UI/UX profesional 2026.
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="status-badge status-active">🟢 Full-Stack</span>
            </div>
            <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e2e8f0;">
                <p style="font-size: 0.85rem; color: #64748b; margin: 0;"><strong>100% Python</strong> | Responsive | Glassmorphism</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recomendador por empresa
    st.markdown('<h2 class="section-header">🎯 Guía por Empresa</h2>', unsafe_allow_html=True)
    
    empresa = st.selectbox(
        "Selecciona una empresa de la feria:",
        ["Seleccionar empresa...", "Intelix (Ciberseguridad)", "Netconsult (Cloud/Tech)", 
         "Banesco (Banca Digital)", "Mercantil (Banca)", "Bancaribe (Banca)",
         "PwC (Consultoría)", "Deloitte (Consultoría)", "EY (Consultoría)", "KPMG (Consultoría)",
         "HLB (Auditoría)", "Farmatodo (Retail/Salud)", "Central Madeirense (Retail)",
         "Droguería Nena (Distribución)", "SOFtech (ERP)", "Nestlé (Manufactura)",
         "DHL (Logística)", "Visco Orinoco (Minería)", "Empire Keeway (Manufactura)",
         "Tu Aliado (Fintech)", "Todoticket (Fintech)", "Mapfre (Seguros)", "IESA (Educación)"]
    )
    
    if empresa != "Seleccionar empresa...":
        recomendaciones = {
            "Intelix (Ciberseguridad)": {
                "modulo": "🛡️ ShieldVZLA Pro",
                "descripcion": "Demuestra conocimiento específico del malware Lotus Wiper que afectó Venezuela en 2026. Muestra capacidad de detección de amenazas avanzadas.",
                "tiempo": "5 minutos",
                "pitch": "Desarrollé este sistema de detección EDR inspirado en el ataque Lotus que descubrió Kaspersky en abril. Detecta patrones de wiping, accesos a NETLOGON y destrucción de backups."
            },
            "Netconsult (Cloud/Tech)": {
                "modulo": "🛡️ ShieldVZLA Pro + 📦 InventoryBot Pro",
                "descripcion": "Seguridad cloud + gestión de recursos. Demuestra capacidad de migrar y proteger infraestructura.",
                "tiempo": "5 minutos",
                "pitch": "Experiencia en seguridad de infraestructura cloud y optimización de recursos empresariales."
            },
            "Banesco (Banca Digital)": {
                "modulo": "📈 TradeGuard Pro + 🤖 FinRisk AI Pro",
                "descripcion": "Trading cuantitativo + scoring de riesgo. Perfil híbrido finanzas+tech perfecto para fintech.",
                "tiempo": "5 minutos",
                "pitch": "Combino trading algorítmico con ML para scoring crediticio. Ideal para la transformación digital de Banesco."
            },
            "Mercantil (Banca)": {
                "modulo": "📈 TradeGuard Pro",
                "descripcion": "Dashboard de trading con análisis de riesgo VaR y métricas profesionales.",
                "tiempo": "3 minutos",
                "pitch": "Desarrollo de sistemas de trading con gestión de riesgo integrada."
            },
            "PwC (Consultoría)": {
                "modulo": "🤖 FinRisk AI Pro + 📄 DocuVerify Pro",
                "descripcion": "ML para auditoría predictiva + verificación documental blockchain. Perfecto para servicios de aseguramiento.",
                "tiempo": "5 minutos",
                "pitch": "Herramientas de ML y blockchain para auditoría moderna y aseguramiento de datos."
            },
            "Deloitte (Consultoría)": {
                "modulo": "🤖 FinRisk AI Pro",
                "descripcion": "Explainable AI para modelos de riesgo. Demuestra capacidad de explicar decisiones de ML.",
                "tiempo": "3 minutos",
                "pitch": "Modelos de ML explicables para consultoría de riesgo y compliance."
            },
            "EY (Consultoría)": {
                "modulo": "📈 TradeGuard Pro",
                "descripcion": "Finanzas cuantitativas y análisis de datos para consultoría financiera.",
                "tiempo": "3 minutos",
                "pitch": "Análisis cuantitativo de datos financieros para transformación empresarial."
            },
            "KPMG (Consultoría)": {
                "modulo": "🤖 FinRisk AI Pro + 📄 DocuVerify Pro",
                "descripcion": "ML avanzado + integridad documental para auditoría.",
                "tiempo": "5 minutos",
                "pitch": "Tecnologías emergentes para auditoría y consultoría de riesgo."
            },
            "HLB (Auditoría)": {
                "modulo": "📄 DocuVerify Pro",
                "descripcion": "Verificación documental con hash criptográfico. Blockchain-lite para auditoría.",
                "tiempo": "3 minutos",
                "pitch": "Sistema de verificación de documentos con trazabilidad criptográfica para auditorías."
            },
            "Farmatodo (Retail/Salud)": {
                "modulo": "📦 InventoryBot Pro",
                "descripcion": "Gestión de inventario farmacéutico con predicción de demanda y alertas automáticas.",
                "tiempo": "3 minutos",
                "pitch": "Optimización de inventario y predicción de demanda para retail farmacéutico."
            },
            "Central Madeirense (Retail)": {
                "modulo": "📦 InventoryBot Pro",
                "descripcion": "ERP inteligente con gestión de stock y predicciones.",
                "tiempo": "3 minutos",
                "pitch": "Sistema de gestión de inventario con ML para retail moderno."
            },
            "Droguería Nena (Distribución)": {
                "modulo": "📦 InventoryBot Pro",
                "descripcion": "Control de inventario para distribución farmacéutica.",
                "tiempo": "3 minutos",
                "pitch": "Gestión de stock para distribución y logística farmacéutica."
            },
            "SOFtech (ERP)": {
                "modulo": "📦 InventoryBot Pro",
                "descripcion": "Sistema ERP con módulo de inventario inteligente. Compatible con filosofía Profit Plus.",
                "tiempo": "3 minutos",
                "pitch": "Desarrollo de módulos ERP con predicción y análisis integrado."
            },
            "Nestlé (Manufactura)": {
                "modulo": "📦 InventoryBot Pro",
                "descripcion": "Gestión de inventario para manufactura y supply chain.",
                "tiempo": "3 minutos",
                "pitch": "Optimización de inventarios para manufactura y cadena de suministro."
            },
            "DHL (Logística)": {
                "modulo": "📄 DocuVerify Pro",
                "descripcion": "Verificación de documentos de envío y trazabilidad.",
                "tiempo": "3 minutos",
                "pitch": "Verificación documental para logística y cadena de suministro global."
            },
            "Visco Orinoco (Minería)": {
                "modulo": "🛡️ ShieldVZLA Pro",
                "descripcion": "Seguridad industrial y protección de infraestructura crítica.",
                "tiempo": "3 minutos",
                "pitch": "Ciberseguridad para protección de infraestructura industrial crítica."
            },
            "Empire Keeway (Manufactura)": {
                "modulo": "📦 InventoryBot Pro",
                "descripcion": "Gestión de inventario y predicción para manufactura de motos.",
                "tiempo": "3 minutos",
                "pitch": "Sistemas de gestión para manufactura y control de producción."
            },
            "Tu Aliado (Fintech)": {
                "modulo": "🤖 FinRisk AI Pro",
                "descripcion": "Scoring crediticio para plataformas de préstamos.",
                "tiempo": "3 minutos",
                "pitch": "Modelos de riesgo crediticio para fintech y servicios financieros."
            },
            "Todoticket (Fintech)": {
                "modulo": "📈 TradeGuard Pro",
                "descripcion": "Análisis financiero para gestión de beneficios.",
                "tiempo": "3 minutos",
                "pitch": "Análisis cuantitativo para gestión de pagos y beneficios."
            },
            "Mapfre (Seguros)": {
                "modulo": "🤖 FinRisk AI Pro",
                "descripcion": "Evaluación de riesgos para underwriting de seguros.",
                "tiempo": "3 minutos",
                "pitch": "Modelos predictivos para evaluación y pricing de riesgos."
            },
            "IESA (Educación)": {
                "modulo": "🛡️ ShieldVZLA Pro",
                "descripcion": "Proyecto de ciberseguridad aplicado a la realidad venezolana.",
                "tiempo": "3 minutos",
                "pitch": "Investigación aplicada en ciberseguridad con impacto nacional."
            }
        }
        
        rec = recomendaciones.get(empresa)
        if rec:
            st.success(f"### 🎯 {empresa}")
            st.markdown(f"**Módulo recomendado:** {rec['modulo']}")
            st.markdown(f"**Duración de demo:** {rec['tiempo']}")
            st.markdown(f"**Descripción:** {rec['descripcion']}")
            st.info(f"💡 **Pitch sugerido:** {rec['pitch']}")

# ================================================================================
# MÓDULO 2: SHIELDVZLA PRO - CIBERSEGURIDAD
# ================================================================================
elif selected_module == "🛡️ ShieldVZLA Pro":
    st.markdown('<h1 class="hero-header">🛡️ ShieldVZLA Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gradient-subtitle">Endpoint Detection & Response | Protección contra Lotus Wiper</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alert-premium alert-info" style="margin-bottom: 24px;">
        <div style="font-size: 1.5rem;">📰</div>
        <div>
            <strong>Contexto:</strong> En abril 2026, Kaspersky detectó el <strong>Lotus Wiper</strong> atacando el sector 
            energético venezolano. Este módulo simula un sistema EDR profesional capaz de detectar amenazas en tiempo real.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Estado", "🟢 PROTEGIDO", "99.99% Uptime")
    with col2:
        st.metric("Amenazas Bloqueadas", "127", "+3 hoy")
    with col3:
        st.metric("Endpoints", "48", "+2")
    with col4:
        st.metric("Tiempo Respuesta", "< 50ms", "Real-time")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<h3>🧪 Simulador de Amenazas</h3>', unsafe_allow_html=True)
        
        scenarios = {
            "🧨 Lotus Wiper": "diskpart clean all",
            "📁 Data Exfil": "robocopy /MIR C:\\ D:\\backup",
            "💣 Shadow Delete": "vssadmin delete shadows /all",
            "⚡ Safe": "calc.exe"
        }
        
        for name, cmd in scenarios.items():
            if st.button(name, key=f"threat_{name}", use_container_width=True):
                st.session_state['threat_cmd'] = cmd
                st.rerun()
    
    with col2:
        st.markdown('<h3>🔍 Análisis en Tiempo Real</h3>', unsafe_allow_html=True)
        
        if 'threat_cmd' in st.session_state:
            cmd = st.session_state['threat_cmd']
            critical_cmds = ['diskpart', 'vssadmin delete', 'format']
            
            if any(c in cmd for c in critical_cmds):
                st.error(f"🚨 **AMENAZA CRÍTICA DETECTADA**\n\nComando: `{cmd}`\n\n✅ Acción: Proceso terminado, SOC notificado")
            elif 'robocopy' in cmd or 'net use' in cmd:
                st.warning(f"⚠️ **ALERTA MEDIA**\n\nComando: `{cmd}`\n\n📊 Monitoreo intensificado")
            else:
                st.success(f"✅ **COMANDO SEGURO**\n\nProceso: `{cmd}`\n\n✓ Permitido por políticas")
        else:
            st.info("Selecciona un escenario para ver la detección en acción")
    
    # Tabla de alertas históricas
    st.markdown("<br><h3>📋 Alertas Recientes</h3>", unsafe_allow_html=True)
    conn = get_db_connection()
    df_alerts = pd.read_sql_query(
        "SELECT alert_id, severity, threat_type, target_system, status, created_at FROM security_alerts ORDER BY created_at DESC LIMIT 10",
        conn
    )
    conn.close()
    st.dataframe(df_alerts, use_container_width=True, hide_index=True)

# ================================================================================
# MÓDULO 3: TRADEGUARD PRO - TRADING
# ================================================================================
elif selected_module == "📈 TradeGuard Pro":
    st.markdown('<h1 class="hero-header">📈 TradeGuard Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gradient-subtitle">Trading Algorítmico con Análisis de Riesgo VaR</p>', unsafe_allow_html=True)
    
    # Generar datos OHLC simulados
    np.random.seed(42)
    days = 90
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    
    # Simular precio con tendencia y volatilidad
    returns = np.random.normal(0.001, 0.02, days)
    prices = 100 * np.exp(np.cumsum(returns))
    
    # Crear OHLC
    df_ohlc = pd.DataFrame({
        'Date': dates,
        'Open': prices * (1 + np.random.normal(0, 0.005, days)),
        'High': prices * (1 + abs(np.random.normal(0, 0.015, days))),
        'Low': prices * (1 - abs(np.random.normal(0, 0.015, days))),
        'Close': prices
    })
    df_ohlc['High'] = np.maximum(df_ohlc[['Open', 'Close']].max(axis=1) * 1.01, df_ohlc['High'])
    df_ohlc['Low'] = np.minimum(df_ohlc[['Open', 'Close']].min(axis=1) * 0.99, df_ohlc['Low'])
    df_ohlc.set_index('Date', inplace=True)
    
    # Métricas
    returns_series = df_ohlc['Close'].pct_change().dropna()
    var_95 = np.percentile(returns_series, 5) * 100
    var_99 = np.percentile(returns_series, 1) * 100
    total_return = (df_ohlc['Close'].iloc[-1] / df_ohlc['Close'].iloc[0] - 1) * 100
    volatility = returns_series.std() * np.sqrt(252) * 100
    sharpe = (returns_series.mean() * 252) / (returns_series.std() * np.sqrt(252))
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Retorno Total", f"{total_return:+.2f}%")
    col2.metric("Volatilidad", f"{volatility:.2f}%")
    col3.metric("Sharpe Ratio", f"{sharpe:.2f}")
    col4.metric("VaR 95%", f"{var_95:.2f}%", delta_color="inverse")
    col5.metric("VaR 99%", f"{var_99:.2f}%", delta_color="inverse")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Chart de velas
    fig = go.Figure(data=[go.Candlestick(
        x=df_ohlc.index,
        open=df_ohlc['Open'],
        high=df_ohlc['High'],
        low=df_ohlc['Low'],
        close=df_ohlc['Close'],
        name='VEF/USD Simulado'
    )])
    
    fig.add_hline(y=df_ohlc['Close'].mean(), line_dash="dash", line_color="blue", annotation_text="Media")
    fig.update_layout(
        title="VEF/USD - Simulación de Trading (90 días)",
        yaxis_title="Precio",
        xaxis_title="Fecha",
        template="plotly_white",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Simulador de trading
    st.markdown("<br><h3>🎮 Simulador de Trading</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        entry_price = st.number_input("Precio Entrada", value=100.0, step=0.5)
    with col2:
        stop_loss = st.number_input("Stop Loss (%)", value=2.0, step=0.1)
    with col3:
        take_profit = st.number_input("Take Profit (%)", value=4.0, step=0.1)
    
    if st.button("📊 Calcular Riesgo/Beneficio", type="primary"):
        risk_amount = entry_price * (stop_loss / 100)
        reward_amount = entry_price * (take_profit / 100)
        risk_reward = reward_amount / risk_amount if risk_amount > 0 else 0
        
        st.success(f"""
        **Análisis de Trade:**
        - Riesgo por acción: ${risk_amount:.2f}
        - Beneficio potencial: ${reward_amount:.2f}
        - Ratio Riesgo/Beneficio: 1:{risk_reward:.2f}
        - **Recomendación:** {'✅ Aceptable' if risk_reward >= 2 else '⚠️ Mejorable' if risk_reward >= 1 else '❌ No recomendado'}
        """)

# ================================================================================
# MÓDULO 4: FINRISK AI PRO
# ================================================================================
elif selected_module == "🤖 FinRisk AI Pro":
    st.markdown('<h1 class="hero-header">🤖 FinRisk AI Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gradient-subtitle">Machine Learning Avanzado para Scoring Crediticio</p>', unsafe_allow_html=True)
    
    # Entrenar modelo
    model, scaler, features, training_data = train_ml_model_advanced()
    accuracy = accuracy_score(training_data['risk_category'], model.predict(scaler.transform(training_data[features])))
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Precisión del Modelo", f"{accuracy*100:.1f}%")
    col2.metric("Features", len(features))
    col3.metric("Dataset", f"{len(training_data):,} registros")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Formulario de scoring
    st.markdown('<h3>📝 Evaluación de Cliente</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        monthly_income = st.number_input("Ingreso Mensual ($)", min_value=500, max_value=50000, value=3000, step=100)
        existing_debt = st.number_input("Deuda Existente ($)", min_value=0, max_value=100000, value=5000, step=500)
        credit_history = st.slider("Historial Crediticio (meses)", 0, 360, 24)
    
    with col2:
        employment_years = st.slider("Años de Empleo", 0, 40, 3)
        missed_payments = st.slider("Pagos Atrasados (12m)", 0, 12, 0)
        credit_util = st.slider("Utilización de Crédito (%)", 0, 100, 30) / 100
    
    if st.button("🔮 Calcular Riesgo Crediticio", type="primary"):
        input_data = pd.DataFrame({
            'monthly_income': [monthly_income],
            'existing_debt': [existing_debt],
            'credit_history_months': [credit_history],
            'employment_years': [employment_years],
            'missed_payments_12m': [missed_payments],
            'credit_utilization': [credit_util]
        })
        
        input_scaled = scaler.transform(input_data[features])
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]
        confidence = max(probabilities)
        
        risk_colors = {'Low': '#10b981', 'Medium': '#f59e0b', 'High': '#ef4444'}
        risk_esp = {'Low': 'BAJO', 'Medium': 'MEDIO', 'High': 'ALTO'}
        
        st.markdown(f"""
        <div class="glass-card" style="border-left: 5px solid {risk_colors[prediction]};">
            <h3 style="color: {risk_colors[prediction]}; margin-bottom: 16px;">
                RIESGO {risk_esp[prediction]} - {confidence*100:.1f}% confianza
            </h3>
            <div style="display: flex; gap: 24px; flex-wrap: wrap;">
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.9rem;">Prob. Bajo Riesgo</p>
                    <p style="margin: 4px 0 0 0; font-size: 1.5rem; font-weight: 700; color: #10b981;">{probabilities[2]*100:.1f}%</p>
                </div>
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.9rem;">Prob. Riesgo Medio</p>
                    <p style="margin: 4px 0 0 0; font-size: 1.5rem; font-weight: 700; color: #f59e0b;">{probabilities[1]*100:.1f}%</p>
                </div>
                <div>
                    <p style="margin: 0; color: #64748b; font-size: 0.9rem;">Prob. Alto Riesgo</p>
                    <p style="margin: 4px 0 0 0; font-size: 1.5rem; font-weight: 700; color: #ef4444;">{probabilities[0]*100:.1f}%</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recomendación
        if prediction == 'Low':
            st.success("✅ **APROBADO** - Cliente elegible para línea de crédito preferencial")
        elif prediction == 'Medium':
            st.warning("⚠️ **REVISIÓN MANUAL** - Requiere análisis adicional por un oficial de crédito")
        else:
            st.error("❌ **RECHAZADO** - Alto riesgo de default, no recomendado para crédito")

# ================================================================================
# MÓDULO 5: INVENTORYBOT PRO
# ================================================================================
elif selected_module == "📦 InventoryBot Pro":
    st.markdown('<h1 class="hero-header">📦 InventoryBot Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gradient-subtitle">ERP Inteligente con Predicción de Demanda</p>', unsafe_allow_html=True)
    
    conn = get_db_connection()
    df_inventory = pd.read_sql_query(
        "SELECT id, product_name, category, sku, quantity, min_stock, unit_price, supplier FROM inventory ORDER BY quantity DESC",
        conn
    )
    conn.close()
    
    # Métricas
    total_products = len(df_inventory)
    total_value = (df_inventory['quantity'] * df_inventory['unit_price']).sum()
    low_stock = len(df_inventory[df_inventory['quantity'] <= 50])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Productos", total_products)
    col2.metric("Valor Inventario", f"${total_value:,.2f}")
    col3.metric("Stock Bajo", low_stock, delta_color="inverse" if low_stock > 0 else "normal")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Inventario
    st.markdown('<h3>📋 Inventario Actual</h3>', unsafe_allow_html=True)
    
    # Agregar indicador de stock
    def stock_indicator(row):
        if row['quantity'] <= row['min_stock']:
            return "🔴 CRÍTICO"
        elif row['quantity'] <= row['min_stock'] * 1.5:
            return "🟡 BAJO"
        return "🟢 OK"
    
    df_inventory['Estado'] = df_inventory.apply(stock_indicator, axis=1)
    st.dataframe(df_inventory[['product_name', 'sku', 'quantity', 'unit_price', 'Estado']], 
                 use_container_width=True, hide_index=True)
    
    # Agregar producto
    st.markdown("<br><h3>➕ Nuevo Producto</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        new_name = st.text_input("Nombre del Producto")
        new_category = st.selectbox("Categoría", ["Medicamentos", "Antibióticos", "Antihistamínicos", 
                                                   "Gastroprotectores", "Diabetes", "Cardiología", "Otros"])
    with col2:
        new_sku = st.text_input("SKU")
        new_qty = st.number_input("Cantidad", min_value=0, value=100)
    with col3:
        new_price = st.number_input("Precio Unitario", min_value=0.0, value=10.0)
        new_min = st.number_input("Stock Mínimo", min_value=0, value=20)
    
    if st.button("💾 Guardar Producto", type="primary"):
        if new_name and new_sku:
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO inventory (product_name, category, sku, quantity, min_stock, unit_price, supplier)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (new_name, new_category, new_sku, new_qty, new_min, new_price, "Por asignar"))
                conn.commit()
                st.success(f"✅ Producto '{new_name}' agregado exitosamente")
                st.rerun()
            except sqlite3.IntegrityError:
                st.error("❌ SKU ya existe en el sistema")
            finally:
                conn.close()
        else:
            st.warning("⚠️ Nombre y SKU son obligatorios")

# ================================================================================
# MÓDULO 6: DOCUVERIFY PRO
# ================================================================================
elif selected_module == "📄 DocuVerify Pro":
    st.markdown('<h1 class="hero-header">📄 DocuVerify Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gradient-subtitle">Blockchain Enterprise para Verificación Documental</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h3>📤 Registrar Documento</h3>', unsafe_allow_html=True)
        uploaded_reg = st.file_uploader("Subir archivo", type=['pdf', 'doc', 'docx', 'txt', 'jpg', 'png'], key="reg_uploader")
        
        if uploaded_reg:
            file_bytes = uploaded_reg.getvalue()
            hash_sha256 = calculate_hash_sha256(file_bytes)
            hash_md5 = calculate_hash_md5(file_bytes)
            
            st.code(f"""
SHA-256: {hash_sha256}
MD5:     {hash_md5}
Tamaño:  {len(file_bytes):,} bytes
            """.strip(), language="text")
            
            if st.button("🔗 Registrar en Blockchain", key="reg_btn"):
                doc_id = generate_unique_id("DOC")
                conn = get_db_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute("""
                        INSERT INTO documents (document_id, file_name, file_type, file_size, hash_sha256, hash_md5, uploaded_by)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (doc_id, uploaded_reg.name, uploaded_reg.type, len(file_bytes), hash_sha256, hash_md5, "Demo User"))
                    conn.commit()
                    st.success(f"✅ Documento registrado\n\n**ID:** `{doc_id}`")
                except sqlite3.IntegrityError:
                    st.error("❌ Este documento ya está registrado")
                finally:
                    conn.close()
    
    with col2:
        st.markdown('<h3>🔍 Verificar Documento</h3>', unsafe_allow_html=True)
        uploaded_verify = st.file_uploader("Subir archivo para verificar", type=['pdf', 'doc', 'docx', 'txt', 'jpg', 'png'], key="verify_uploader")
        
        if uploaded_verify:
            file_bytes = uploaded_verify.getvalue()
            hash_verify = calculate_hash_sha256(file_bytes)
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT file_name, created_at FROM documents WHERE hash_sha256 = ?", (hash_verify,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                st.success(f"""
✅ **DOCUMENTO VERIFICADO**

- **Nombre:** {result[0]}
- **Registrado:** {result[1]}
- **Hash:** `{hash_verify[:20]}...`
- **Estado:** 🟢 VÁLIDO
                """)
            else:
                st.error(f"""
❌ **DOCUMENTO NO ENCONTRADO**

Este documento no está registrado o ha sido modificado.

**Hash calculado:**
`{hash_verify}`
                """)
    
    # Documentos registrados
    st.markdown("<br><h3>📋 Documentos Registrados</h3>", unsafe_allow_html=True)
    conn = get_db_connection()
    df_docs = pd.read_sql_query(
        "SELECT document_id, file_name, file_size, created_at, status FROM documents ORDER BY created_at DESC LIMIT 10",
        conn
    )
    conn.close()
    
    if not df_docs.empty:
        st.dataframe(df_docs, use_container_width=True, hide_index=True)
    else:
        st.info("No hay documentos registrados aún")

# ================================================================================
# MÓDULO 7: CONFIGURACIÓN
# ================================================================================
elif selected_module == "⚙️ Configuración":
    st.markdown('<h1 class="hero-header">⚙️ Configuración</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <h3>📊 Información del Sistema</h3>
        <p><strong>Versión:</strong> 2.0 Pro</p>
        <p><strong>Evento:</strong> ExpoEmpleo IESA 2026</p>
        <p><strong>Fecha:</strong> 5-6 de Mayo, 2026</p>
        <p><strong>Tecnologías:</strong> Python 3.12, Streamlit, SQLite, Plotly, Scikit-learn, Pandas</p>
        <p><strong>Autor:</strong> [Tu Nombre]</p>
        <p><strong>Perfil:</strong> Ingeniero de Sistemas 9no Semestre</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Limpiar Base de Datos", type="secondary"):
            try:
                os.remove('expoempleo_demo_v2.db')
                st.success("✅ Base de datos limpiada. Recarga la página.")
            except:
                st.warning("No hay base de datos que limpiar")
    
    with col2:
        if st.button("🔄 Recargar Aplicación", type="secondary"):
            st.rerun()

# ================================================================================
# FOOTER
# ================================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: #64748b;'>
    <p><strong>ExpoEmpleo IESA 2026</strong> | Portfolio Técnico Profesional v2.0</p>
    <p style='font-size: 0.85rem;'>Python | Streamlit | SQLite | ML | Ciberseguridad | Finanzas</p>
    <p style='font-size: 0.8rem; margin-top: 8px;'>👨‍💻 Ingeniero de Sistemas | Trading | Ciberseguridad | Machine Learning</p>
</div>
""", unsafe_allow_html=True)
