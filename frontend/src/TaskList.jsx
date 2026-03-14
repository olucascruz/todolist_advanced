import { useEffect, useState } from 'react';
import api from './api';

export default function TaskList() {
  const [tasks, setTasks] = useState([]);

  // Busca as tarefas do Django quando o componente carrega
  const fetchTasks = async () => {
    try {
      const response = await api.get('/tasks/');
      // Como o DRF usa paginação, os dados estão em response.data.results
      setTasks(response.data.results);
    } catch (error) {
      console.error("Erro ao carregar tarefas", error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // Lógica para marcar como concluída (Requisito F)
  const toggleComplete = async (task) => {
    try {
      await api.patch(`/tasks/${task.id}/`, { completed: !task.completed });
      fetchTasks(); // Recarrega a lista
    } catch (error) {
      alert("Erro ao atualizar tarefa");
    }
  };

  return (
    <div className="container">
      <h3>Minhas Tarefas</h3>
      {tasks.length === 0 ? <p>Nenhuma tarefa encontrada.</p> : (
        tasks.map(task => (
          <div key={task.id} className="task-card">
            <div>
              <strong style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
                {task.title}
              </strong>
              <p style={{ fontSize: '0.8rem', color: '#666' }}>{task.description}</p>
            </div>
            <button onClick={() => toggleComplete(task)} className="btn">
              {task.completed ? 'Desmarcar' : 'Concluir'}
            </button>
          </div>
        ))
      )}
    </div>
  );
}