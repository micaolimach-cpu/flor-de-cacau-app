import streamlit as st
from datetime import date, time
from urllib.parse import quote

# --- Configuração da página ---
st.set_page_config(page_title="Flor de Cacau", page_icon="🍫", layout="centered")

# --- Estilo visual ---
st.markdown("""
<style>
body {
    background-color: #FFF5F5;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    color: #6B3E26;
    font-weight: 600;
}
.stButton>button {
    background-color: #A94438;
    color: white;
    border-radius: 8px;
    font-size: 1rem;
    padding: 0.6rem 1.2rem;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #8C2F24;
}
.stTextInput>div>input, .stTextArea>div>textarea {
    background-color: #FFF0E6;
    border: 1px solid #D2B48C;
    border-radius: 6px;
}
/* Estilo para Number Input: tenta centralizar o texto dentro do campo */
div[data-testid="stNumberInput"] div input {
    text-align: center;
}
/* Estilo para garantir que o botão de confirmação tenha o estilo rosa */
div.stButton button[data-testid*="stButton-primary"] {
    background-color: #F8BBD0; 
    color: #6B3E26; 
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    padding: 0.8rem 1.5rem;
    width: 100%;
    margin-top: 1rem;
}
div.stButton button[data-testid*="stButton-primary"]:hover {
    background-color: #F48FB1; 
}
</style>
""", unsafe_allow_html=True)

