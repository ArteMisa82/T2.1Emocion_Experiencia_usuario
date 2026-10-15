from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether

ROOT=Path(r"C:\Users\Sebas2hVR\Desktop\T2.1 Emoción y experiencia de usuario")
BASE=ROOT/"Tarea_Experiencia_Emocional_UX"
OUT=BASE/"informe"/"informe_final.pdf"
pdfmetrics.registerFont(TTFont("Arial",r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold",r"C:\Windows\Fonts\arialbd.ttf"))

GREEN=colors.HexColor("#075C4A"); DARK=colors.HexColor("#111E1B"); MUTED=colors.HexColor("#52605C")
PALE=colors.HexColor("#E9F4F0"); GOLD=colors.HexColor("#F59E0B"); RED=colors.HexColor("#B42318")
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="T",fontName="Arial-Bold",fontSize=26,leading=31,textColor=DARK,spaceAfter=14))
styles.add(ParagraphStyle(name="Sub",fontName="Arial",fontSize=12,leading=18,textColor=MUTED,spaceAfter=10))
styles.add(ParagraphStyle(name="H1x",fontName="Arial-Bold",fontSize=18,leading=22,textColor=DARK,spaceBefore=4,spaceAfter=10))
styles.add(ParagraphStyle(name="H2x",fontName="Arial-Bold",fontSize=12,leading=15,textColor=GREEN,spaceBefore=8,spaceAfter=5))
styles.add(ParagraphStyle(name="Bodyx",fontName="Arial",fontSize=9.5,leading=14,textColor=DARK,spaceAfter=7))
styles.add(ParagraphStyle(name="Smallx",fontName="Arial",fontSize=8,leading=11,textColor=MUTED,spaceAfter=4))
styles.add(ParagraphStyle(name="Centerx",fontName="Arial",fontSize=9,leading=13,textColor=MUTED,alignment=TA_CENTER))
styles.add(ParagraphStyle(name="Warn",fontName="Arial-Bold",fontSize=9.5,leading=14,textColor=RED,spaceAfter=8))

def p(s,style="Bodyx"): return Paragraph(s,styles[style])
def scaled(path,maxw,maxh):
    im=Image(str(path)); ratio=min(maxw/im.imageWidth,maxh/im.imageHeight); im.drawWidth=im.imageWidth*ratio; im.drawHeight=im.imageHeight*ratio; return im
def header_footer(canv,doc):
    canv.saveState(); canv.setStrokeColor(colors.HexColor("#D5DFDB")); canv.line(2*cm,1.35*cm,A4[0]-2*cm,1.35*cm)
    canv.setFont("Arial",8); canv.setFillColor(MUTED); canv.drawString(2*cm,.85*cm,"Emoción y experiencia de usuario · SuperOfertas Ecuador")
    canv.drawRightString(A4[0]-2*cm,.85*cm,f"Página {doc.page}"); canv.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=1.7*cm,leftMargin=1.7*cm,topMargin=1.6*cm,bottomMargin=1.7*cm,title="Análisis y rediseño de la experiencia emocional")
story=[]
story += [Spacer(1,1.4*cm),p("ANÁLISIS UX", "H2x"),p("Análisis y rediseño de la experiencia emocional", "T"),p("Caso de estudio: confirmación de dirección en mapa de SuperOfertas Ecuador", "Sub")]
story += [Spacer(1,.4*cm),scaled(BASE/"rediseño"/"antes_despues.png",16.5*cm,8.2*cm),Spacer(1,.5*cm)]
story += [p("Objetivo", "H1x"),p("Analizar qué puede percibir, pensar y sentir una persona antes, durante y después de confirmar una dirección; identificar riesgos de confianza, claridad y control; y proponer un rediseño fundamentado en principios de IHC, usabilidad y accesibilidad.")]
story += [p("Estado de la evidencia", "H2x"),p("La inspección del prototipo, la matriz, el rediseño y los instrumentos de prueba están completos. La prueba emocional con tres participantes reales permanece pendiente. Este documento no atribuye emociones a personas no observadas.","Warn")]
story += [p("Enlace editable de Figma", "H2x"),p("https://www.figma.com/design/u7v5nFGtjdyHFBrtkbPgAU"),p("Integrantes: [completar]  ·  Repositorio GitHub: [completar por el equipo]","Smallx"),PageBreak()]

