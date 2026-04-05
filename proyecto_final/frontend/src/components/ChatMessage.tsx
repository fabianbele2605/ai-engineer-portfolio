import { SourceBadge } from "./SourceBadge";

interface ChatMessageProps {
  role: "user" | "ai";
  text: string;
  fuentes?: string[];
}

export function ChatMessage({ role, text, fuentes }: ChatMessageProps) {
  if (role === "user") {
    return (
      <div className="flex justify-end">
        <div className="bg-chat-user text-chat-user-foreground rounded-2xl rounded-tr-sm px-4 py-3 max-w-[75%]">
          <p className="text-sm leading-relaxed whitespace-pre-wrap">{text}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex items-start gap-3 max-w-3xl">
      <div className="w-8 h-8 rounded-full bg-accent flex items-center justify-center shrink-0">
        <span className="text-xs font-semibold text-muted-foreground">AI</span>
      </div>
      <div className="flex flex-col gap-2">
        <div className="bg-chat-ai text-chat-ai-foreground rounded-2xl rounded-tl-sm px-4 py-3">
          <p className="text-sm leading-relaxed whitespace-pre-wrap">{text}</p>
        </div>
        {fuentes && fuentes.length > 0 && (
          <div className="flex flex-wrap gap-1.5 pl-1">
            {fuentes.map((f) => (
              <SourceBadge key={f} source={f} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
