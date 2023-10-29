document.addEventListener('DOMContentLoaded', function () {
   const img = document.getElementById('select');
   const divHidden = document.querySelector('.modalImga')
   
   img.addEventListener('click', (e) => {
      const styleDiv = window.getComputedStyle(divHidden)
      if (styleDiv.getPropertyValue('display') == 'none') {
         divHidden.style.display = "block"
      }
      else {
         divHidden.style.display = "none"
      }
   })



   const search = document.getElementById('all_users');
   const suggestions = document.getElementById('suggestions');
   
   search.addEventListener('input', function() {
      const searchQuery = search.value.trim();
   
      // Verificar se searchQuery não está vazio ou indefinido
      if (searchQuery) {
         const endpoint = `${window.location.href}search_user/${searchQuery}`;

         fetch(endpoint)
            .then(response => {
               console.log('response', response)
               return response.json();
            })
            .then(data => {
               suggestions.innerHTML = '';
               data.user.forEach(user => {
                  const htmlInsert = `
                  <a href="${user.username}">
                     <div id="user_link_profile">
                        <img src="${user.image}" alt="" id="profile_image">
                        <span class="username" >${user.username}</span>
                        <button class="add" data-user-id="${user.username}">Adicionar</button>
                     </div>
                  </a>
                  `
                  suggestions.insertAdjacentHTML('beforeend', htmlInsert);
               });
               // add friends
               const buttons = document.querySelectorAll('.add')
               buttons.forEach(button => {
                  button.addEventListener('click', ()=>{
                     const attr = button.getAttribute('data-user-id')
                     const friend_endpoint = `${window.location.href}add/${attr}`

                     const dialog = document.querySelector('.content_add')
                     dialog.style.display = 'flex'
                     function friendAdded() {
                        dialog.style.display = 'none'
                     }

                     setTimeout(() => {
                        suggestions.innerHTML = '';
                     }, 10)

                     setTimeout(friendAdded, 1500)
                     fetch(friend_endpoint)
                  })
               })

            })
            .catch(error => {
               console.error('Erro na solicitação HTTP:', error);
            });

      } else {
         // Se searchQuery estiver vazio, você pode limpar a div 'suggestions'.
         suggestions.innerHTML = '';
      }
   });

   search.addEventListener('blur', () => {
      setTimeout(() => {
         suggestions.innerHTML = '';
         search.value = '';
      }, 200);
   })

   // public or private option

   const divPublicOrPrivate = document.querySelector('.public_post')
   const checkbox = document.querySelector('#post_form_text')
   const iconPrivateOrPublic = divPublicOrPrivate.querySelector('i')
   const paragraphPrivateOrPublic = divPublicOrPrivate.querySelector('p')

   divPublicOrPrivate.addEventListener('click', (event) => {
      event.preventDefault()

      if (checkbox.checked) {
         iconPrivateOrPublic.classList.remove('fa-lock-open')
         iconPrivateOrPublic.classList.add('fa-lock')
         paragraphPrivateOrPublic.textContent = 'This post will be private'
         checkbox.checked = false
         checkbox.value = "private";
         console.log(checkbox.value)
      }
      else {
         iconPrivateOrPublic.classList.remove('fa-lock')
         iconPrivateOrPublic.classList.add('fa-lock-open')
         paragraphPrivateOrPublic.textContent = 'This post will be public'
         checkbox.checked = true
         checkbox.value = "public";
         console.log(checkbox.value)
      }
   })

   // button for sending new post 

   const buttonSend = document.querySelector('.fa-share');
   const postForm = document.querySelector('#post_form');
   const spanTextarea = document.querySelector('.text_span')

   const textarea = document.querySelector('.textarea')

   textarea.addEventListener('input', function () {
      if (textarea.value.length > 0) {
          spanTextarea.style.display = 'none';
      } else {
          spanTextarea.style.display = 'block'; 
      }
  });

   buttonSend.addEventListener('click', (event) => {
      event.preventDefault();
      spanTextarea.style.display = 'none'
      console.log('enviado', event);
      console.log(checkbox.value)
      postForm.submit()
   });


});

