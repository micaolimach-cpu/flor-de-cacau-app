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
</style>
""", unsafe_allow_html=True)

# --- Banner de entrada ---
st.markdown("### Flor de Cacau 🍫")
st.markdown("<h1 style='text-align: center;'>Flor de Cacau</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Kits de Brigadeiro para Eventos, Festas & Confraternizações</p>", unsafe_allow_html=True)

# --- Botão de entrada ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.button("🍬 Começar pedido")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")# --- Nossos Kits Especiais ---
st.subheader("🎁 Nossos Kits Especiais")

kits = [
    {"name": "Kit Pequeno", "desc": "Perfeito para degustação", "qty": 6, "price": 18.00},
    {"name": "Kit Médio", "desc": "Ideal para presentear", "qty": 12, "price": 33.00},
    {"name": "Kit Grande", "desc": "Ótimo para os amantes de brigadeiro", "qty": 24, "price": 60.00},
    {"name": "Kit Premium", "desc": "Para aquele evento de última hora", "qty": 50, "price": 120.00},
    {"name": "Kit Especial", "desc": "Para confraternizações médias", "qty": 75, "price": 165.00},
    {"name": "Kit Mega", "desc": "Para festas e eventos maiores (100-1000 unidades)", "qty": 100, "price": 210.00},
]

cols = st.columns(3)
for i, kit in enumerate(kits):
    with cols[i % 3]:
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
            st.session_state["kit_escolhido"] = kit# --- Sabores disponíveis ---
st.subheader("🍬 Sabores Disponíveis")

flavors = [
    {"id": 1, "name": "Tradicional", "icon": "🍫"},
    {"id": 2, "name": "Leite Ninho", "icon": "🥛"},
    {"id": 3, "name": "Morango", "icon": "🍓"},
    {"id": 4, "name": "Meio Amargo", "icon": "🍫"},
    {"id": 5, "name": "Oreo", "icon": "🍪"},
    {"id": 6, "name": "Nutella", "icon": "🍯"},
    {"id": 7, "name": "Coco", "icon": "🥥"},
    {"id": 8, "name": "Paçoca", "icon": "🥜"},
    {"id": 9, "name": "Churros", "icon": "🍩"},
]

cols = st.columns(3)
for i, flavor in enumerate(flavors):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="
            background-color:#FFF0E6;
            border:1px solid #E0C4A8;
            border-radius:12px;
            padding:0.8rem;
            margin-bottom:1rem;
            text-align:center;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#6B3E26;">{flavor['icon']} {flavor['name']}</h4>
        </div>
        """, unsafe_allow_html=True)# --- Seção institucional ---
st.subheader("❤️ Feito com Amor")

