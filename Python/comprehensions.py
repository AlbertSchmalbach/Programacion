productos = [
    {
        "nombre": "Pan integral",
        "precio": 3500,
        "descripcion": "Pan elaborado con harina integral, ideal para una alimentación saludable.",
    },
    {
        "nombre": "Galletas de avena",
        "precio": 2500,
        "descripcion": "Crujientes galletas hechas con avena y miel natural.",
    },
    {
        "nombre": "Torta de chocolate",
        "precio": 12000,
        "descripcion": "Deliciosa torta húmeda con cobertura de chocolate artesanal.",
    },
    {
        "nombre": "Pan aliñado",
        "precio": 2000,
        "descripcion": "Pan suave y aromático, preparado con mantequilla y queso rallado.",
    },
    {
        "nombre": "Rosquitas dulces",
        "precio": 1800,
        "descripcion": "Rosquitas azucaradas perfectas para acompañar con café o té.",
    },
]


def return_title_product():
    return [product["nombre"] for product in productos]


def return_price_product():
    return [product["precio"] for product in productos if product["precio"] > 2000]


print(return_title_product())
print(return_price_product())
