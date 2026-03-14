import { useState } from 'react';
import api from './api';

export default function Login({ onLoginSuccess }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/token/', { username, password });
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
      onLoginSuccess();
    } catch (error) {
      alert('Erro ao fazer login. Verifique suas credenciais.');
    }
  };

  return (
    <div className="container">
      <h2>Login - ToDo Advanced</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Usuário:</label>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div className="form-group">
          <label>Senha:</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button type="submit" className="btn">Entrar</button>
      </form>
    </div>
  );
}