# --- Banner de entrada ---
st.markdown("<h1 style='text-align: center;'>Flor de Cacau</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Kits de Brigadeiro para Eventos, Festas & Confraternizações</p>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.button("🍬 Começar pedido")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- Nossos Kits Especiais (LAYOUT OTIMIZADO) ---
st.subheader("🎁 Nossos Kits Especiais")

kits = [
    {"name": "Kit Pequeno", "desc": "Perfeito para degustação", "qty": 6, "price": 18.00},
    {"name": "Kit Médio", "desc": "Ideal para presentear", "qty": 12, "price": 33.00},
    {"name": "Kit Grande", "desc": "Ótimo para os amantes de brigadeiro", "qty": 24, "price": 60.00},
    {"name": "Kit Mega", "desc": "Para festas e eventos maiores (100-1000 unidades)", "qty": 100, "price": 210.00},
]

# Layout em 2 colunas para melhor simetria
cols = st.columns(2) 
for i, kit in enumerate(kits):
    with cols[i % 2]: 
        st.markdown(f"""
        <div style="
            background-color:#FFF0E6;
            border:1px solid #E0C4A8;
            border-radius:12px;
            padding:1rem;
            margin-bottom:1rem;
            text-align:center;
            box-shadow:0 2px 6px rgba(0,0,0,0.1);
        ">
            <h3 style="color:#6B3E26;">{kit['name']}</h3>
            <p>{kit['desc']}</p>
            <p>📦 {kit['qty']} unidades</p>
            <p><b>💰 R$ {kit['price']:.2f}</b></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Quero esse", key=f"btn_{kit['name']}"):
            st.session_state["kit_escolhido"] = kit

st.markdown("---")

# --- Seleção de sabores (CUSTOMIZADA E CORRIGIDA) ---
if "kit_escolhido" in st.session_state:
    kit = st.session_state["kit_escolhido"]

    # Kit Mega: cliente define quantidade entre 100 e 1000
    if kit["name"] == "Kit Mega":
        qtd_mega = st.number_input("Quantidade de brigadeiros", min_value=100, max_value=1000, step=10)
        kit["qty"] = qtd_mega
        kit["price"] = qtd_mega * 2.10
        st.session_state["kit_escolhido"] = kit
        st.info(f"{qtd_mega} unidades selecionadas - R$ {kit['price']:.2f}")

    total_unidades = kit["qty"]

    
    st.markdown(f"## 🍬 Monte seu {kit['name']}")
    st.write(f"Selecione os sabores até completar **{total_unidades} unidades**")

    flavors = [
        {"name": "Tradicional", "icon": "🍫"},
        {"name": "Beijinho", "icon": "🥥"},
        {"name": "Morango", "icon": "🍓"},
        {"name": "Maracujá", "icon": "🥭"},
        {"name": "Oreo", "icon": "🍪"},
        {"name": "Ninho", "icon": "🥛"},
        {"name": "Café", "icon": "☕"},
        {"name": "Paçoca", "icon": "🥜"},
        {"name": "Churros", "icon": "🍩"},
    ]

    # CÁLCULO DE SOMA para exibir o progresso
    soma = sum(st.session_state.get(f"flavor_{flavor['name']}", 0) for flavor in flavors)

    # BLOCO DE PROGRESSO COM ESTILO DE CAIXA (SÓ TEXTO)
    st.markdown(f"""
        <div style="
            background-color:#FFF5E6; 
            border:1px solid #FFD799; 
            border-radius:8px; 
            padding:10px; 
            margin-bottom:0.5rem; /* Margem ajustada para inserir o progress bar abaixo */
        ">
            <p style='margin-bottom:0.5rem; font-weight:500;'>
                Instruções: Selecione a quantidade de cada sabor até completar o total de unidades do kit
            </p>
            <p style='margin:0; font-weight:600;'>Progresso: 
                <span style='float:right;'>{soma} de {total_unidades} unidades</span>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # BARRA DE PROGRESSO REAL (FORA DO MARKDOWN HTML para funcionar)
    # CORREÇÃO APLICADA: Movemos st.progress para fora do bloco markdown
    st.progress(min(soma / total_unidades, 1.0))
    
    # LAYOUT EM DUAS COLUNAS PARA SABORES
    selected_flavors = {}
    cols = st.columns(2) 
    
    for i, flavor in enumerate(flavors):
        with cols[i % 2]: 
            # Estilo de caixa para o sabor
            st.markdown(f"""
            <div style="
                background-color:#FFFFFF; 
                border:1px solid #D2B48C; 
                border-radius:8px; 
                padding:0.5rem; 
                margin-bottom:1rem;
                box-shadow:0 1px 3px rgba(0,0,0,0.05);
            ">
                <p style="color:#6B3E26; margin:0.2rem 0; font-weight:600;">{flavor['icon']} {flavor['name']}</p>
            """, unsafe_allow_html=True)

            # O st.number_input é usado para a seleção de quantidade
            qtd = st.number_input(
                "Quantidade", 
                min_value=0,
                max_value=total_unidades,
                step=1,
                key=f"flavor_{flavor['name']}",
                label_visibility="collapsed" # Esconde o label
            )
            
            st.markdown("</div>", unsafe_allow_html=True)
            
    # RE-CÁLCULO DE SOMA para a lógica de confirmação
    selected_flavors = {}
    soma = 0
    for flavor in flavors:
        qtd = st.session_state.get(f"flavor_{flavor['name']}", 0)
        if qtd > 0:
            selected_flavors[flavor["name"]] = qtd
            soma += qtd

    # Botão de confirmação
    if soma == total_unidades:
        
        if st.button("Confirmar Adicionar ao Pedido", type="primary"):
            st.session_state["pedido"] = {
                "kit": kit,
                "sabores": selected_flavors
            }
            st.success("Pedido adicionado com sucesso! 🎉")
    else:
        st.warning("Complete todas as unidades do kit antes de confirmar.")

st.markdown("---")

# --- Dados do cliente (CUSTOMIZADA) ---
if "pedido" in st.session_state:
    st.subheader("📄 Dados do Cliente")

    # Layout em duas colunas para Nome/Data e Horário
    col1, col2 = st.columns(2)
    
    with col1:
        nome_cliente = st.text_input("👤 Nome do cliente")
        data_entrega = st.date_input("📅 Data de entrega", min_value=date.today())
    
    with col2:
        # Coluna 2 é usada apenas para o Horário de entrega
        st.markdown("<p style='visibility: hidden;'>Nome placeholder</p>", unsafe_allow_html=True)
        horario_entrega = st.time_input("⏰ Horário de entrega", value=time(14, 0))
        
    st.markdown("---")
    
    st.markdown("#### 🚚 Opções de Entrega")
    entrega_opcao = st.radio(
        "Forma de entrega", 
        ["Entrega no endereço", "Retirada no local"], 
        key="entrega_radio",
        horizontal=True, 
        label_visibility="collapsed" 
    )

    st.markdown("---")
    
    obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: sem coco, embalar separadamente...")

    if st.button("📲 Finalizar pedido no WhatsApp"):
        phone = "5551992860852"
        pedido = st.session_state["pedido"]
        
        # INÍCIO DA MENSAGEM DO WHATSAPP ORGANIZADA EM TÓPICOS
        
        # 1. Cabeçalho e Resumo do Kit
        message = "*🍫 NOVO PEDIDO - FLOR DE CACAU*\\n\\n"
        message += "*--- RESUMO DO PEDIDO ---*\\n"
        message += f"*- Kit:* {pedido['kit']['name']} ({pedido['kit']['qty']} unidades)\\n"
        message += f"*- TOTAL:* R$ {pedido['kit']['price']:.2f}\\n\\n"

        # 2. Seção de Sabores (Tópicos)
        message += "*--- SABORES SELECIONADOS ---*\\n"
        for sabor, qtd in pedido["sabores"].items():
            message += f"*{qtd}x* {sabor}\\n" # Quantidade em negrito
        message += "\\n"
        
        # 3. Detalhes do Cliente e Entrega (Tópicos)
        message += "*--- DADOS DA ENTREGA/CLIENTE ---*\\n"

        if nome_cliente:
            message += f"*- Cliente:* {nome_cliente}\\n"
        if data_entrega:
            message += f"*- Data de Entrega:* {data_entrega.strftime('%d/%m/%Y')}\\n"
        if horario_entrega:
            message += f"*- Horário:* {horario_entrega.strftime('%H:%M')}\\n"
        if entrega_opcao:
            message += f"*- Forma de Entrega:* {entrega_opcao}\\n"
        if obs:
            message += f"*- Observações:* {obs}\\n"
            
        # FIM DA MENSAGEM DO WHATSAPP ORGANIZADA
        
        url = f"https://wa.me/{phone}?text={quote(message)}"
        st.markdown(f"[👉 Abrir WhatsApp]({url})", unsafe_allow_html=True)

st.markdown("---")

# --- Pagamentos aceitos ---
st.markdown("""
<div style="
    background-color:#FFF0E6;
    border:1px solid #E0C4A8;
    border-radius:12px;
    padding:1rem;
    text-align:center;
    margin-bottom:1rem;
">
    <h4 style="color:#6B3E26;">💳 Formas de Pagamento</h4>
    <p>✔️ Aceitamos cartões: Visa, MasterCard, Elo, Hipercard</p>
    <p>✔️ Pagamento via <b>PIX</b></p>
</div>
""", unsafe_allow_html=True)

# --- Rodapé ---
st.markdown("""
<div style="
    background-color:#6B3E26;
    color:white;
    text-align:center;
    padding:1rem;
    border-radius:8px;
    margin-top:2rem;
">
    &copy; 2025 Flor de Cacau Confeitaria - Ingredientes frescos, produtores locais e chocolate nobre.<br>
    Feito com ❤️ em Porto Alegre - RS<br>
    📍 Endereço: Avenida Antonio de Carvalho, 2600 - Ap 170<br>
    <a href="https://www.instagram.com/confeitariaflordcacau/" target="_blank" style="color:#FFD700; text-decoration:none;">
        📸 Instagram: @confeitariaflordcacau
    </a>
</div>
""", unsafe_allow_html=True)
                               
