st.markdown("---")

# --- Dados do cliente ---
if "pedido" in st.session_state:
    st.subheader("📄 Dados do Cliente")

    # Layout em duas colunas para Data e Horário
    col1, col2 = st.columns(2)
    
    with col1:
        [span_2](start_span)nome_cliente = st.text_input("👤 Nome do cliente")[span_2](end_span)
        [span_3](start_span)data_entrega = st.date_input("📅 Data de entrega", min_value=date.today())[span_3](end_span)
    
    with col2:
        # Coluna 2 é usada apenas para o Horário de entrega
        st.markdown("<p style='visibility: hidden;'>Nome placeholder</p>", unsafe_allow_html=True) # Espaço
        [span_4](start_span)horario_entrega = st.time_input("⏰ Horário de entrega", value=time(14, 0))[span_4](end_span)
        
    st.markdown("---")
    
    st.markdown("#### 🚚 Opções de Entrega")
    entrega_opcao = st.radio(
        "Forma de entrega", 
        ["Entrega no endereço", "Retirada no local"], 
        key="entrega_radio",
        horizontal=True, # Deixa as opções lado a lado
        label_visibility="collapsed" # Esconde o label para visual mais limpo
    [span_5](start_span))

    st.markdown("---")
    
    obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: sem coco, embalar separadamente...")[span_5](end_span)

    # Recriando o botão de WhatsApp com a cor e estilo originais
    # O botão já tem um estilo definido no CSS inicial (cor marrom/vermelha)
    [span_6](start_span)if st.button("📲 Finalizar pedido no WhatsApp"):[span_6](end_span)
        [span_7](start_span)phone = "5551992860852"[span_7](end_span)
        [span_8](start_span)pedido = st.session_state["pedido"][span_8](end_span)
        [span_9](start_span)message = "*🍫 NOVO PEDIDO - FLOR DE CACAU*\\n\\n"[span_9](end_span)
        [span_10](start_span)message += f"Kit escolhido: {pedido['kit']['name']} ({pedido['kit']['qty']} unidades)\\n\\n"[span_10](end_span)
        [span_11](start_span)for sabor, qtd in pedido["sabores"].items():[span_11](end_span)
            [span_12](start_span)message += f"{qtd}x {sabor}\\n"[span_12](end_span)
        [span_13](start_span)message += f"\\n*TOTAL: R$ {pedido['kit']['price']:.2f}*\\n"[span_13](end_span)

        [span_14](start_span)if nome_cliente:[span_14](end_span)
            [span_15](start_span)message += f"\\n👤 Cliente: {nome_cliente}"[span_15](end_span)
        [span_16](start_span)if data_entrega:[span_16](end_span)
            [span_17](start_span)message += f"\\n📅 Entrega: {data_entrega.strftime('%d/%m/%Y')}"[span_17](end_span)
        [span_18](start_span)if horario_entrega:[span_18](end_span)
            [span_19](start_span)message += f"\\n⏰ Horário: {horario_entrega.strftime('%H:%M')}"[span_19](end_span)
        [span_20](start_span)if entrega_opcao:[span_20](end_span)
            [span_21](start_span)message += f"\\n🚚 Forma de entrega: {entrega_opcao}"[span_21](end_span)
        [span_22](start_span)if obs:[span_22](end_span)
            [span_23](start_span)message += f"\\n📝 Observações: {obs}"[span_23](end_span)

        [span_24](start_span)url = f"https://wa.me/{phone}?text={quote(message)}"[span_24](end_span)
        [span_25](start_span)st.markdown(f"[👉 Abrir WhatsApp]({url})", unsafe_allow_html=True)[span_25](end_span)
