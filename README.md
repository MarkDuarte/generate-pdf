# API REST em Flask - Gerador de PDF

Esta é uma API REST desenvolvida em Flask que permite a geração de arquivos PDF utilizando a biblioteca **ReportLab**. A API possui um endpoint principal para enviar dados e gerar o PDF. A validação dos dados fornecidos é feita com o **Marshmallow**.

---

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **ReportLab**: Biblioteca para criação de documentos PDF.
- **Marshmallow**: Biblioteca para validação de dados e serialização.

---

## Instalação

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina (versão 3.7 ou superior).

1. Clone este repositório:
   ```bash
   git clone https://github.com/MarkDuarte/generate-pdf.git
   cd pdf

## Endpoints

### Post / generate-pdf

Este endpoint recebe os dados no formato JSON e gera um arquivo PDF com base nas informações fornecidas.
**URL**: /generate-pdf
**Método HTTP**: POST

**title** (obrigatório): Título do documento.
**content** (obrigatório): Conteúdo do relatório.
**author** (Obrigátorio): Autor do documento.

## Executando o endpoint:
      ```
      curl -X POST http://127.0.0.1:5000/generate-pdf \
      -H "Content-Type: application/json" \
      -d '{
        "title": "Relatório de Vendas",
        "content": "Este é um relatório detalhado de vendas do mês.",
        "author": "Marcos"
      }'
      ```

## Exemplo em json:
  ```json
    {
      "title": "Relatório de Vendas",
      "content": "Este é um relatório detalhado de vendas do mês.",
      "author": "Marcos Duarte"
    }
