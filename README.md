# Projeto ETL: Lista de Alunos 🎓

Este projeto é uma API simples que realiza o processo de ETL (Extração, Transformação e Carga) para listar nomes a partir de um arquivo CSV. Funciona como a criação de sistema simples que permite que dados que estão no seu computador local sejam acessados e processados por qualquer outro serviço na nuvem como o Google Colab.


## 🚀 Tecnologias Utilizadas
- **Python**
- **FastAPI**: Criação da API e documentação automática (Swagger).
- **Pandas**: Para leitura e manipulação do arquivo CSV.
- **Uvicorn**: Servidor para rodar a aplicação.
- **nGrok**: Permite expor a API via nuvem para qualquer pessoa acessar remotamente

## 📋 Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie o servidor: `uvicorn main:app --reload`
3. Acesse o Swagger em: `http://127.0.0.1:8000/docs`
