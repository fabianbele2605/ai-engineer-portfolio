const colorMap: Record<string, string> = {
  aws: "bg-source-aws/20 text-source-aws border-source-aws/30",
  python: "bg-source-python/20 text-source-python border-source-python/30",
  ml: "bg-source-ml/20 text-source-ml border-source-ml/30",
  azure: "bg-source-azure/20 text-source-azure border-source-azure/30",
};

export function SourceBadge({ source }: { source: string }) {
  const classes = colorMap[source.toLowerCase()] ?? "bg-source-default/20 text-source-default border-source-default/30";
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium border ${classes}`}>
      {source}
    </span>
  );
}
