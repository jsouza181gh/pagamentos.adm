/project
│
├── app.py
├── models/
│   └── usuario_model.py
├── repositories/
│   └── usuario_repository.py
├── services/
│   └── usuario_service.py
├── routes/
│   └── usuario_routes.py
└── templates/


Model - Define as tabelas e entidades do banco	Estrutura de dados
	>> (Fornece ao Repository as entidades do banco)

Repository - Faz o CRUD direto no banco - Acesso a dados
	<< (Recebe do Model as entidades do banco)
	>> (Fornece ao Service funções para operações no banco)

Service - Aplica as regras de negócio e chama o repositório - Lógica de negócio
	<< (Recebe do Repository as funções de operações no banco)
	>> (Fornece ao Route as funções de regras de negócio e validação)

Route - Recebe a requisição HTTP, chama o service e retorna resposta - Interface da aplicação
	<< (Recebe do Service as funções de regras de negócio e validação)
	>> (Fornece ao HTML as rotas e informações validadas)


| Camada                 | Função                                                                                       |   Recebe de   |   Fornece para   |
| ---------------------- | -------------------------------------------------------------------------------------------- | ------------- | ---------------- |
| Model                  | Define as tabelas e entidades do banco (estrutura de dados)                                  | —             | Repository       |
| Repository             | Executa operações de CRUD e consultas diretas no banco (acesso a dados)                      | Model         | Service          |
| Service                | Aplica regras de negócio, validações e orquestra chamadas ao repositório (lógica de negócio) | Repository    | Route            |
| Route (ou Controller)  | Recebe requisições HTTP, chama o service e retorna respostas (interface da aplicação)        | Service       | HTML / API       |
| View                   | Exibe os dados e interage com o usuário (interface visual)                                   | Route         | Usuário          |
