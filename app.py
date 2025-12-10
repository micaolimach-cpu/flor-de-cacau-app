import streamlit as st
from datetime import date, time
from urllib.parse import quote

# --------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------
st.set_page_config(page_title="Flor de Cacau", page_icon="🍫", layout="centered")

# --------------------------------------------
# ESTILO PREMIUM
# --------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #FAF3EF !important;
}

/* Títulos */
h1, h2, h3, h4 {
    color: #5A2E1B !important;
    font-weight: 600;
}

/* Seções */
.section {
    background-color: #FFF7F3;
    border: 1px solid #E8D5C4;
    padding: 1.4rem;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    margin-bottom: 2rem;
}

/* Botões */
.stButton>button {
    background: linear-gradient(135deg, #B45F04, #8C3A06);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 0.7rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
    transition: transform .2s ease, background .2s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #8C3A06, #6E2A04);
}

/* Inputs */
.stTextInput>div>input,
.stTextArea>div>textarea,
.stNumberInput input {
    background-color: #FFF4EA !important;
    border: 1px solid #DEBFA7 !important;
    border-radius: 10px;
    padding: 0.5rem;
}

/* Cards dos Kits */
.kit-card {
    background-color:#FFF4EA;
    border:1px solid #E4C9B0;
    padding:1rem;
    border-radius:14px;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
    transition: transform .2s ease;
    text-align:center;
}
.kit-card:hover {
    transform: scale(1.02);
}

/* Barra de progresso */
.stProgress > div > div {
    background-image: linear-gradient(to right, #B45F04 , #E69A57);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------
# BANNER
# --------------------------------------------
st.markdown("<h1 style='text-align: center;'>🍫 Flor de Cacau</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Kits de Brigadeiro para Eventos, Festas & Confraternizações</p>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.button("🍬 Começar pedido")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------
# KITS DISPONÍVEIS
# --------------------------------------------
st.subheader("🎁 Nossos Kits Especiais")

kits = [
    {"name": "Kit Pequeno", "desc": "Perfeito para degustação", "qty": 6, "price": 18.00},
    {"name": "Kit Médio", "desc": "Ideal para presentear", "qty": 12, "price": 33.00},
    {"name": "Kit Grande", "desc": "Ótimo para os amantes de brigadeiro", "qty": 24, "price": 60.00},
    {"name": "Kit Mega", "desc": "Para festas e eventos maiores (100-1000 unidades)", "qty": 100, "price": 210.00},
]

cols = st.columns(3)
for i, kit in enumerate(kits):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="kit-card">
            <h3 style="color:#5A2E1B;">{kit['name']}</h3>
            <p>{kit['desc']}</p>
            <p>📦 {kit['qty']} unidades</p>
            <p style="font-size:1.2rem;"><b>💰 R$ {kit['price']:.2f}</b></p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Quero esse", key=f"btn_{kit['name']}"):
            st.session_state["kit_escolhido"] = kit

st.markdown("---")

# --------------------------------------------
# SELEÇÃO DE SABORES
# --------------------------------------------
if "kit_escolhido" in st.session_state:
    kit = st.session_state["kit_escolhido"]

    st.markdown('<div class="section">', unsafe_allow_html=True)

    # Kit Mega permite escolher quantidade
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

    selected_flavors = {}
    soma = 0
    cols = st.columns(3)
    for i, flavor in enumerate(flavors):
        with cols[i % 3]:
            qtd = st.number_input(
                f"{flavor['icon']} {flavor['name']}",
                min_value=0,
                max_value=total_unidades,
                step=1,
                key=f"flavor_{flavor['name']}"
            )
            if qtd > 0:
                selected_flavors[flavor["name"]] = qtd
                soma += qtd

    st.progress(min(soma / total_unidades, 1.0))
    st.write(f"**{soma} de {total_unidades} unidades selecionadas**")

    if soma == total_unidades:
        if st.button("✅ Confirmar e Adicionar ao Pedido"):
            st.session_state["pedido"] = {
                "kit": kit,
                "sabores": selected_flavors
            }
            st.success("Pedido adicionado com sucesso! 🎉")
    else:
        st.warning("Complete todas as unidades do kit antes de confirmar.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------
# DADOS DO CLIENTE
# --------------------------------------------
if "pedido" in st.session_state:

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("📄 Dados do Cliente")

    nome_cliente = st.text_input("👤 Nome do cliente")
    data_entrega = st.date_input("📅 Data de entrega", min_value=date.today())
    horario_entrega = st.time_input("⏰ Horário de entrega", value=time(14, 0))
    entrega_opcao = st.radio("🚚 Forma de entrega", ["Entrega no endereço", "Retirada no local"])
    obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: sem coco, embalar separadamente...")

    if st.button("📲 Finalizar pedido no WhatsApp"):
        phone = "5551992860852"
        pedido = st.session_state["pedido"]

        message = "*🍫 NOVO PEDIDO - FLOR DE CACAU*\\n\\n"
        message += f"Kit escolhido: {pedido['kit']['name']} ({pedido['kit']['qty']} unidades)\\n\\n"

        for sabor, qtd in pedido["sabores"].items():
            message += f"{qtd}x {sabor}\\n"

        message += f"\\n*TOTAL: R$ {pedido['kit']['price']:.2f}*\\n"

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

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------
# FORMAS DE PAGAMENTO
# --------------------------------------------
st.markdown("""
<div class="section" style="text-align:center;">
    <h4 style="color:#5A2E1B;">💳 Formas de Pagamento</h4>
    <p>✔️ Aceitamos cartões: Visa, MasterCard, Elo, Hipercard</p>
    <p>✔️ Pagamento via <b>PIX</b></p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------
# RODAPÉ PREMIUM
# --------------------------------------------
footer_html = """
<div style="
    background: linear-gradient(135deg, #5A2E1B, #3E1A10);
    color:white;
    text-align:center;
    padding:1.5rem;
    border-radius:12px;
    margin-top:3rem;
    font-size:0.9rem;
">
    <b>Flor de Cacau Confeitaria</b><br>
    Produção artesanal • Chocolate nobre • Ingredientes frescos<br><br>
    📍 Avenida Antonio de Carvalho, 2600 - Porto Alegre, RS<br>
    <a href="https://www.instagram.com/confeitariaflordecacau/"
       target="_blank"
       style="color:#F2C98A; text-decoration:none;">
        Instagram @flordecacau
    </a>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