story += [p("1 Caso y tarea evaluada","H1x"),p("La interfaz corresponde al paso 4 de un flujo de compra. La tarea evaluada consiste en revisar la ubicación mostrada, confirmar que corresponde a Calle Inventada 123, Barrio Ejemplo, y avanzar al pago. La misma tarea debe emplearse en la versión original y en el rediseño para que la comparación sea válida.")]
story += [scaled(BASE/"evidencias"/"original"/"captura-01-momentos-anotados.png",16.5*cm,10.6*cm),p("Figura 1. Prototipo original con los cinco momentos de interacción señalados.","Centerx")]
story += [p("Lectura inicial","H2x"),p("La pantalla combina colores de alta saturación, mensajes de urgencia y varias acciones con pesos visuales contradictorios. El mapa, la dirección y el botón de guardado no forman una secuencia perceptiva clara. La acción 'OMITIR' domina, aunque no ayuda a completar la tarea principal."),PageBreak()]

story += [p("2 Cinco momentos de interacción","H1x")]
moments=[
 ("1 Antes e ingreso","La persona llega desde el paso “Quién recibe”. Debe reconocer que ahora revisará una dirección y comprender el progreso del flujo.","La oferta, el temporizador y el fondo saturado compiten con el encabezado de tarea."),
 ("2 Exploración","La persona recorre el mapa, la dirección textual y los controles disponibles.","No se indica cómo manipular el mapa ni cómo se relaciona el punto con la dirección."),
 ("3 Búsqueda o ajuste","La persona intenta comprobar o corregir la ubicación.","No existe búsqueda visible y el botón de guardado parece inactivo."),
 ("4 Selección","La persona interpreta cuál punto está seleccionado.","El pin rojo y el punto azul crean dos candidatos visuales sin confirmación."),
 ("5 Después y finalización","La persona guarda la dirección y espera avanzar.","La acción 'OMITIR' domina, mientras la finalización carece de una respuesta clara."),
]
for a,b,c in moments:
    story += [p(a,"H2x"),p(b),p("Evidencia observable: "+c,"Smallx")]
story += [Spacer(1,.25*cm),p("Criterio de interpretación","H2x"),p("Los hallazgos anteriores describen propiedades observables de la interfaz y riesgos plausibles. No constituyen emociones comprobadas. Para afirmar frustración, confianza o satisfacción se requiere la valoración de participantes y evidencia conductual o verbal."),PageBreak()]

story += [p("3 Curva emocional provisional","H1x"),scaled(BASE/"curva_emocional"/"curva_emocional.png",16.5*cm,8.4*cm),p("Figura 2. Estimación heurística usada para priorizar el rediseño; no reemplaza la medición con usuarios.","Centerx")]
story += [p("Momentos críticos previstos","H2x"),p("La selección se considera el riesgo principal porque existen dos señales espaciales incompatibles. La búsqueda o ajuste constituye el segundo riesgo, pues el sistema no ofrece una vía evidente para corregir la dirección. Estas prioridades deben confirmarse o refutarse con tres participantes.")]
story += [p("Escala de medición","H2x"),p("Cada participante calificará cada momento entre -3 (muy negativa) y +3 (muy positiva). La matriz Excel incluida calcula el promedio individual y el promedio por momento cuando se ingresan los quince valores de cada versión."),PageBreak()]

story += [p("4 Matriz UX","H1x")]
data=[[p(x,"Smallx") for x in ["Momento","Evidencia","Problema","Mejora","Principio IHC"]]]
rows=[
 ["Ingreso","Oferta y temporizador dominan","Jerarquía confusa","Título de tarea y progreso legible","Correspondencia y carga cognitiva"],
 ["Exploración","Sin instrucciones de uso","Affordances débiles","Instrucción y controles rotulados","Visibilidad del estado"],
 ["Búsqueda","Sin búsqueda o edición visible","Bajo control","Campos editables y ajuste explícito","Control y recuperación"],
 ["Selección","Pin rojo y punto azul compiten","Estado ambiguo","Un marcador y confirmación textual","Retroalimentación y consistencia"],
 ["Finalización","Guardar parece inactivo; Omitir domina","Acción riesgosa","CTA primario y edición secundaria","Jerarquía y prevención de errores"],
]
data += [[p(c,"Smallx") for c in row] for row in rows]
t=Table(data,colWidths=[2.4*cm,3.5*cm,3.0*cm,3.6*cm,3.4*cm],repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),GREEN),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.HexColor("#D5DFDB")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("BACKGROUND",(0,1),(-1,-1),colors.white),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#F4F8F6")]),("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
story += [t,Spacer(1,.35*cm),p("La versión editable completa se encuentra en matriz/matriz_ux.xlsx. Las columnas amarillas están reservadas para emociones y puntuaciones reales.","Smallx"),PageBreak()]

