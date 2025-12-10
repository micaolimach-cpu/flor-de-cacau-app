import streamlit as st
from datetime import date, time
from urllib.parse import quote

st.set_page_config(page_title="Flor de Cacau", page_icon="🍫", layout="centered")

# --- Estilo personalizado ---
st.markdown("""
<style>
body {
    background-color: #FDECEF;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #4A3B32;
}
button, .stButton>button {
    background-color: #A0522D;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
}
.stTextInput>div>input {
    background-color: #FFF8F0;
    border: 1px solid #D2B48C;
}
</style>
""", unsafe_allow_html=True)

# --- Cabeçalho ---
st.image("logo.png", width=160)
st.title("Flor de Cacau")
st.markdown("Monte seu kit de brigadeiros personalizados 🍬")

# --- Sabores disponíveis ---
flavors = [
    {"id": 1, "name": "Tradicional", "icon": "🍫", "price": 3.00},
    {"id": 2, "name": "Beijinho", "icon": "🥥", "price": 3.00},
    {"id": 3, "name": "Morango", "icon": "🍓", "price": 3.50},
    {"id": 4, "name": "Maracujá", "icon": "🥭", "price": 3.50},
    {"id": 5, "name": "Oreo", "icon": "🍪", "price": 3.50},
    {"id": 6, "name": "Ninho", "icon": "🥛", "price": 3.50},
    {"id": 7, "name": "Café", "icon": "☕", "price": 3.50},
    {"id": 8, "name": "Paçoca", "icon": "🥜", "price": 3.50},
    {"id": 9, "name": "Churros", "icon": "🍩", "price": 3.50},
]

st.subheader("Escolha os Sabores")
selected_flavors = {}
total_price = 0.0

for flavor in flavors:
    with st.expander(f"{flavor['icon']} {flavor['name']} — R$ {flavor['price']:.2f}/un"):
        qty = st.number_input(
            f"Quantidade de {flavor['name']}",
            min_value=0,
            max_value=100,
            step=1,
            key=f"qty_{flavor['id']}"
        )
        if qty > 0:
            selected_flavors[flavor["name"]] = qty
            total_price += qty * flavor["price"]# --- Carrinho ---
st.subheader("🛒 Seu Pedido")

if not selected_flavors:
    st.info("Nenhum sabor selecionado ainda.")
else:
    st.markdown("### Resumo do Pedido")
    for sabor, qtd in selected_flavors.items():
        preco_unit = next(f["price"] for f in flavors if f["name"] == sabor)
        st.write(f"- {qtd}x {sabor} (R$ {preco_unit:.2f}/un)")

    st.markdown(f"**Total: R$ {total_price:.2f}**")

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
        for sabor, qtd in selected_flavors.items():
            preco_unit = next(f["price"] for f in flavors if f["name"] == sabor)
            message += f"{qtd}x {sabor} (R$ {preco_unit:.2f}/un)\\n"
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
        st.markdown(f"[👉 Abrir WhatsApp]({url})", unsafe_allow_html=True)# --- Rodapé ---
st.markdown("""
<hr style="margin-top: 2rem; margin-bottom: 1rem;">

<div style="text-align: center; font-size: 0.9rem; color: #4A3B32;">
    &copy; 2025 Flor de Cacau Confeitaria - Ingredientes frescos, produtores locais e chocolate nobre.<br>
    Feito com ❤️ em Porto Alegre - RS<br>
    <a href="https://www.instagram.com/confeitariaflordcacau/" target="_blank" style="color: #E91E63; text-decoration: none;">
        📸 Siga-nos no Instagram: @confeitariaflordcacau
    </a>
</div>
""", unsafe_allow_html=True)




