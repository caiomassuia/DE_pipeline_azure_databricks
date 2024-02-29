
# Projeto de Engenharia de Dados: Alura DataBricks e Data Factory
## Descrição:

Este projeto demonstra a aplicação de conhecimentos em engenharia de dados através da construção de um pipeline completo utilizando Databricks, Data Factory e Azure Data Lake Gen2. O objetivo é processar dados brutos de imóveis, transformá-los e armazená-los em diferentes camadas para análise.

## Tecnologias utilizadas:

  * **Databricks:** plataforma para processamento de dados em grande escala.
  * **Data Factory:** serviço de integração de dados em nuvem.
  * **Azure Data Lake Gen2:** armazenamento de dados em nuvem para grandes volumes.
## Etapas do projeto:

**1. Configuração do ambiente:**

  * Integração do Databricks e Data Factory com o Git para controle de versionamento.
**2. Armazenamento de dados brutos:**

  * Carregamento dos dados brutos de imóveis no Data Lake Gen2.

**3. Camada Bronze:**

  * Processamento dos dados brutos no Databricks:
      * Remoção de colunas desnecessárias.
      * Renomeação de colunas para melhor legibilidade.
  * Armazenamento dos dados processados na camada Bronze do Data Lake Gen2.

**4. Camada Silver:**

  * Seleção dos dados específicos que serão usados na análise.
  * Transformação dos dados para a estrutura desejada.
  * Armazenamento dos dados processados na camada Silver do Data Lake Gen2.
    
## Resultados:

  * Pipeline de dados completo e funcional para processar dados de imóveis.
  * Dados brutos armazenados de forma segura e organizada no Data Lake Gen2.
  * Camadas Bronze e Silver prontas para serem utilizadas em análises posteriores.
