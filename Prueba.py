from GestionPedidos import Pedido, SistemaPedidos

def ok(msg): print(f"✅ {msg}")
def fail(msg): print(f"❌ {msg}")

# Prueba 1: crear pedido y estado inicial
p = Pedido("Pizza", 2)
if p.estado == "Pendiente": ok("Estado inicial correcto")
else: fail("Estado inicial incorrecto")

# Prueba 2: cambiar a estado válido
try:
    p.cambiar_estado("Entregado")
    if p.estado == "Entregado": ok("Cambio de estado válido")
    else: fail("El estado no cambió correctamente")
except:
    fail("Excepción inesperada al cambiar estado válido")

# Prueba 3: cambiar a estado inválido
try:
    p.cambiar_estado("Inexistente")
    fail("No lanzó error al estado inválido")
except ValueError:
    ok("Capturó error en estado inválido")

# Prueba 4: agregar pedidos al sistema
s = SistemaPedidos()
s.agregar_pedido("Hamburguesa", 1)
s.agregar_pedido("Jugo", 1)
if len(s.pedidos) == 2: ok("Agregó pedidos correctamente")
else: fail("No agregó la cantidad correcta de pedidos")

# Prueba 5: resumen por estado
s.pedidos[1].cambiar_estado("En preparación")
r = s.resumen_por_estado()
if r.get("Pendiente",0)==1 and r.get("En preparación",0)==1:
    ok("Resumen por estado correcto")
else:
    fail(f"Resumen incorrecto: {r}")