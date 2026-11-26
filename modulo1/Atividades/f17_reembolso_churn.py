# Função 17 - Solicitar reembolso

def solicitar_reembolso(banco_dados, id_pedido):
    try:
        pedido = banco_dados["assinaturas_transacoes"][id_pedido]
    except KeyError:
        return False
    
    if pedido["status"] == "REEMBOLSADO":
        return False
    
    if pedido["status"] == "PAGO":
        banco_dados["faturamento_total"] -= pedido["valor_liquido"]
        pedido["carrinho"].clear()
        pedido["status"] = "REEMBOLSADO"
        return True