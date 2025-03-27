# Súmario da documentação

Na pasta SQL tem o passo a passo para instalação do servidor MySQL 8 e instalação da interface gráfica MySQL Workbench

Possiveis problemas que podems ser encontrados:
  O processo de instalação do MySQL e Workbench aparecem varias opções para personalizar, no geral não precisa mudar nada, só dar next next e funciona mas da uma lida antes de dar next para ver se esta tudo certinho
  
  O MySQL tem uma configuração padrão de segurança que ele não aceita dados vindos de arquivos da maquina então para facilitar e você não precisar abrir os arquivos de configuração e realizar as devidas modificações você precisa colocar os arquivos na pasta

  `C:\ProgramData\MySQL\MySQL Server 8.0\Uploads`

  então você separa e coloca o arquivo da 3.2 solto na pasta Uploads mesmo e os 8 arquivos da 3.1 em duas pastas dentro de Uploads ficando então

Uploads/
- Arquivo da 3.2.csv
- 2023/
  - Arquivo da 3.1 de 2023.csv
  - Arquivo da 3.1 de 2023.csv
  - Arquivo da 3.1 de 2023.csv
  - Arquivo da 3.1 de 2023.csv
- 2024/
  - Arquivo da 3.1 de 2024.csv
  - Arquivo da 3.1 de 2024.csv
  - Arquivo da 3.1 de 2024.csv
  - Arquivo da 3.1 de 2024.csv

Para que assim os arquivos possam ser acessados pelo MySQL



Qualquer duvida durante o processo de teste entra em contato comigo
XD
