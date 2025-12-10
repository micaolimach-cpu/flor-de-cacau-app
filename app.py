import streamlit as st
from datetime import date, time
from urllib.parse import quote

# --- Configuração da página ---
st.set_page_config(page_title="Flor de Cacau", page_icon="🍫", layout="wide")

# --- Logo ---
st.image("logo.png", width=200)
st.title("🍫 Flor de Cacau")
st.subheader("Kits de Brigadeiro para Eventos, Festas & Confraternizações")

# --- Dados dos Kits ---
kits = [
    {"id": 1, "name": "Kit Pequeno", "units": 6, "price": 18.00, "description": "Perfeito para degustação"},
    {"id": 2, "name": "Kit Médio", "units": 12, "price": 33.00, "description": "Ideal para presentear"},
    {"id": 3, "name": "Kit Grande", "units": 24, "price": 60.00, "description": "Ótimo para os amantes de brigadeiro"},
    {"id": 4, "name": "Kit Premium", "units": 50, "price": 120.00, "description": "Para aquele evento de última hora"},
    {"id": 6, "name": "Kit Mega", "units": 100, "price": 210.00, "description": "Para festas e eventos maiores (100–1000 unidades)"},
]

# --- Dados dos Sabores ---
flavors = [
    {"id": 1, "name": "Tradicional", "icon": "🍫"},
    {"id": 2, "name": "Beijinho", "icon": "🥥"},
    {"id": 3, "name": "Morango", "icon": "🍓"},
    {"id": 7, "name": "Maracujá", "icon": "🥭"},
    {"id": 8, "name": "Oreo", "icon": "🍪"},
    {"id": 9, "name": "Ninho", "icon": "🥛"},
    {"id": 10, "name": "Café", "icon": "☕"},
    {"id": 11, "name": "Paçoca", "icon": "🥜"},
    {"id": 12, "name": "Churros", "icon": "🍩"},


# --- Estado ---
if "cart" not in st.session_state:
    st.session_state["cart"] = []
if "selected_kit" not in st.session_state:
    st.session_state["selected_kit"] = None

# --- Mostrar Kits ---
st.header("📦 Nossos Kits Especiais")
cols = st.columns(3)
for i, kit in enumerate(kits):
    with cols[i % 3]:
        st.markdown(f"### {kit['name']}")
        st.write(kit["description"])
        st.write(f"**{kit['units']} unidades**")
        st.write(f"💰 R$ {kit['price']:.2f} (R$ {kit['price']/kit['units']:.2f}/un)")
        if st.button(f"Montar {kit['name']}", key=f"btn_{kit['id']}"):
            st.session_state["selected_kit"] = kit

# --- Configuração do Kit ---
if st.session_state["selected_kit"]:
    kit = st.session_state["selected_kit"]
    st.subheader(f"🎨 Configurar {kit['name']}")
    selected_flavors = {}
    total_units = 0

    cols = st.columns(3)
    for i, flavor in enumerate(flavors):
        with cols[i % 3]:
            max_units = 1000 if kit["id"] == 6 else kit["units"]
            qty = st.number_input(
                f"{flavor['icon']} {flavor['name']}",
                min_value=0,
                max_value=max_units,
                step=1,
                key=f"flavor_{kit['id']}_{flavor['id']}"
            )
            if qty > 0:
                selected_flavors[flavor["name"]] = qty
                total_units += qty

    if kit["id"] == 6:
        st.write(f"Selecionado: {total_units} unidades (mínimo 100, máximo 1000)")
        st.progress(min(total_units / 1000, 1.0))
        can_add = 100 <= total_units <= 1000
    else:
        st.write(f"Selecionado: {total_units}/{kit['units']} unidades")
        st.progress(min(total_units / kit["units"], 1.0))
        can_add = (total_units == kit["units"])

    if can_add and st.button("✅ Adicionar ao carrinho"):
        st.session_state["cart"].append({
            "kit": kit,
            "flavors": selected_flavors,
            "total": kit["price"]
        })
        st.session_state["selected_kit"] = None
        st.success("Kit adicionado ao carrinho!")

# --- Carrinho ---
st.header("🛒 Seu carrinho")
if not st.session_state["cart"]:
    st.info("Carrinho vazio.")
else:
    total = 0.0
    for i, item in enumerate(st.session_state["cart"]):
        st.markdown(f"**{item['kit']['name']}** — {item['kit']['units']} unidades")
        st.write("Sabores:")
        for sabor, qtd in item["flavors"].items():
            st.write(f"- {qtd}x {sabor}")
        st.write(f"💰 **R$ {item['total']:.2f}**")
        total += item["total"]

        if st.button("🗑️ Remover este kit", key=f"remove_{i}"):
            st.session_state["cart"].pop(i)
            st.experimental_rerun()

    st.markdown(f"## Total: R$ {total:.2f}")

    # --- Dados do cliente ---
    st.subheader("📄 Dados para entrega")
    nome_cliente = st.text_input("👤 Nome do cliente")
    data_entrega = st.date_input("📅 Data de entrega", min_value=date.today())
    horario_entrega = st.time_input("⏰ Horário de entrega", value=time(14, 0))
    obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: Embalar separadamente, sem coco...")

    # --- Opções de pagamento ---
    st.subheader("💳 Forma de pagamento")
    pagamento = st.radio(
        "Selecione:",
        ["PIX", "Cartão de Crédito", "Cartão de Débito", "Pagamento na Entrega"]
    )

    if pagamento == "PIX":
        st.info("Chave PIX (CPF): 01738014045")
    elif pagamento in ["Cartão de Crédito", "Cartão de Débito"]:
        st.write("Aceitamos as principais bandeiras:")
        st.markdown("Visa | MasterCard | Elo | Hipercard | American Express")
    else:
        st.success("Pagamento será realizado no ato da entrega.")

    # --- Finalizar no WhatsApp ---
    if st.button("📲 Finalizar no WhatsApp"):
        phone = "5551992860852"
        message = "*🍫 NOVO PEDIDO - FLOR DE CACAU*\\n\\n"
        for idx, item in enumerate(st.session_state["cart"], 1):
            units_display = sum(item["flavors"].values()) if item["kit"]["id"] == 6 else item["kit"]["units"]
            message += f"*{idx}. {item['kit']['name']}* ({units_display} unidades)\\n"
            message += f"Valor: R$ {item['total']:.2f}\\nSabores:\\n"
            for sabor, qtd in item["flavors"].items():
                message += f"  • {qtd}x {sabor}\\n"
            message += "\\n"

        message += f"*TOTAL: R$ {total:.2f}*\\n"

        if nome_cliente:
            message += f"\\n👤 Cliente: {nome_cliente}"
        if data_entrega:
            message += f"\\n📅 Entrega: {data_entrega.strftime('%d/%m/%Y')}"
        if horario_entrega:
            message += f"\\n⏰ Horário: {horario_entrega.strftime('%H:%M')}"
        if obs:
            message += f"\\n📝 Observações: {obs}"
        message += f"\\n💳 Pagamento: {pagamento}"

        url = f"https://wa.me/{phone}?text={quote(message)}"
        st.markdown(f"[👉 Abrir WhatsApp]({url})", unsafe_allow_html=True)

# --- Rodapé ---
st.markdown(""
<hr style="margin-top: 2rem; margin-bottom: 1rem;">

<div style="text-align: center; font-size: 0.9rem; color: #4A3B32;">
    © 2025 Flor de Cacau Confeitaria — Ingredientes frescos, produtores locais e chocolate nobre.<br>
    Feito com ❤️ em Porto Alegre - RS<br>
    <a href="https://www.instagram.com/confeitariaflordcacau/" target="_blank" style="color: #E91E63; text-decoration: none;">
        📸 Siga-nos no Instagram: @confeitariaflordcacau
    </a>
</div>
"", unsafe_allow_html=True)

