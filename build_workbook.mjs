import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = "C:/Users/Sebas2hVR/Desktop/T2.1 Emoción y experiencia de usuario/Tarea_Experiencia_Emocional_UX";
const out = `${root}/matriz/matriz_ux.xlsx`;
const wb = Workbook.create();
const ux = wb.worksheets.add("Matriz UX");
const tests = wb.worksheets.add("Registro pruebas");

ux.getRange("A1:H1").merge();
ux.getRange("A1").values = [["Matriz UX - Confirmación de dirección en mapa"]];
ux.getRange("A2:H2").merge();
ux.getRange("A2").values = [["La emoción reportada y la valoración se completan únicamente después de observar a participantes reales."]];
ux.getRange("A4:H9").values = [
  ["Momento","Emoción reportada","Valoración -3 a +3","Evidencia observable","Captura","Problema","Mejora propuesta","Fundamento IHC"],
  ["1. Ingreso","PENDIENTE","","La oferta, el temporizador y el fondo saturado compiten con el objetivo de confirmar la dirección.","Captura 01 - marcador 1","Jerarquía confusa y presión comercial.","Título orientado a tarea, oferta secundaria y progreso legible.","Correspondencia con la tarea; reducción de carga cognitiva."],
  ["2. Exploración","PENDIENTE","","Mapa y dirección están separados; no hay instrucción sobre cómo revisar o ajustar.","Captura 01 - marcador 2","Baja visibilidad de posibilidades de interacción.","Instrucción breve, mapa delimitado y controles rotulados.","Visibilidad del estado y affordances."],
  ["3. Búsqueda o ajuste","PENDIENTE","","No existe búsqueda visible; el usuario depende de zoom y de un mapa ficticio.","Captura 01 - marcador 3","Falta de control y prevención de errores.","Dirección editable y controles de ajuste explícitos.","Control del usuario; prevención y recuperación de errores."],
  ["4. Selección","PENDIENTE","","El marcador rojo y el punto azul compiten; no se confirma cuál ubicación está activa.","Captura 01 - marcador 4","Estado de selección ambiguo.","Un único marcador, estado 'Punto confirmado' y resumen asociado.","Retroalimentación inmediata y consistencia."],
  ["5. Finalización","PENDIENTE","","'Guardar dirección' parece deshabilitado mientras 'OMITIR' domina visualmente.","Captura 01 - marcador 5","Acción principal ambigua y riesgosa.","CTA primario 'Guardar dirección y continuar' y opción secundaria de edición.","Jerarquía de acciones; prevención de errores; confianza."]
];
ux.getRange("A11:H11").merge(); ux.getRange("A11").values=[["Resultado de validación"]];
ux.getRange("A12:H12").merge(); ux.getRange("A12").values=[["PENDIENTE: completar pruebas con tres participantes y trasladar promedios/evidencias desde la hoja Registro pruebas."]];

