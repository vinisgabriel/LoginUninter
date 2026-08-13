# 🚀 Univirtus Auto-Login & Screen Setup

> Script em Python com Selenium para automação de login no portal **Univirtus (UNINTER)** e ajuste automático de zoom na tela.

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo automatizar o processo repetitivo de login na plataforma acadêmica **Univirtus**. Ele aguarda os elementos da tela carregarem, preenche as credenciais do usuário, efetua o login e ajusta o nível de zoom da página para proporcionar uma melhor visualização do painel acadêmico.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/)** — Linguagem principal do projeto.
* **[Selenium WebDriver](https://www.selenium.dev/)** — Automação de navegadores web.
* **[ChromeDriver](https://chromedriver.chromium.org/)** — Driver para integração com o Google Chrome.

---

## 🚀 Funcionalidades

* ⏳ **Aguardar carregamento dinâmico:** Utiliza `WebDriverWait` para garantir que o formulário de login esteja visível antes de interagir.
* 🔐 **Preenchimento automático:** Digita o RU e a senha nos campos correspondentes.
* ⌨️ **Submissão rápida:** Simula o envio do formulário através da tecla `Enter`.
* 🔍 **Ajuste de Zoom:** Reduz automaticamente o zoom da página para **75%** via execução de JavaScript, otimizando o layout visual do portal pós-login.
* 🌐 **Sessão mantida:** Mantém a janela do navegador aberta para navegação manual contínua.

---

## 📦 Pré-requisitos

Antes de iniciar, você precisará ter instalado em sua máquina:
1. **Python 3.8+**
2. **Google Chrome** instalado.
3. Biblioteca do Selenium:

```bash
pip install selenium

🔧 Como Executar
Clone este repositório:
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio

Edite o arquivo com suas credenciais:
Abra o script Python e substitua os valores das variáveis pelas suas credenciais do Univirtus:

# DIGITE SEU RU AQUI EM BAIXO
campo_ru.send_keys("SEU_RU_AQUI")

# DIGITE SUA SENHA AQUI EM BAIXO
campo_senha.send_keys("SUA_SENHA_AQUI")

python main.py
