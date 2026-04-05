import { useState, useRef, useEffect } from "react";
import { Send, Menu, MessageSquare } from "lucide-react";
import { ChatMessage } from "@/components/ChatMessage";
import { TypingIndicator } from "@/components/TypingIndicator";
import { ChatSidebar } from "@/components/ChatSidebar";
import { sendChat } from "@/lib/api";

interface Message {
  role: "user" | "ai";
  text: string;
  fuentes?: string[];
}

const Index = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSend = async () => {
    const text = input.trim();
    if (!text || loading) return;

    setInput("");
    setMessages((prev) => [...prev, { role: "user", text }]);
    setLoading(true);

    try {
      const data = await sendChat(text);
      setMessages((prev) => [
        ...prev,
        { role: "ai", text: data.respuesta, fuentes: data.fuentes },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "ai", text: "Error al conectar con el servidor. Asegúrate de que la API esté ejecutándose." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen overflow-hidden">
      <ChatSidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      <div className="flex-1 flex flex-col min-w-0">
        {/* Header */}
        <header className="flex items-center gap-3 px-4 py-3 border-b border-border bg-card">
          <button
            onClick={() => setSidebarOpen(true)}
            className="text-muted-foreground hover:text-foreground transition-colors"
          >
            <Menu className="w-5 h-5" />
          </button>
          <div className="flex items-center gap-2">
            <MessageSquare className="w-5 h-5 text-primary" />
            <h1 className="text-sm font-semibold text-foreground">AI Engineer - Document Chat</h1>
          </div>
        </header>

        {/* Messages */}
        <main className="flex-1 overflow-y-auto scrollbar-thin px-4 py-6">
          <div className="max-w-3xl mx-auto space-y-4">
            {messages.length === 0 && (
              <div className="flex flex-col items-center justify-center h-[60vh] text-center">
                <div className="w-16 h-16 rounded-2xl bg-accent flex items-center justify-center mb-4">
                  <MessageSquare className="w-8 h-8 text-primary" />
                </div>
                <h2 className="text-lg font-semibold text-foreground mb-1">¿En qué puedo ayudarte?</h2>
                <p className="text-sm text-muted-foreground max-w-md">
                  Pregunta sobre tus documentos de AWS, Python, ML o Azure. Powered by RAG + Claude.
                </p>
              </div>
            )}

            {messages.map((msg, i) => (
              <ChatMessage key={i} role={msg.role} text={msg.text} fuentes={msg.fuentes} />
            ))}

            {loading && <TypingIndicator />}
            <div ref={bottomRef} />
          </div>
        </main>

        {/* Input */}
        <div className="border-t border-border bg-card px-4 py-3">
          <div className="max-w-3xl mx-auto flex gap-2">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && handleSend()}
              placeholder="Escribe tu pregunta..."
              className="flex-1 bg-input text-foreground placeholder:text-muted-foreground rounded-xl px-4 py-3 text-sm outline-none focus:ring-2 focus:ring-ring transition-shadow"
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || loading}
              className="bg-primary text-primary-foreground rounded-xl px-4 py-3 hover:opacity-90 disabled:opacity-40 transition-opacity"
            >
              <Send className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
