import { useState } from "react";
import { TaskInput } from "@/components/TaskInput";
import { TaskCard, TaskCategory } from "@/components/TaskCard";
import { useToast } from "@/hooks/use-toast";
import waveBackground from "@/assets/wave-background.jpg";

interface Task {
  id: string;
  text: string;
  category: TaskCategory;
}

const Index = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const { toast } = useToast();

  const categorizeTask = async (taskText: string): Promise<TaskCategory> => {
    try {
      const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";
      const response = await fetch(`${apiUrl}/tag-task`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ task: taskText }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      
      const data = await response.json();
      // Response format: { "task": "Gym", "category": "Health" }
      return data.category as TaskCategory;
    } catch (error) {
      console.error("Categorization failed:", error);
      // Fallback to "Other" if API fails
      return "Other";
    }
  };

  const handleAddTask = async (taskText: string) => {
    setIsLoading(true);
    try {
      const category = await categorizeTask(taskText);
      const newTask: Task = {
        id: Date.now().toString(),
        text: taskText,
        category,
      };
      setTasks([newTask, ...tasks]);
      toast({
        title: "Task added",
        description: `Categorized as ${category}`,
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to add task. Please try again.",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div
      className="min-h-screen flex items-center justify-center p-4 relative"
      style={{
        backgroundImage: `url(${waveBackground})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
      }}
    >
      <div className="absolute inset-0 bg-background/60 backdrop-blur-sm" />
      
      <div className="relative z-10 w-full max-w-3xl">
        <header className="text-center mb-12">
          <h1 className="text-5xl md:text-6xl font-bold text-foreground mb-3 tracking-tight">
            AI To-Do List
          </h1>
          <p className="text-muted-foreground text-lg">
            Smart task categorization with NLP
          </p>
        </header>

        <div className="glass-card p-8 rounded-3xl space-y-8">
          <TaskInput onAddTask={handleAddTask} isLoading={isLoading} />

          <div className="space-y-3">
            {tasks.length === 0 ? (
              <div className="text-center py-12 text-muted-foreground">
                <p className="text-lg">No tasks yet. Add your first task above!</p>
              </div>
            ) : (
              tasks.map((task) => (
                <TaskCard
                  key={task.id}
                  id={task.id}
                  text={task.text}
                  category={task.category}
                />
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
