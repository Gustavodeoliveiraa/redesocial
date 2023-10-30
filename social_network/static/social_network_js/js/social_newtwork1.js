document.addEventListener("DOMContentLoaded", function() {

    // option for change profile image
    const profileImageDiv = document.querySelector(".image_profile")
    const changeProfileImage = document.querySelector(".modal_change_picture")

    profileImageDiv.addEventListener("click", ()=> {
        const profileImageDiv = getComputedStyle(changeProfileImage);

        if (profileImageDiv.getPropertyValue("display") == "none") {
            changeProfileImage.style.display = "block"
        }
        else {
            changeProfileImage.style.display = "none"
        }
    })
    //
    
    // option for change the post for public or private

    const publicOrPrivate = document.querySelector('.post_form')
    const iconPrivateOrPublic = publicOrPrivate.querySelector('i')
    const textPrivateOrPublic = publicOrPrivate.querySelector('p')
    const publicOrPrivateCheckbox = publicOrPrivate.querySelector('#post_form_checkbox')

    publicOrPrivate.addEventListener('click', (e) => {
        e.preventDefault()

        if(!publicOrPrivateCheckbox.checked == true){
            iconPrivateOrPublic.classList.remove('fa-lock')
            iconPrivateOrPublic.classList.add('fa-lock-open')
            textPrivateOrPublic.textContent = 'This post will be public'

            publicOrPrivateCheckbox.checked = true
        }
        else {
            iconPrivateOrPublic.classList.remove('fa-lock-open')
            iconPrivateOrPublic.classList.add('fa-lock')
            textPrivateOrPublic.textContent = 'This post will be private'

            publicOrPrivateCheckbox.checked = false
        }
        
    })

    // clear span tag in textarea when be in focus

    const span = document.querySelector('.text_for_new_post')
    const textarea = document.querySelector('textarea')
    const maxCharacters = 299;

    textarea.addEventListener('input', () => {
        if (textarea.value.length > 0) {
            span.style.display = 'none';
        }
        else{
            span.style.display = 'block';
        }

        // setting the height of textarea

        textarea.style.height = 'auto';
        textarea.style.height = (textarea.scrollHeight) + 'px'

        // limits the length of characters

        if (textarea.value.length > maxCharacters) {
            textarea.value = textarea.value.substring(0, maxCharacters)
        }
    })


    // friend search bar
    const searchBar = document.getElementById('all_users');
    const suggestions = document.getElementById('suggestions');

    searchBar.addEventListener('input', function() {
        const searchInputValue = searchBar.value.trim();

        // checking if searchInputValue is not none
        if (searchInputValue) {
            const endpoint = `${window.location.href}search_user/${searchInputValue}`

            fetch(endpoint)
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    suggestions.innerHTML = '';
                    data.user.forEach(user => {
                        const htmlInsert = 
                        `
                            <a href="${user.username}">
                                <div class="image_profile_search search_img">
                                <img src="${user.image}" alt="" class="image_profile">
                                <span class="username" >${user.username}</span>
                                <div class="add" data-user-id="${user.username}">Adicionar</div>
                                </div>
                            </a>
                        `
                        suggestions.insertAdjacentHTML('beforeend', htmlInsert)
                    })

                    // button for add user
                    const buttons = document.querySelectorAll('.add')
                    buttons.forEach(button => {
                       button.addEventListener('click', (e)=>{
                            e.preventDefault()
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
        }
        else {
            // Se searchQuery estiver vazio, você pode limpar a div 'suggestions'.
            suggestions.innerHTML = '';
        }
    })

    // sending form post
    const buttonSubmit = document.querySelector('.span_send_post')
    const formThinking = document.querySelector('.text')
    const formPublicOrPrivate = document.querySelector('.post_form')

    buttonSubmit.addEventListener('click', (e)=>{
        e.preventDefault()
        formThinking.submit()
    })

});