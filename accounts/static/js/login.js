const loginContainer = document.getElementById('login-content');

// Função para adicionar ou remover a classe "move" no loginContainer
const moveOverlay = () => {
  loginContainer.classList.toggle('move');
  localStorage.setItem('moveState', loginContainer.classList.contains('move'));
};

// Recuperar o estado da classe "move" do LocalStorage quando a página for carregada
window.addEventListener('load', () => {
  const moveState = localStorage.getItem('moveState');
  if (moveState === 'true') {
    loginContainer.classList.add('move');
  }
});

// Adicionar event listeners aos botões
document.getElementById('open-register').addEventListener('click', moveOverlay);
document.getElementById('open-login').addEventListener('click', moveOverlay);
document.getElementById('register-mobile').addEventListener('click', moveOverlay);
document.getElementById('login-mobile').addEventListener('click', moveOverlay);

// script modal

const button_model = document.getElementById('updateDetails');
const modal_id = document.getElementById('modal');
const close_model = document.getElementById('closeModel')

button_model.onclick = function () {
  modal_id.showModal()
};

close_model.onclick = function () {
  modal_id.close()
};