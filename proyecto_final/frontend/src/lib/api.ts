const API_BASE = "http://localhost:8000";

export interface ChatResponse {
  pregunta: string;
  respuesta: string;
  contexto: string[];
  fuentes: string[];
}

export interface HistorialItem {
  pregunta: string;
  respuesta: string;
  fuentes?: string[];
}

export interface Documento {
  nombre: string;
  tipo?: string;
}

export async function sendChat(texto: string, k = 3): Promise<ChatResponse> {
  const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ texto, k }),
  });
  if (!res.ok) throw new Error("Error en la respuesta del servidor");
  return res.json();
}

export async function subirDocumento(archivo: File): Promise<{mensaje: string, fragmentos_totales: number}> {
  const form = new FormData();
  form.append("archivo", archivo);
  const res = await fetch(`${API_BASE}/subir`, { method: "POST", body: form });
  if (!res.ok) throw new Error("Error al subir archivo");
  return res.json();
}

export async function getHistorial(): Promise<HistorialItem[]> {
  const res = await fetch(`${API_BASE}/historial`);
  if (!res.ok) throw new Error("Error al obtener historial");
  const data = await res.json();
  return data.historial;
}

export async function getDocumentos(): Promise<Documento[]> {
  const res = await fetch(`${API_BASE}/documentos`);
  if (!res.ok) throw new Error("Error al obtener documentos");
  const data = await res.json();
  return Object.keys(data.documentos).map((k) => ({ nombre: k }));
}
