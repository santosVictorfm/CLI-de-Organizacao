🗂️ Organizador de Arquivos

Ferramenta de linha de comando em Python que organiza automaticamente os arquivos de uma pasta, separando-os em subpastas por tipo (imagens, documentos, vídeos...) ou por data (ano/mês).

Ideal para dar um jeito naquela pasta de Downloads que só cresce.



Demonstração

✨ Funcionalidades
Organização por tipo: move cada arquivo para uma pasta de acordo com a extensão
Organização por data: agrupa arquivos em ANO/MÊS com base na data de modificação
Modo simulação (--simular): mostra o que seria feito sem mover nenhum arquivo
Conflitos de nome resolvidos: se foto.jpg já existir no destino, o arquivo vira foto (1).jpg
Logs de todas as operações realizadas
Categorias
Categoria	Extensões
Imagens	.jpg .jpeg .png .gif .webp
Documentos	.pdf .docx .txt .xlsx .pptx
Videos	.mp4 .mkv .mov
Audio	.mp3 .wav .flac
Compactados	.zip .rar .7z .tar .gz
Codigo	.py .ino .js .c .cpp
Outros	qualquer extensão não listada
⚙️ Como funciona

O programa trabalha em duas etapas:

Planejamento: varre a pasta, identifica cada arquivo e calcula para onde ele deve ir, gerando uma lista de movimentos.
Execução: aplica os movimentos, criando as pastas necessárias e tratando conflitos de nome.

Separar as etapas torna o código fácil de testar e faz o modo --simular funcionar de forma natural: ele exibe o plano e para antes da execução.

Downloads/                      Downloads/
├── relatorio.pdf               ├── Documentos/
├── foto.png          ──►       │   └── relatorio.pdf
├── musica.mp3                  ├── Imagens/
└── script.py                   │   └── foto.png
                                ├── Audio/
                                │   └── musica.mp3
                                └── Codigo/
                                    └── script.py

🚀 Instalação

Pré-requisitos: Python 3.10+ e uv (pip install uv).

bash
git clone https://github.com/SEU-USUARIO/organizador-arquivos.git
cd organizador-arquivos
uv sync
<details> <summary>Usando pip em vez de uv</summary>
bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -e .
</details>

💻 Uso
bash
# Organiza por tipo
uv run organizador ~/Downloads

# Mostra o que seria feito, sem mover nada
uv run organizador ~/Downloads --simular

# Organiza por ano/mês
uv run organizador ~/Downloads --por-data

# Ajuda
uv run organizador --help

💡 Dica: rode primeiro com --simular para conferir o resultado antes de mover os arquivos.

📁 Estrutura do projeto
organizador-arquivos/
├── pyproject.toml
├── README.md
├── src/
│   └── organizador/
│       ├── __init__.py
│       ├── categorias.py   # mapeamento extensão → categoria
│       ├── core.py         # lógica de planejamento e execução
│       └── cli.py          # interface de linha de comando (typer)
└── tests/
    └── test_core.py
🧪 Testes e qualidade
bash
uv run pytest          # roda os testes
uv run ruff check .    # verifica o estilo do código
uv run ruff format .   # formata o código

Os testes usam o fixture tmp_path do pytest, que cria pastas temporárias. Nenhum arquivo real é tocado.

🛠️ Tecnologias
Python 3.10+
Typer: interface de linha de comando
pathlib e shutil: manipulação de arquivos
pytest: testes
Ruff: lint e formatação
uv: gerenciamento de ambiente e dependências

🗺️ Próximos passos
 Organização por tipo
 Modo simulação
 Organização por data
 Tratamento de conflitos de nome
 Comando desfazer, revertendo a última organização a partir de um histórico em JSON
 Categorias personalizadas via arquivo de configuração
 Opção para incluir subpastas (modo recursivo)
 CI com GitHub Actions

📚 Aprendizados
Python na prática

Manipulação de arquivos com pathlib e shutil: caminhos, extensões, criar pastas, mover arquivos e ler a data de modificação. Isso aparece em todo script de automação.

Type hints e dataclass: a classe Movimento é um exemplo de como modelar dados de forma clara em vez de passar tuplas e dicionários soltos.

Estruturas de dados: escolher set para as extensões (busca rápida) e dict para as categorias, e entender o motivo.

Tratamento de erros: pasta que não existe, arquivo sem permissão, arquivo em uso. Seu programa precisa falhar de forma educada.

logging: a diferença entre mostrar algo ao usuário e registrar o que aconteceu.

Pensamento de engenharia
Separação de responsabilidades: a lógica (core.py) não sabe que existe um terminal (cli.py). Esse é o mesmo princípio que separa as camadas de uma API no back-end.

Planejar antes de executar: o padrão “gera um plano, depois aplica” é usado em ferramentas sérias, como o terraform plan e as migrações de banco. Ele torna o código previsível e seguro.

Casos de borda: conflito de nomes, arquivo sem extensão, arquivos ocultos, pasta vazia. Pensar nesses casos é o que separa um código que funciona na sua máquina de um código confiável.

Operações destrutivas com cuidado: mover arquivos de alguém é sério. O --simular e o futuro desfazer ensinam a projetar pensando no usuário.

Ferramentas profissionais
pytest com tmp_path: testar código que mexe no sistema de arquivos sem estragar nada. É uma habilidade valorizada, porque muita gente só testa funções “puras”.

Empacotamento: pyproject.toml, layout src/ e entry points. Seu projeto vira um comando instalável de verdade, e não um script solto.

CLI com typer: argumentos, opções e --help automático.


👤 Autor

Victor Santos Ferreira de Morais | Estudante de Engenharia de Software

Github: https://github.com/santosVictorfm
LinkedIn:  https://www.linkedin.com/in/victor-de-morais/