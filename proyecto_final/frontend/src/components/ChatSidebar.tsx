import { useState } from "react";
import { MessageSquare, FileText, History, X } from "lucide-react";
import { getHistorial, getDocumentos, type HistorialItem, type Documento } from "@/lib/api";

interface ChatSidebarProps {
  open: boolean;
  onClose: () => void;
}

export function ChatSidebar({ open, onClose }: ChatSidebarProps) {
  const [tab, setTab] = useState<"history" | "docs">("history");
  const [historial, setHistorial] = useState<HistorialItem[]>([]);
  const [documentos, setDocumentos] = useState<Documento[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const loadHistory = async () => {
    setTab("history");
    setLoading(true);
    setError("");
    try {
      setHistorial(await getHistorial());
    } catch {
      setError("No se pudo cargar el historial");
    } finally {
      setLoading(false);
    }
  };

  const loadDocs = async () => {
    setTab("docs");
    setLoading(true);
    setError("");
    try {
      setDocumentos(await getDocumentos());
    } catch {
      setError("No se pudieron cargar los documentos");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {open && (
        <div className="fixed inset-0 bg-background/60 z-40 md:hidden" onClick={onClose} />
      )}
      <aside
        className={`fixed top-0 left-0 h-full w-72 bg-sidebar border-r border-sidebar-border z-50 flex flex-col transition-transform duration-300 ${
          open ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="flex items-center justify-between p-4 border-b border-sidebar-border">
          <div className="flex items-center gap-2">
            <MessageSquare className="w-5 h-5 text-primary" />
            <h1 className="text-base font-semibold text-foreground">AI Engineer - Document Chat</h1>
          </div>
          <button onClick={onClose} className="text-muted-foreground hover:text-foreground transition-colors">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="flex border-b border-sidebar-border">
          <button
            onClick={loadHistory}
            className={`flex-1 flex items-center justify-center gap-1.5 py-3 text-xs font-medium transition-colors ${
              tab === "history" ? "text-primary border-b-2 border-primary" : "text-muted-foreground hover:text-foreground"
            }`}
          >
            <History className="w-3.5 h-3.5" /> Historial
          </button>
          <button
            onClick={loadDocs}
            className={`flex-1 flex items-center justify-center gap-1.5 py-3 text-xs font-medium transition-colors ${
              tab === "docs" ? "text-primary border-b-2 border-primary" : "text-muted-foreground hover:text-foreground"
            }`}
          >
            <FileText className="w-3.5 h-3.5" /> Documentos
          </button>
        </div>

        <div className="flex-1 overflow-y-auto scrollbar-thin p-3 space-y-2">
          {loading && <p className="text-xs text-muted-foreground text-center py-4">Cargando...</p>}
          {error && <p className="text-xs text-destructive text-center py-4">{error}</p>}

          {!loading && !error && tab === "history" && historial.length === 0 && (
            <p className="text-xs text-muted-foreground text-center py-4">Haz clic en "Historial" para cargar</p>
          )}

          {tab === "history" &&
            historial.map((item, i) => (
              <div key={i} className="rounded-lg bg-sidebar-hover p-3 space-y-1">
                <p className="text-xs font-medium text-foreground truncate">{item.pregunta}</p>
                <p className="text-xs text-muted-foreground line-clamp-2">{item.respuesta}</p>
              </div>
            ))}

          {!loading && !error && tab === "docs" && documentos.length === 0 && (
            <p className="text-xs text-muted-foreground text-center py-4">Haz clic en "Documentos" para cargar</p>
          )}

          {tab === "docs" &&
            documentos.map((doc, i) => (
              <div key={i} className="rounded-lg bg-sidebar-hover p-3 flex items-center gap-2">
                <FileText className="w-4 h-4 text-muted-foreground shrink-0" />
                <span className="text-xs text-foreground truncate">{doc.nombre}</span>
              </div>
            ))}
        </div>
      </aside>
    </>
  );
}