story += [p("5 Rediseño antes y después","H1x"),scaled(BASE/"rediseño"/"antes_despues.png",16.5*cm,8.4*cm),p("Figura 3. Comparación de la interfaz original y la pantalla editable desarrollada en Figma.","Centerx")]
story += [p("Cambios principales","H2x")]
for s in [
 "Jerarquía orientada a la tarea: el propósito y el progreso preceden al contenido del mapa.",
 "Estado único y visible: un marcador seleccionado se vincula con una dirección y el texto 'Punto confirmado'.",
 "Acción inequívoca: 'Guardar dirección y continuar' es el CTA primario; editar y volver son secundarios.",
 "Reducción de presión: el temporizador y el mensaje de urgencia dejan de competir con una decisión logística.",
 "Accesibilidad: contraste más estable, tipografía sans serif, controles rotulados, foco previsto y mensajes que no dependen solo del color."
]: story += [p("• "+s)]
story += [PageBreak()]

story += [p("6 Plan de validación con tres participantes","H1x"),p("La validación debe completarse antes de presentar el trabajo como evidencia de usuarios. El paquete incluye protocolo, consentimiento breve, plantilla visual y un registro Excel con fórmulas.")]
steps=[
 ["1","Preparación","Asignar códigos U1-U3, evitar datos personales y abrir ambas versiones."],
 ["2","Prueba original","Leer la tarea, observar sin ayudar y registrar cinco puntuaciones, tiempo, errores y citas."],
 ["3","Prueba del rediseño","Repetir la misma tarea; si es posible, equilibrar el orden entre participantes."],
 ["4","Comparación","Calcular promedios antes/después y contrastar conducta, verbalizaciones y puntuaciones."],
 ["5","Cierre","Sustituir la curva provisional, completar la matriz y actualizar conclusiones."],
]
tab=Table([[p("Paso","Smallx"),p("Actividad","Smallx"),p("Evidencia","Smallx")]]+[[p(x,"Smallx") for x in r] for r in steps],colWidths=[1.2*cm,3.7*cm,11.9*cm],repeatRows=1)
tab.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),GREEN),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.5,colors.HexColor("#D5DFDB")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#F4F8F6")]),("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
story += [tab,Spacer(1,.4*cm),p("Criterio de mejora","H2x"),p("Una mejora será más convincente si el promedio emocional aumenta en los momentos críticos y, al mismo tiempo, disminuyen dudas, errores o tiempo. Una puntuación aislada no basta: debe interpretarse junto con la evidencia observable."),PageBreak()]

story += [p("7 Conclusiones y reflexión","H1x"),p("El problema central del prototipo original no es únicamente estético. La interfaz dificulta comprender el estado de la ubicación y jerarquiza una salida alternativa por encima de la acción necesaria. El rediseño concentra la atención en revisar, confirmar y continuar, por lo que se espera mayor claridad, control y confianza.")]
story += [p("Momento de mayor riesgo","H2x"),p("La selección es el momento potencialmente más negativo: dos marcadores visuales y la ausencia de confirmación impiden saber qué ubicación se guardará. La evidencia disponible es visual y heurística; la emoción debe confirmarse con participantes.")]
story += [p("Relación con usabilidad y accesibilidad","H2x"),p("Las mejoras hacen visible el estado del sistema, reducen la carga de decisión, previenen errores y conservan una ruta clara de edición. El contraste, las etiquetas y la redundancia entre icono y texto favorecen el acceso sin depender únicamente del color.")]
story += [p("Diferencia esperada antes y después","H2x"),p("Se espera que el rediseño reduzca incertidumbre durante búsqueda y selección y aumente satisfacción al finalizar. Esta diferencia es una hipótesis de diseño, no un resultado, hasta completar la prueba.")]
story += [p("Pendientes para la entrega final","H2x"),p("Completar datos de tres participantes, reemplazar la curva provisional, completar integrantes y contribuciones, añadir la URL del repositorio y publicar los archivos en GitHub."),Spacer(1,.3*cm)]
story += [p("Fuentes","H2x"),p("Prototipo original: https://github.com/juANO2202/HCI-2026-G1/blob/main/prototipos/original/B-4-mapa.png.jpeg", "Smallx"),p("Consigna: Tarea grupal - Interacción Humano-Computador, tema Emoción y experiencia de usuario.","Smallx")]

doc.build(story,onFirstPage=header_footer,onLaterPages=header_footer)
print(OUT)
