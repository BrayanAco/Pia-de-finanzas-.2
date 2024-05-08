# Definir las funciones para cada razón financiera
def liquidez_corriente(activo_corriente, pasivo_corriente):
    return activo_corriente / pasivo_corriente

def razon_rapida(activo_corriente, inventario, pasivo_corriente):
    return (activo_corriente - inventario) / pasivo_corriente

def rotacion_inventario(costo_venta, inventario_promedio):
    return costo_venta / inventario_promedio

def periodo_promedio_cobro(cuentas_por_cobrar, ventas_netas):
    return cuentas_por_cobrar / (ventas_netas / 365)

def periodo_promedio_pago(cuentas_por_pagar, costo_venta):
    return cuentas_por_pagar / (costo_venta / 365)

def rotacion_activos_totales(ventas_netas, activos_totales):
    return ventas_netas / activos_totales

def razon_endeudamiento(total_pasivos, activos_totales):
    return total_pasivos / activos_totales

def razon_cargos_interes_fijos(EBIT, gastos_interes):
    return EBIT / gastos_interes

def razon_cobertura_pagos_fijos(EBIT, pagos_fijos):
    return EBIT / pagos_fijos

def margen_utilidad_bruta(ventas_netas, costo_venta):
    return (ventas_netas - costo_venta) / ventas_netas

def margen_utilidad_operativa(EBIT, ventas_netas):
    return EBIT / ventas_netas

def margen_utilidad_neta(utilidad_neta, ventas_netas):
    return utilidad_neta / ventas_netas

def ganancias_por_accion(utilidad_neta, acciones_emitidas):
    return utilidad_neta / acciones_emitidas

def rendimiento_sobre_activos_totales(utilidad_neta, activos_totales):
    return utilidad_neta / activos_totales

def rendimiento_sobre_patrimonio(utilidad_neta, patrimonio):
    return utilidad_neta / patrimonio

def razon_precio_ganancias(precio_accion, ganancias_por_accion):
    return precio_accion / ganancias_por_accion

def razon_mercado_libro(precio_accion, valor_libro_accion):
    return precio_accion / valor_libro_accion

# Solicitar la entrada del usuario
SEPARADOR = "--" * 22

razon_financiera = print("Introduzca el nombre de una razón financiera: ")
print("---------------Opciones--------------------")
print("1). Liquidez corriente")
print("2). Razón rápida")
print("3). Rotación de inventario")
print("4). Período promedio de cobro")
print("5). Período promedio de pago")
print("6). Rotación de activos totales")
print("7). Razón de endeudamiento")
print("8). Razón de cargos de interés fijos")
print("9). Razón de cobertura de pagos fijos")
print("10). Margen de utilidad bruta")
print("11). Margen de utilidad operativa")
print("12). Margen de utilidad neta")
print("13). Ganancias por acción")
print("14). Rendimiento sobre los activos totales")
print("15). Rendimiento sobre el patrimonio")
print("16). Razón precio/ganancias")
print("17). Razón mercado/libro")
print(SEPARADOR)

razon = int(input("¿Qué razón financiera necesitas? "))
print(SEPARADOR)

# Ejecutar la función correspondiente y mostrar el resultado
if razon == 1:
    razon_financiera = "Liquidez corriente"
    activo_corriente = float(input("Introduzca el valor del activo corriente: "))
    pasivo_corriente = float(input("Introduzca el valor del pasivo corriente: "))
    resultado = liquidez_corriente(activo_corriente, pasivo_corriente)
    print("El resultado de la razón financiera de liquidez corriente es:", resultado)
    print(SEPARADOR)
    
elif razon == 2:
    razon_financiera = "Razón rápida"
    activo_corriente = float(input("Introduzca el valor del activo corriente: "))
    inventario = float(input("Introduzca el valor del inventario: "))
    pasivo_corriente = float(input("Introduzca el valor del pasivo corriente: "))
    resultado = razon_rapida(activo_corriente, inventario, pasivo_corriente)
    print("El resultado de la razón financiera de razón rápida es:", resultado)
    print(SEPARADOR)
    
elif razon == 3:
    razon_financiera = "Rotación de inventario"
    costo_venta = float(input("Introduzca el costo de venta: "))
    inventario_promedio = float(input("Introduzca el valor del inventario promedio: "))
    resultado = rotacion_inventario(costo_venta, inventario_promedio)
    print("El resultado de la razón financiera de rotación de inventario es:", resultado)
    print(SEPARADOR)
    
elif razon == 4:
    razon_financiera = "Período promedio de cobro"
    cuentas_por_cobrar = float(input("Introduzca el valor de las cuentas por cobrar: "))
    ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
    resultado = periodo_promedio_cobro(cuentas_por_cobrar, ventas_netas)
    print("El resultado del período promedio de cobro es:", resultado)
    print(SEPARADOR)
    
elif razon == 5:
    razon_financiera = "Período promedio de pago"
    cuentas_por_pagar = float(input("Introduzca el valor de las cuentas por pagar: "))
    costo_venta = float(input("Introduzca el costo de venta: "))
    resultado = periodo_promedio_pago(cuentas_por_pagar, costo_venta)
    print("El resultado del período promedio de pago es:", resultado)
    print(SEPARADOR)
    