st.markdown("""
<div style="
    background-color:#FFF0E6;
    border:1px solid #E0C4A8;
    border-radius:12px;
    padding:1.5rem;
    margin-bottom:1rem;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
">
    <p style="color:#6B3E26; font-size:1.1rem;">
        Nossos brigadeiros são feitos com <b>ingredientes selecionados</b>, 
        chocolate nobre e receitas tradicionais. 
        Produção artesanal, sem conservantes e com muito carinho em cada detalhe.
    </p>
    <ul style="color:#6B3E26; font-size:1rem;">
        <li>🌱 Ingredientes frescos</li>
        <li>👩‍🍳 Produção artesanal</li>
        <li>🚫 Sem conservantes</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")# --- Carrinho ---
st.subheader("🛒 Seu Pedido")

if "kit_escolhido" not in st.session_state:
    st.info("Selecione um kit para começar seu pedido.")
else:
    kit = st.session_state["kit_escolhido"]
    st.markdown(f"### Kit escolhido: {kit['name']} ({kit['qty']} unidades)")
    st.write(f"💰 Valor: R$ {kit['price']:.2f}")

    # --- Resumo dos sabores ---
    st.markdown("### Sabores selecionados")
    selected_flavors = {}
    total_price = 0.0

    for flavor in ["Tradicional", "Leite Ninho", "Morango", "Meio Amargo", "Oreo", "Nutella", "Coco", "Paçoca", "Churros"]:
        qtd = st.number_input(f"{flavor}", min_value=0, max_value=kit["qty"], step=1, key=f"pedido_{flavor}")
        if qtd > 0:
            selected_flavors[flavor] = qtd
            # preço fictício médio
            preco_unit = 3.00 if flavor in ["Tradicional", "Leite Ninho", "Morango"] else 3.50
            total_price += qtd * preco_unit

    st.markdown(f"**Total estimado: R$ {total_price:.2f}**")

    # --- Dados do cliente ---
    st.markdown("### 📄 Dados do Cliente")
    nome_cliente = st.text_input("👤 Nome do cliente")
    data_entrega = st.date_input("📅 Data de entrega", min_value=date.today())
    horario_entrega = st.time_input("⏰ Horário de entrega", value=time(14, 0))
    obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: sem coco, embalar separadamente...")

    # --- Opção de entrega ---
    st.markdown("### 🚚 Forma de Entrega")
    entrega_opcao = st.radio("Escolha a forma de entrega:", ["Entrega no endereço", "Retirada no local"])

    # --- Botão WhatsApp ---
    if st.button("📲 Finalizar pedido no WhatsApp"):
        phone = "5551992860852"
        message = "*🍫 NOVO PEDIDO - FLOR DE CACAU*\\n\\n"
        message += f"Kit escolhido: {kit['name']} ({kit['qty']} unidades)\\n\\n"
        for sabor, qtd in selected_flavors.items():
            message += f"{qtd}x {sabor}\\n"
        message += f"\\n*TOTAL: R$ {total_price:.2f}*\\n"

        if nome_cliente:
            message += f"\\n👤 Cliente: {nome_cliente}"
        if data_entrega:
            message += f"\\n📅 Entrega: {data_entrega.strftime('%d/%m/%Y')}"
        if horario_entrega:
            message += f"\\n⏰ Horário: {horario_entrega.strftime('%H:%M')}"
        if entrega_opcao:
            message += f"\\n🚚 Forma de entrega: {entrega_opcao}"
        if obs:
            message += f"\\n📝 Observações: {obs}"

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
# --- Carrinho ---
st.subheader("🛒 Seu Pedido")

if "kit_escolhido" not in st.session_state:
    st.info("Selecione um kit para começar seu pedido.")
else:
    kit = st.session_state["kit_escolhido"]
    st.markdown(f"### Kit escolhido: {kit['name']} ({kit['qty']} unidades)")
    st.write(f"💰 Valor: R$ {kit['price']:.2f}")

    # --- Resumo dos sabores ---
    st.markdown("### Sabores selecionados")
    selected_flavors = {}
    total_price = 0.0

    for flavor in ["Tradicional", "Leite Ninho", "Morango", "Meio Amargo", "Oreo", "Nutella", "Coco", "Paçoca", "Churros"]:
        qtd = st.number_input(f"{flavor}", min_value=0, max_value=kit["qty"], step=1, key=f"pedido_{flavor}")
        if qtd > 0:
            selected_flavors[flavor] = qtd
            # preço fictício médio
            preco_unit = 3.00 if flavor in ["Tradicional", "Leite Ninho", "Morango"] else 3.50
            total_price += qtd * preco_unit

    st.markdown(f"**Total estimado: R$ {total_price:.2f}**")

    # --- Dados do cliente ---
    st.markdown("### 📄 Dados do Cliente")
    nome_cliente = st.text_input("👤 Nome do cliente")
    data_entrega = st.date_input("📅 Data de entrega", min_value=date.today())
    horario_entrega = st.time_input("⏰ Horário de entrega", value=time(14, 0))
    obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: sem coco, embalar separadamente...")

    # --- Botão WhatsApp ---
    if st.button("📲 Finalizar pedido no WhatsApp"):
        phone = "5551992860852"
        message = "*🍫 NOVO PEDIDO - FLOR DE CACAU*\\n\\n"
        message += f"Kit escolhido: {kit['name']} ({kit['qty']} unidades)\\n\\n"
        for sabor, qtd in selected_flavors.items():
            message += f"{qtd}x {sabor}\\n"
        message += f"\\n*TOTAL: R$ {total_price:.2f}*\\n"

        if nome_cliente:
            message += f"\\n👤 Cliente: {nome_cliente}"
        if data_entrega:
            message += f"\\n📅 Entrega: {data_entrega.strftime('%d/%m/%Y')}"
        if horario_entrega:
            message += f"\\n⏰ Horário: {horario_entrega.strftime('%H:%M')}"
        if obs:
            message += f"\\n📝 Observações: {obs}"

        url = f"https://wa.me/{phone}?text={quote(message)}"
        st.markdown(f"[👉 Abrir WhatsApp]({url})", unsafe_allow_html=True)

st.markdown("---")

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
    Feito com ❤️ em Esteio - RS<br>
    <a href="https://www.instagram.com/confeitariaflordcacau/" target="_blank" style="color:#FFD700; text-decoration:none;">
        📸 Instagram: @confeitariaflordcacau
    </a>
</div>
""", unsafe_allow_html=True)





