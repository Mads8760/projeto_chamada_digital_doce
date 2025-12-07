# 🎼 Chamada Digital - Doce de Flautas

Sistema de gestão de frequência e matrícula desenvolvido para o grupo de iniciação artística **Doce de Flautas** (Universidade Estadual do Ceará - UECE).

O projeto substitui o antigo caderno de chamadas em papel por uma aplicação web responsiva, facilitando o controle pedagógico e a geração de relatórios para a coordenação.

## 🔗 Acesso ao Sistema

### O deploy foi realizado e o sistema está em uso privado pela coordenação do projeto.

---

## 🚀 Funcionalidades

O sistema foi desenhado para atender ao fluxo real da coordenação:

1.  **Matrícula de Alunos:** Cadastro completo com Nome, Curso, Tipo de Flauta (Soprano, Contralto, etc.), Telefone e necessidades especiais.
2.  **Agendamento de Ensaios:** Registro de datas, horários, local e repertório a ser trabalhado.
3.  **Chamada Digital:** Interface intuitiva para registrar a presença dos alunos em cada ensaio específico.
4.  **Relatórios Automáticos:** Botão para exportar a base de dados em formato **CSV** (compatível com Excel Brasileiro), facilitando a prestação de contas do projeto.
5.  **Navegação Integrada:** Menu fluido para alternar entre cadastro e chamada.

---

## 🛠️ Tecnologias Utilizadas

Este é um projeto **Full-Stack** (Back-end e Front-end) desenvolvido com:

- **Linguagem:** Python 3.10
- **Framework Web:** Flask
- **Banco de Dados:** SQLite (com SQLAlchemy ORM)
- **Front-end:** HTML5, CSS3 (Design Responsivo e Clean)
- **Deploy (Nuvem):** PythonAnywhere

---

## ⚙️ Estrutura do Banco de Dados

O sistema utiliza um banco relacional com três entidades principais:

- **Aluno:** Dados cadastrais do músico.
- **Ensaio:** Dados do evento (Data, Hora, Repertório).
- **Chamada:** Tabela associativa que vincula *Muitos Alunos* a *Muitos Ensaios* (Relacionamento N:N), registrando a presença.

---

## 💻 Como Rodar Localmente

Se você é desenvolvedor e quer testar o código na sua máquina:

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/SEU_USUARIO/projeto_chamada_digital_doce.git](https://github.com/SEU_USUARIO/projeto_chamada_digital_doce.git)
    cd projeto_chamada_digital_doce
    ```

2.  **Crie o ambiente virtual e instale as dependências**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Inicialize o Banco de Dados e Rode o Servidor**
    ```bash
    python run.py
    ```
    O sistema estará disponível em `http://127.0.0.1:5000/matricula`.

---
**Desenvolvido por Madelu Lopes** 🎸💻
*Projeto voluntário para apoio à educação musical.*
