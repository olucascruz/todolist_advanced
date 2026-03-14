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