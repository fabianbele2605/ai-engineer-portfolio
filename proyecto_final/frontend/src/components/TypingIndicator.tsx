export function TypingIndicator() {
  return (
    <div className="flex items-start gap-3 max-w-3xl">
      <div className="w-8 h-8 rounded-full bg-accent flex items-center justify-center shrink-0">
        <span className="text-xs font-semibold text-muted-foreground">AI</span>
      </div>
      <div className="bg-chat-ai rounded-2xl rounded-tl-sm px-4 py-3">
        <div className="flex gap-1.5">
          <span className="typing-dot w-2 h-2 rounded-full bg-muted-foreground inline-block" />
          <span className="typing-dot w-2 h-2 rounded-full bg-muted-foreground inline-block" />
          <span className="typing-dot w-2 h-2 rounded-full bg-muted-foreground inline-block" />
        </div>
      </div>
    </div>
  );
}
