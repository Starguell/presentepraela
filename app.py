from datetime import datetime
import time
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Para o meu amor 💙", page_icon="✨", layout="centered"
)

# Estilo visual: Órbita ajustada para o Sol não tampar a Lua + Sem REC
st.markdown(
    """
    <style>
    /* --- REMOVE A BARRA SUPERIOR E O MENU DO STREAMLIT --- */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Força o fundo preto e desenha a malha quadriculada no app inteiro */
    .stApp {
        background-color: #000000;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.08) 1px, transparent 1px);
        background-size: 40px 40px;
    }
    
    /* Textos com ótima leitura no fundo preto */
    h1, h2, h3 {
        color: #90e0ef !important;
        text-align: center;
        text-shadow: 0 0 10px rgba(144, 224, 239, 0.3);
    }
    p, label, .stMetricValue {
        color: #e0f2fe !important;
        text-align: center;
    }

    /* --- RELÓGIOS FLUTUANDO NO FUNDO --- */
    .floating-elements {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        pointer-events: none;
        z-index: 0;
    }
    .clock-particle {
        position: absolute;
        display: block;
        list-style: none;
        font-size: 22px;
        color: rgba(144, 224, 239, 0.3);
        bottom: -100px;
        animation: fly 16s infinite linear;
    }
    .clock-particle:nth-child(1) { left: 8%; font-size: 26px; animation-duration: 14s; }
    .clock-particle:nth-child(2) { left: 22%; font-size: 18px; animation-duration: 19s; animation-delay: 2s; }
    .clock-particle:nth-child(3) { left: 40%; font-size: 30px; animation-duration: 11s; animation-delay: 4s; }
    .clock-particle:nth-child(4) { left: 58%; font-size: 20px; animation-duration: 15s; animation-delay: 1s; }
    .clock-particle:nth-child(5) { left: 75%; font-size: 25px; animation-duration: 17s; animation-delay: 3s; }
    .clock-particle:nth-child(6) { left: 90%; font-size: 22px; animation-duration: 21s; animation-delay: 5s; }

    @keyframes fly {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 0.9;
        }
        100% {
            transform: translateY(-900px) rotate(360deg);
            opacity: 0;
        }
    }

    /* --- SISTEMA SOLAR MAIOR (ÓRBITA AMPLIADA PARA NADA SE TAMPAR) --- */
    .solar-system-container {
        display: flex;
        justify-content: center;
        margin: 40px 0;
        height: 180px;
        align-items: center;
    }
    .orbit-system {
        position: relative;
        width: 160px;
        height: 160px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    /* O Sol no centro (Você) */
    .sun-center {
        position: absolute;
        width: 55px;
        height: 55px;
        background: radial-gradient(circle, #ffcc00, #ff6600);
        border-radius: 50%;
        box-shadow: 0 0 25px rgba(255, 165, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        z-index: 2;
        cursor: pointer;
    }
    .sun-center .label-sun {
        position: absolute;
        bottom: -32px;
        background: rgba(0, 0, 0, 0.85);
        color: #ffcc00;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 12px;
        font-weight: bold;
        opacity: 0;
        transition: opacity 0.3s ease;
        white-space: nowrap;
        border: 1px solid rgba(255, 204, 0, 0.4);
    }
    .sun-center:hover .label-sun {
        opacity: 1;
    }

    /* Órbita maior onde a lua gira */
    .moon-orbit {
        position: absolute;
        width: 160px;
        height: 160px;
        border-radius: 50%;
        animation: spin 7s linear infinite;
    }
    /* A Lua girando bem afastada (Eu) com o texto para cima para nunca ser tampada */
    .moon-item {
        position: absolute;
        top: 5px;
        left: 65px;
        width: 30px;
        height: 30px;
        background: radial-gradient(circle, #e2e8f0, #94a3b8);
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(148, 163, 184, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        cursor: pointer;
    }
    .moon-item .label-moon {
        position: absolute;
        top: -30px;
        background: rgba(0, 0, 0, 0.85);
        color: #90e0ef;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 11px;
        font-weight: bold;
        opacity: 0;
        transition: opacity 0.3s ease;
        white-space: nowrap;
        border: 1px solid rgba(144, 224, 239, 0.4);
        z-index: 10;
    }
    .moon-item:hover .label-moon {
        opacity: 1;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>

    <!-- Relógios flutuantes no fundo -->
    <div class="floating-elements">
        <span class="clock-particle">⏰</span>
        <span class="clock-particle">⏳</span>
        <span class="clock-particle">⭐</span>
        <span class="clock-particle">⏱️</span>
        <span class="clock-particle">✨</span>
        <span class="clock-particle">🕰️</span>
    </div>
""",
    unsafe_allow_html=True,
)