tests.getRange("A1:O1").merge(); tests.getRange("A1").values=[["Registro anónimo de prueba antes y después"]];
tests.getRange("A2:O2").merge(); tests.getRange("A2").values=[["Ingrese valores enteros entre -3 y +3. No registre nombres ni datos personales."]];
tests.getRange("A4:O7").values = [
  ["Código","Versión","Ingreso","Explorar","Buscar/Ajustar","Seleccionar","Finalizar","Promedio","Tiempo (s)","Errores","Cita breve","Observación ingreso","Observación exploración","Observación selección","Observación finalización"],
  ["U1","Antes","","","","","","","","","","","","",""],
  ["U2","Antes","","","","","","","","","","","","",""],
  ["U3","Antes","","","","","","","","","","","","",""]
];
tests.getRange("A9:O12").values = [
  ["Código","Versión","Ingreso","Explorar","Buscar/Ajustar","Seleccionar","Finalizar","Promedio","Tiempo (s)","Errores","Cita breve","Observación ingreso","Observación exploración","Observación selección","Observación finalización"],
  ["U1","Después","","","","","","","","","","","","",""],
  ["U2","Después","","","","","","","","","","","","",""],
  ["U3","Después","","","","","","","","","","","","",""]
];
for (const r of [5,6,7,10,11,12]) tests.getRange(`H${r}`).formulas=[[`=IF(COUNT(C${r}:G${r})=5,AVERAGE(C${r}:G${r}),"")`]];
tests.getRange("A14:H17").values = [
  ["Resumen","Ingreso","Explorar","Buscar/Ajustar","Seleccionar","Finalizar","Promedio general","Estado"],
  ["Antes","","","","","","","Pendiente"],
  ["Después","","","","","","","Pendiente"],
  ["Diferencia","","","","","","","Pendiente"]
];
for (let c=2;c<=6;c++) {
  const col=String.fromCharCode(64+c);
  tests.getRange(`${col}15`).formulas=[[`=IF(COUNT(${col}5:${col}7)=3,AVERAGE(${col}5:${col}7),"")`]];
  tests.getRange(`${col}16`).formulas=[[`=IF(COUNT(${col}10:${col}12)=3,AVERAGE(${col}10:${col}12),"")`]];
  tests.getRange(`${col}17`).formulas=[[`=IF(OR(${col}15="",${col}16=""),"",${col}16-${col}15)`]];
}
tests.getRange("G15").formulas=[["=IF(COUNT(B15:F15)=5,AVERAGE(B15:F15),\"\")"]];
tests.getRange("G16").formulas=[["=IF(COUNT(B16:F16)=5,AVERAGE(B16:F16),\"\")"]];
tests.getRange("G17").formulas=[["=IF(OR(G15=\"\",G16=\"\"),\"\",G16-G15)"]];

const header={fill:"#075C4A",font:{name:"Arial",bold:true,color:"#FFFFFF",size:10},wrapText:true,verticalAlignment:"center"};
const title={fill:"#E9F4F0",font:{name:"Arial",bold:true,color:"#075C4A",size:16},verticalAlignment:"center"};
ux.getRange("A1:H1").format=title; ux.getRange("A4:H4").format=header; ux.getRange("A11:H11").format=header;
tests.getRange("A1:O1").format=title; tests.getRange("A4:O4").format=header; tests.getRange("A9:O9").format=header; tests.getRange("A14:H14").format=header;
for (const sh of [ux,tests]) sh.getUsedRange().format.font={name:"Arial",size:10};
ux.getRange("A4:H12").format.wrapText=true; ux.getRange("A4:H12").format.verticalAlignment="center";
tests.getRange("A4:O17").format.wrapText=true; tests.getRange("C5:G7").format.fill="#FFF4CC"; tests.getRange("C10:G12").format.fill="#FFF4CC";
ux.getRange("B5:C9").format.fill="#FFF4CC"; ux.getRange("A5:H9").format.rowHeight=62;
for (const [r,w] of [["A:A",18],["B:B",18],["C:C",15],["D:D",38],["E:E",20],["F:F",28],["G:G",34],["H:H",32]]) ux.getRange(r).format.columnWidth=w;
for (const [r,w] of [["A:A",12],["B:B",12],["C:H",14],["I:J",12],["K:O",28]]) tests.getRange(r).format.columnWidth=w;
ux.freezePanes.freezeRows(4); tests.freezePanes.freezeRows(4);
wb.recalculate();
await fs.mkdir(`${root}/matriz`,{recursive:true});
const preview=await wb.render({sheetName:"Matriz UX",range:"A1:H12",scale:1.2,format:"png"});
await fs.writeFile(`${root}/matriz/matriz_ux_preview.png`,new Uint8Array(await preview.arrayBuffer()));
const file=await SpreadsheetFile.exportXlsx(wb); await file.save(out);
const check=await wb.inspect({kind:"table",range:"Matriz UX!A1:H12",include:"values,formulas",tableMaxRows:12,tableMaxCols:8});
console.log(check.ndjson);
