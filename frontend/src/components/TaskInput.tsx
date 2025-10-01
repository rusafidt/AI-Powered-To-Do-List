import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Plus } from "lucide-react";

interface TaskInputProps {
  onAddTask: (task: string) => void;
  isLoading?: boolean;
}

export const TaskInput = ({ onAddTask, isLoading }: TaskInputProps) => {
  const [taskText, setTaskText] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (taskText.trim()) {
      onAddTask(taskText);
      setTaskText("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-3 w-full">
      <Input
        type="text"
        placeholder="Enter your task..."
        value={taskText}
        onChange={(e) => setTaskText(e.target.value)}
        className="flex-1 h-14 text-lg bg-secondary/50 border-border/50 focus-visible:ring-accent"
        disabled={isLoading}
      />
      <Button
        type="submit"
        disabled={!taskText.trim() || isLoading}
        className="h-14 px-8 bg-accent hover:bg-accent/90 text-accent-foreground font-medium"
      >
        <Plus className="w-5 h-5 mr-2" />
        Add Task
      </Button>
    </form>
  );
};
