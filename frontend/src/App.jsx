import { useState } from 'react';
import './App.css';
import Login from './Login';
import TaskList from './TaskList';

function App() {
  // Verifica se já existe um token no navegador
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('access_token'));

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsLoggedIn(false);
  };

  return (
    <div className="App">
      <nav style={{ background: '#f4f4f4', padding: '10px', marginBottom: '20px' }}>
        <h1>olucascruz | ToDo</h1>
        {isLoggedIn && <button onClick={handleLogout}>Sair</button>}
      </nav>

      {!isLoggedIn ? (
        <Login onLoginSuccess={() => setIsLoggedIn(true)} />
      ) : (
        <TaskList />
      )}
    </div>
  );
}

export default App;