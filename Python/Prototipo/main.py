from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Ruta del archivo PDF
import os
pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Documento_Diseño_YuliPanPedidos.pdf")

# Crear documento
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()

# Estilos personalizados
style_title = ParagraphStyle(
    name="Title",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    fontSize=24,
    textColor=colors.HexColor("#D4AF37")
)
style_heading = ParagraphStyle(
    name="Heading",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=18,
    textColor=colors.HexColor("#8B5E3C")
)
style_subtitle = ParagraphStyle(
    name="Subtitle",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontName="Helvetica",
    fontSize=14,
    textColor=colors.HexColor("#8B5E3C")
)
style_body = ParagraphStyle(
    name="Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=12,
    leading=18,
    textColor=colors.HexColor("#000000")
)

elements = []

# Portada
elements.append(Spacer(1, 100))
elements.append(Paragraph("🏪 YuliPanPedidos", style_title))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Documento de Diseño del Proyecto", style_subtitle))
elements.append(Spacer(1, 40))
elements.append(Paragraph("Desarrollado por: Alberto Schmalbach López", style_body))
elements.append(Paragraph("Fecha: Octubre 2025", style_body))
elements.append(PageBreak())

# Introducción
elements.append(Paragraph("1. Introducción", style_heading))
elements.append(Spacer(1, 20))
elements.append(Paragraph("""El presente documento describe los aspectos visuales, estructurales y de navegación del proyecto YuliPanPedidos, 
una plataforma web para la gestión de pedidos de panadería artesanal. El diseño busca reflejar una identidad cálida y moderna, 
que evoque la frescura del pan recién hecho y facilite la experiencia de compra de los usuarios.""", style_body))
elements.append(PageBreak())

# Diseño Visual
elements.append(Paragraph("2. Diseño Visual", style_heading))
elements.append(Spacer(1, 20))
elements.append(Paragraph("2.1 Identidad de la marca", style_subtitle))
elements.append(Spacer(1, 10))
elements.append(Paragraph("""La identidad visual de YuliPanPedidos se fundamenta en tres conceptos clave: artesanal, acogedor y moderno.
El diseño emplea tonos beige con textura de panadería y un dorado suave para transmitir elegancia y cercanía.
El ícono principal es una ilustración vectorial plana de una tienda, representando el espacio físico y virtual donde los clientes realizan sus compras.""", style_body))
elements.append(Spacer(1, 20))

elements.append(Paragraph("2.2 Tipografía y color", style_subtitle))
elements.append(Spacer(1, 10))
elements.append(Paragraph("""• Tipografía principal: Poppins (para títulos y botones)
• Tipografía secundaria: Open Sans (para textos descriptivos)

Paleta de colores:
• Dorado suave (#D4AF37)
• Blanco cálido (#FAF7F2)
• Beige claro (#F5EBD0)
• Marrón tostado (#8B5E3C)""", style_body))
elements.append(PageBreak())

# Pantallas del Proyecto
elements.append(Paragraph("3. Pantallas del Proyecto", style_heading))
elements.append(Spacer(1, 20))

elements.append(Paragraph("3.1 Pantalla de Inicio", style_subtitle))
elements.append(Spacer(1, 10))
elements.append(Paragraph("""Contiene el logotipo principal, un mensaje de bienvenida y botones de acceso rápido a las secciones 
del catálogo y contacto. Se destaca una imagen ilustrada representando la panadería.""", style_body))
elements.append(Spacer(1, 20))

elements.append(Paragraph("3.2 Pantalla de Catálogo", style_subtitle))
elements.append(Spacer(1, 10))
elements.append(Paragraph("""Muestra los productos en tarjetas verticales con nombre, descripción breve, precio e imagen.
Ejemplos:
• Pan aliñado
• Postre de fresa
• Café con leche
Cada tarjeta incluye el botón "Agregar al carrito".""", style_body))
elements.append(Spacer(1, 20))

elements.append(Paragraph("3.3 Pantalla de Carrito", style_subtitle))
elements.append(Spacer(1, 10))
elements.append(Paragraph("""Presenta los productos seleccionados, con opciones para cambiar la cantidad o eliminarlos.
Incluye un resumen del pedido y el total a pagar, además del botón "Proceder al pago".""", style_body))
elements.append(PageBreak())

# Mapa de Navegación
elements.append(Paragraph("4. Mapa de Navegación", style_heading))
elements.append(Spacer(1, 20))
elements.append(Paragraph("""La estructura de navegación es jerárquica y clara:""", style_body))
elements.append(Spacer(1, 10))
nav_structure = ListFlowable(
    [
        ListItem(Paragraph("Inicio", style_body), leftIndent=0),
        ListItem(Paragraph("Catálogo", style_body), leftIndent=20),
        ListItem(Paragraph("Pan aliñado", style_body), leftIndent=40),
        ListItem(Paragraph("Postre de fresa", style_body), leftIndent=40),
        ListItem(Paragraph("Café con leche", style_body), leftIndent=40),
        ListItem(Paragraph("Carrito", style_body), leftIndent=20),
        ListItem(Paragraph("Confirmar pedido", style_body), leftIndent=40),
        ListItem(Paragraph("Contacto", style_body), leftIndent=20),
        ListItem(Paragraph("Enviar mensaje", style_body), leftIndent=40),
    ]
)
elements.append(nav_structure)
elements.append(Spacer(1, 20))
elements.append(Paragraph("""El usuario inicia en la pantalla principal, desde donde puede acceder al catálogo, 
agregar productos al carrito o contactar la panadería. La navegación es vertical y jerárquica, 
con accesos claros en la parte superior (barra de navegación fija).""", style_body))
elements.append(PageBreak())

# Conclusión
elements.append(Paragraph("5. Conclusión", style_heading))
elements.append(Spacer(1, 20))
elements.append(Paragraph("""El diseño de YuliPanPedidos integra simplicidad, estética y funcionalidad.
El uso de Material Design 3, ilustraciones vectoriales planas y una paleta cálida permite transmitir confianza y comodidad.
La estructura y el mapa de navegación garantizan una experiencia accesible, fluida y coherente con la identidad de la marca.""", style_body))
elements.append(Spacer(1, 40))

# Pie de documento
elements.append(Paragraph("Documento preparado por:", style_subtitle))
elements.append(Spacer(1, 10))
elements.append(Paragraph("Alberto Schmalbach López", style_body))
elements.append(Paragraph("Octubre 2025", style_body))

# Generar PDF
doc.build(elements)

pdf_path
