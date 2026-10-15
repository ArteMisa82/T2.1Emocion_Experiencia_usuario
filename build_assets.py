from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Users\Sebas2hVR\Desktop\T2.1 Emoción y experiencia de usuario")
BASE = ROOT / "Tarea_Experiencia_Emocional_UX"
for p in [BASE/"evidencias"/"original", BASE/"evidencias"/"pruebas_usuarios", BASE/"curva_emocional", BASE/"matriz", BASE/"rediseño", BASE/"informe"]:
    p.mkdir(parents=True, exist_ok=True)

orig = Image.open(ROOT/"prototipo-original.jpeg").convert("RGB")
orig.save(BASE/"evidencias"/"original"/"B-4-mapa-original.jpeg", quality=94)
red = Image.open(ROOT/"rediseño-figma.png").convert("RGB")
red.save(BASE/"rediseño"/"rediseño-figma.png")

font_paths = [r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf"]
bold = ImageFont.truetype(font_paths[0], 28)
small = ImageFont.truetype(font_paths[0], 20)

# Evidencia numerada sobre la interfaz original.
ann = orig.copy()
d = ImageDraw.Draw(ann)
points = [(360,46),(680,229),(177,631),(774,430),(1012,674)]
labels = ["1","2","3","4","5"]
for (x,y), lab in zip(points, labels):
    d.ellipse((x-22,y-22,x+22,y+22), fill="#075C4A", outline="white", width=4)
    box=d.textbbox((0,0),lab,font=bold)
    d.text((x-(box[2]-box[0])/2,y-(box[3]-box[1])/2-2),lab,font=bold,fill="white")
ann.save(BASE/"evidencias"/"original"/"captura-01-momentos-anotados.png")

# Comparación antes/después.
W,H=1500,780
canvas=Image.new("RGB",(W,H),"#F5F7F6")
d=ImageDraw.Draw(canvas)
d.text((40,24),"Comparación visual antes y después",font=bold,fill="#111E1B")
def fit(im, box):
    x,y,w,h=box; cp=im.copy(); cp.thumbnail((w,h)); px=x+(w-cp.width)//2; py=y+(h-cp.height)//2; canvas.paste(cp,(px,py)); return px,py,cp.width,cp.height
d.rounded_rectangle((30,80,730,740),radius=20,fill="white",outline="#D5DFDB",width=2)
d.rounded_rectangle((770,80,1470,740),radius=20,fill="white",outline="#D5DFDB",width=2)
d.text((55,100),"ANTES · Interfaz original",font=small,fill="#B42318")
d.text((795,100),"DESPUÉS · Rediseño en Figma",font=small,fill="#075C4A")
fit(orig,(50,150,660,540)); fit(red,(790,150,660,540))
canvas.save(BASE/"rediseño"/"antes_despues.png")

def curve(path, values=None, title="Curva emocional antes y después - plantilla"):
    im=Image.new("RGB",(1500,720),"white"); q=ImageDraw.Draw(im)
    q.text((60,32),title,font=bold,fill="#111E1B")
    left,top,right,bottom=120,110,1430,590
    moments=["Ingreso","Explorar","Buscar","Seleccionar","Finalizar"]
    xs=[left+i*(right-left)//4 for i in range(5)]
    for val in range(-3,4):
        y=bottom-(val+3)*(bottom-top)//6
        q.line((left,y,right,y),fill="#D5DFDB",width=2)
        q.text((72,y-12),f"{val:+d}",font=small,fill="#52605C")
    for x,label in zip(xs,moments):
        q.text((x-45,bottom+28),label,font=small,fill="#52605C")
    if values is not None:
        pts=[]
        for x,val in zip(xs,values):
            y=bottom-(val+3)*(bottom-top)//6; pts.append((x,y))
        q.line(pts,fill="#075C4A",width=6)
        for x,y in pts: q.ellipse((x-10,y-10,x+10,y+10),fill="#075C4A",outline="white",width=3)
        q.text((270,650),"NO corresponde a usuarios evaluados; sustituir con datos reales de 3 participantes.",font=small,fill="#B42318")
    im.save(path)

curve(BASE/"curva_emocional"/"curva_emocional.png",[0,-1,-2,-3,-1],"Estimación heurística de la experiencia original")
curve(BASE/"evidencias"/"pruebas_usuarios"/"plantilla_curva_vacia.png")

print(BASE)
