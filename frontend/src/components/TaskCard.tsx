import { ShoppingBag, Briefcase, Heart, User, MoreHorizontal } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export type TaskCategory = "Shopping" | "Work" | "Health" | "Personal" | "Other";

interface TaskCardProps {
  id: string;
  text: string;
  category: TaskCategory;
}

const categoryConfig: Record<TaskCategory, { icon: React.ElementType; color: string }> = {
  Shopping: { icon: ShoppingBag, color: "bg-blue-500/10 text-blue-400 border-blue-500/20" },
  Work: { icon: Briefcase, color: "bg-purple-500/10 text-purple-400 border-purple-500/20" },
  Health: { icon: Heart, color: "bg-rose-500/10 text-rose-400 border-rose-500/20" },
  Personal: { icon: User, color: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20" },
  Other: { icon: MoreHorizontal, color: "bg-gray-500/10 text-gray-400 border-gray-500/20" },
};

export const TaskCard = ({ text, category }: TaskCardProps) => {
  const { icon: Icon, color } = categoryConfig[category];

  return (
    <div className="glass-card p-4 rounded-2xl flex items-center justify-between gap-4 task-enter hover:bg-card/40 transition-colors">
      <p className="text-foreground flex-1 text-base">{text}</p>
      <Badge
        variant="outline"
        className={`${color} flex items-center gap-2 px-3 py-1.5 font-medium border`}
      >
        <Icon className="w-4 h-4" />
        {category}
      </Badge>
    </div>
  );
};
