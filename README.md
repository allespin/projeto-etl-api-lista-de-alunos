# Pipeline de dados com integração via API 🎓

Desenvolvimento de uma pipeline de dados simplificada. O projeto consiste em uma API que disponibiliza os dados após um processo de ETL (Extração, Transformação e Carga) realizado a partir de um arquivo CSV com nomes de alunos. 

A solução permite que dados armazenados localmente sejam consumidos de forma estruturada por serviços em nuvem, como o Google Colab, simulando um cenário real de integração de dados.


## 🚀 Tecnologias Utilizadas
- **Python**
- **Google Colab**
- **FastAPI**: Criação da API e documentação automática (Swagger).
- **Pandas**: Para leitura e manipulação do arquivo CSV.
- **Uvicorn**: Servidor para rodar a aplicação.
- **Ngrok**: Permite expor a API via nuvem para qualquer pessoa acessar remotamente

## 📋 Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie o servidor: `uvicorn main:app --reload`
3. Acesse o Swagger em: `http://127.0.0.1:8000/docs`
