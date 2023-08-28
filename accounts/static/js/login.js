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

// ajax 
$(document).ready(function() {
  $(".form_modal").submit(function(event){
    event.preventDefault();
  
    var form_ = $('#reset')
    var form_data = $(this).serialize();
    const message = $('#message');


    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: form_data,
      success: function messageDialog(response){
        
        if (response.email == "Email send") {
          message.removeClass('message-error')
          message.append(response.email)
          message.addClass('message-success')
        }
        else{
          message.removeClass('message-success')
          message.append(response.email)
          message.addClass('message-error')
        }
        setTimeout(function() {
          $('#message').empty()
          message.removeClass('message-success message-error');
          location.reload();
          window.close();
        }, 2000);
        
      },
    })
  })
})

