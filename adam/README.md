# adam

## No linux
1. Create and enter virtual environment
  * `virtualenv --clear env`
  * `source env/bin/activate`
2. Install adam requirements to the virtual env
  * `pip install -r requirements.txt
3. Install plugin requirements to the virtual env
  * ufpbots example: `pip install -r ufpbots/requirements.txt`

## No windows (por Helon)
1. Abrir `git-cmd`.
2. Navegar com "cd" até a pasta onde quer salvar o projeto. Chamarei de ".".
3. Clonar o repositório: git clone https://github.com/rsmarinho/adam.git. Uma pasta é criada: "./adam".
4. Entrar na pasta adam: `cd adam`
5. Criar o ambiente virtual: `python -m venv venv`. O 2° venv é o nome do ambiente. Poderia ser qualquer nome...
6. Ativar o ambiente virtual (supondo que você esteja na pasta adam): `venv\Scripts\activate`. Deve aparecer "(venv)" no início do caminho do git-cmd.
7. Instalar pacotes requeridos usando pip 1 (supondo que você esteja na pasta adam com venv ativado): `pip install -r requirements.txt`.
8. Instalar pacotes requeridos usando pip 2 (supondo que você esteja na pasta adam com venv ativado): `pip install -r ufpbots/requirements.txt`
9. Rodar aplicação: `python adam.py`

No final: 
  * Fechar o ambiente virtual no git-cmd: `venv\Scripts\deactivate`. Deve sumir o "(venv)" do início do caminho. 
  * Agora pode fechar o git-cmd com exit.
