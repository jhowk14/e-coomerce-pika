---

# Django DRF Multi-Tenant Template

Este projeto é um template básico para um sistema Django Rest Framework (DRF) multi-tenant, com autenticação via `dj-rest-auth`, documentação de API usando Swagger, suporte a PostgreSQL, envio de e-mails via SMTP, armazenamento de arquivos na AWS S3 com CloudFront, e implantação via Zappa. O template também inclui pacotes adicionais como `drf-writable-nested` e `django-filter` para facilitar o desenvolvimento de APIs robustas e escaláveis.

## Funcionalidades

- **Django Rest Framework (DRF)**
- **Autenticação com `dj-rest-auth`**
- **Documentação da API com Swagger/OpenAPI**
- **Suporte a PostgreSQL**
- **Suporte a Multi-Tenant (Organização-Membro)**
- **Envio de e-mails configurado via SMTP**
- **Armazenamento de arquivos na AWS S3 com CloudFront**
- **Implantação via Zappa**
- **Integração com Debugger Toolbar para desenvolvimento**
- **Filtros avançados com `django-filter`**
- **Suporte a relacionamentos aninhados com `drf-writable-nested`**

---

## Tecnologias Utilizadas

- **Django**: 4.x.x
- **Django Rest Framework (DRF)**: 3.x.x
- **dj-rest-auth**: Para autenticação de usuários com endpoints de login, registro, alteração de senha e redefinição de senha.
- **django-filter**: Suporte a filtros na API DRF.
- **drf-writable-nested**: Manipulação de relacionamentos aninhados no DRF.
- **PostgreSQL**: Banco de dados relacional.
- **Zappa**: Implantação de aplicações serverless na AWS Lambda.
- **AWS S3 & CloudFront**: Para armazenamento de arquivos e entrega de conteúdo.
- **Django Debug Toolbar**: Ferramenta de debug para otimizar o desenvolvimento.

---
