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
                     </div>
                  </a>
                  `
                  suggestions.insertAdjacentHTML('beforeend', htmlInsert);
               });
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

});