elif razon == 6:
    razon_financiera = "Rotación de activos totales"
    ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
    activos_totales = float(input("Introduzca el valor de los activos totales: "))
    resultado = rotacion_activos_totales(ventas_netas, activos_totales)
    print("El resultado de la razón financiera de rotación de activos totales es:", resultado)
    print(SEPARADOR)
    
elif razon == 7:
    razon_financiera = "Razón de endeudamiento"
    pasivo_total = float(input("Introduzca el valor del pasivo total: "))
    activos_totales = float(input("Introduzca el valor de los activos totales: "))
    resultado = razon_endeudamiento(pasivo_total, activos_totales)
    print("El resultado de la razón financiera de razón de endeudamiento es:", resultado)
    print(SEPARADOR)
    
elif razon == 8:
    razon_financiera = "Razón de cargos de interés fijos"
    gastos_interes = float(input("Introduzca el valor de los gastos por intereses: "))
    utilidad_antes_impuestos = float(input("Introduzca el valor de la utilidad antes de impuestos: "))
    resultado = razon_cargos_interes_fijos(gastos_interes, utilidad_antes_impuestos)
    print("El resultado de la razón financiera de razón de cargos de interés fijos es:", resultado)
    print(SEPARADOR)
    
elif razon == 9:
    razon_financiera = "Razón de cobertura de pagos fijos"
    utilidad_antes_impuestos = float(input("Introduzca el valor de la utilidad antes de impuestos: "))
    gastos_interes = float(input("Introduzca el valor de los gastos por intereses: "))
    pagos_fijos = float(input("Introduzca el valor de los pagos fijos: "))
    resultado = razon_cobertura_pagos_fijos(utilidad_antes_impuestos, gastos_interes, pagos_fijos)
    print("El resultado de la razón financiera de razón de cobertura de pagos fijos es:", resultado)
    print(SEPARADOR)
    
elif razon == 10:
    razon_financiera = "Margen de utilidad bruta"
    utilidad_bruta = float(input("Introduzca el valor de la utilidad bruta: "))
    ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
    resultado = margen_utilidad_bruta(utilidad_bruta, ventas_netas)
    print("El resultado de la razón financiera de margen de utilidad bruta es:", resultado)
    print(SEPARADOR)
    
elif razon == 11:
    razon_financiera = "Margen de utilidad operativa"
    utilidad_operativa = float(input("Introduzca el valor de la utilidad operativa: "))
    ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
    resultado = margen_utilidad_operativa(utilidad_operativa, ventas_netas)
    print("El resultado de la razón financiera de margen de utilidad operativa es:", resultado)
    print(SEPARADOR)
    
elif razon == 12:
    razon_financiera = "Margen de utilidad neta"
    utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
    ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
    resultado = margen_utilidad_neta(utilidad_neta, ventas_netas)
    print("El resultado de la razón financiera de margen de utilidad neta es:", resultado)
    print(SEPARADOR)
    
elif razon == 13:
    razon_financiera = "Ganancias por acción"
    utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
    acciones_emitidas = float(input("Introduzca el valor de las acciones emitidas: "))
    resultado = ganancias_por_accion(utilidad_neta, acciones_emitidas)
    print("El resultado de la razón financiera de ganancias por acción es:", resultado)
    print(SEPARADOR)
    
elif razon == 14:
    razon_financiera = "Rendimiento sobre los activos totales"
    utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
    activos_totales = float(input("Introduzca el valor de los activos totales: "))
    resultado = rendimiento_sobre_activos_totales(utilidad_neta, activos_totales)
    print("El resultado de la razón financiera de rendimiento sobre los activos totales es:", resultado)
    print(SEPARADOR)
    
elif razon == 15:
    razon_financiera = "Rendimiento sobre el patrimonio"
    utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
    patrimonio = float(input("Introduzca el valor del patrimonio: "))
    resultado = rendimiento_sobre_patrimonio(utilidad_neta, patrimonio)
    print("El resultado de la razón financiera de rendimiento sobre el patrimonio es:", resultado)
    print(SEPARADOR)
    
elif razon == 16:
    razon_financiera = "Razón precio/ganancias"
    precio_accion = float(input("Introduzca el valor del precio por acción: "))
    ganancias_por_accion = float(input("Introduzca el valor de las ganancias por acción: "))
    resultado = razon_precio_ganancias(precio_accion, ganancias_por_accion)
    print("El resultado de la razón financiera de razón precio/ganancias es:", resultado)
    print(SEPARADOR)
    
elif razon == 17:
    razon_financiera = "Razón mercado/libro"
    precio_accion = float(input("Introduzca el valor del precio por acción: "))
    valor_libro_accion = float(input("Introduzca el valor del valor en libros por acción: "))
    resultado = razon_mercado_libro(precio_accion, valor_libro_accion)
    print("El resultado de la razón financiera de razón mercado/libro es:", resultado)
    print(SEPARADOR)
    
else:
    print("¡Opción no válida!")


