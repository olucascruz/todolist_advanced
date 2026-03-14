🚀 Advanced To-Do List | olucascruz
Uma solução robusta e escalável para gerenciamento de tarefas, projetada com foco em alta performance, segurança e arquitetura modular. Este projeto demonstra a aplicação prática de padrões de projeto modernos e uma separação clara de responsabilidades entre o ecossistema de backend e frontend.

🛠️ Stack Tecnológica
Backend (Core Engine)
Python 3.11+ & Django 6.0: Framework robusto para o núcleo da aplicação.

Django REST Framework (DRF): Construção de uma API robusta, seguindo os princípios RESTful.

SimpleJWT: Autenticação stateless segura via JSON Web Tokens.

Pytest & Pytest-Django: Suíte de testes automatizados para garantia de qualidade e cobertura de código.

Frontend (Interface)
React & Vite: Frontend ultra-rápido com suporte a HMR (Hot Module Replacement).

Axios: Gerenciamento centralizado de requisições HTTP e interceptors de autenticação.

Modern CSS: Interface focada em usabilidade (UX) e design limpo.

🏗️ Arquitetura e Engenharia de Software
A aplicação foi desenvolvida sob o paradigma da Engenharia de Software Orientada a Objetos, aplicando rigorosamente os seguintes conceitos:

1. Princípios SOLID
Responsabilidade Única (SRP): Separação clara entre modelos de dados, lógica de negócio (Services) e comunicação externa (Gateways).

Desacoplamento via Signals: Implementação de Django Signals para processamento de eventos secundários (como gamificação), garantindo que a falha em um serviço externo não impacte o fluxo principal da aplicação.

2. Padrões de Projeto (Design Patterns)
Gateway Pattern: Centralização da comunicação com APIs externas em uma camada específica, facilitando a manutenção e testes (Mocks).

Service Layer: Abstração da lógica de negócio para além dos Views tradicionais, mantendo o código DRY (Don't Repeat Yourself).


🚀 Como Executar o Projeto
Para rodar a aplicação localmente, certifique-se de ter o Python 3.11+ e o Node.js instalados em sua máquina.

1. Clonando o Repositório
Bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
2. Configurando o Backend (Django)
Abra um terminal na pasta raiz do projeto e siga os passos:

Bash
# Entrar na pasta do backend
cd backend

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Realizar as migrações do banco de dados
python manage.py migrate

# Criar um superusuário para acessar o Admin (Opcional)
python manage.py createsuperuser

# Iniciar o servidor
python manage.py runserver
O servidor estará disponível em: http://127.0.0.1:8000

3. Configurando o Frontend (React + Vite)
Abra um novo terminal na pasta raiz do projeto:

Bash
# Entrar na pasta do frontend
cd frontend

# Instalar as dependências do Node
npm install

# Iniciar o servidor de desenvolvimento
npm run dev
O frontend estará disponível em: http://localhost:5173

🧪 Executando Testes Automatizados
A qualidade do código é garantida por uma suíte de testes robusta. Para executá-los, utilize o ambiente virtual do backend ativo:

Bash
cd backend
pytest -v
📌 Observações Importantes
CORS: O backend já está configurado para aceitar requisições do endereço padrão do Vite (localhost:5173).

Autenticação: Para testar os endpoints protegidos, utilize a rota /api/token/ para gerar o token JWT ou a tela de Login no frontend.

API Externa: A integração com o serviço de gamificação utiliza um Gateway com fallback, garantindo que o sistema funcione mesmo se o serviço externo estiver offline.