# Título principal
st.markdown(
    "<h1>Feliz por ter você ao meu lado! 💙</h1>", unsafe_allow_html=True
)
st.write(
    "Registrando cada instante, segundo e milissegundo do nosso tempo juntos."
)

# --- ANIMAÇÃO DO SOL E DA LUA ORBITANDO ---
st.markdown(
    """
    <div class="solar-system-container">
        <div class="orbit-system">
            <!-- Sol no Centro (Você) -->
            <div class="sun-center">
                ☀️
                <div class="label-sun">Você (O Sol)</div>
            </div>
            <!-- Lua Orbitando (Eu) com órbita maior e label posicionada em cima -->
            <div class="moon-orbit">
                <div class="moon-item">
                    🌙
                    <div class="label-moon">Eu (A Lua)</div>
                </div>
            </div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# --- CITAÇÃO SOBRE A RELATIVIDADE DO TEMPO ---
st.markdown(
    """
    <div style="background-color: rgba(144, 224, 239, 0.08); padding: 15px; border-radius: 10px; border-left: 4px solid #90e0ef; margin-bottom: 20px; margin-top: 15px;">
        <p style="font-style: italic; color: #e0f2fe; margin: 0; font-size: 16px; text-align: center;">
            "A teoria da relatividade diz que o tempo depende do observador... 
            e para mim, o meu universo inteiro se resume a cada segundo com você." 🌌✨
        </p>
    </div>
""",
    unsafe_allow_html=True,
)

st.divider()

# --- CONTAGEM COM O NOVO TÍTULO ---
st.subheader("🪐 A minha órbita em vc dura...")

# Data e hora exatas do início do namoro (12 de maio de 2025, às 12:26)
inicio_namoro = datetime(2025, 5, 12, 12, 26)

# Criamos um espaço reservado (placeholder) para atualizar a tela sem piscar tudo
placeholder = st.empty()

# Loop para manter a contagem rodando na tela em tempo real
for _ in range(100000):
  hoje = datetime.now()
  diferenca = hoje - inicio_namoro

  # Cálculos precisos
  total_segundos = int(diferenca.total_seconds())
  dias_totais = diferenca.days

  anos = dias_totais // 365
  meses = (dias_totais % 365) // 30
  dias = (dias_totais % 365) % 30

  horas = (total_segundos % 86400) // 3600
  minutos = (total_segundos % 3600) // 60
  segundos = total_segundos % 60
  milissegundos = int((diferenca.microseconds / 1000))

  # Exibindo no layout do Streamlit dentro do loop
  with placeholder.container():
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Anos", f"{anos}")
    c2.metric("Meses", f"{meses}")
    c3.metric("Dias", f"{dias}")
    c4.metric("Horas", f"{horas:02d}")
    c5.metric("Seg", f"{segundos:02d}")
    c6.metric("Ms", f"{milissegundos:03d}")

  # Pausa de 0.05 segundos para atualizar os milissegundos de forma fluida
  time.sleep(0.05)

st.divider()

# --- MENSAGEM ESPECIAL ---
st.subheader("💌 Uma mensagem para você")
st.info(
    "Cada ano, segundo e milissegundo ao seu lado vale a pena. Obrigado por"
    " ser quem você é! 💙"
)