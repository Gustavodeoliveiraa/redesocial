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

    const publicOrPrivate = document.querySelector('.public')
    const iconPrivateOrPublic = publicOrPrivate.querySelector('i')
    const textPrivateOrPublic = publicOrPrivate.querySelector('p')
    const publicOrPrivateCheckbox = document.querySelector('#post_form_checkbox')

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

    // sending form post
    const buttonSubmit = document.querySelector('.span_send_post')
    const formThinking = document.querySelector('.text')

    buttonSubmit.addEventListener('click', (e)=>{
        e.preventDefault()
        if(textarea.value.length == 0){

        }else{
            formThinking.submit()
        }
    })

    // option for delete a post

    const ellipse = document.querySelectorAll('.delete_content')
    

    try {
        ellipse.forEach(click=>{
            click.addEventListener('click', (event) => {
                const divDeletePost = event.target.closest('.delete_content').querySelector('.delete_post');
                console.log(divDeletePost)
                const hiddenOrVisible = getComputedStyle(divDeletePost);
                console.log(hiddenOrVisible)
                
                if (hiddenOrVisible.getPropertyValue('opacity') === '0') {
                    divDeletePost.style.display = 'block';
                    divDeletePost.style.opacity = '1';
                } else {
                    divDeletePost.style.display = 'none';
                    divDeletePost.style.opacity = '0';
                }
            });
        })
    } catch (error) {
        console.error("Erro ao adicionar evento: " + error.message);
    }


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
                                location.reload()
                            }
        
                            setTimeout(() => {
                                suggestions.innerHTML = '';
                            }, 10)
        
                            setTimeout(friendAdded, 1000)
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

    function setupCarousel() {
        // carousel for status

        let currentStatus = 0

        let start = 0
        console.log(currentStatus)
        
        // reset the div whenever it is clicked
        const divContentStatus = document.querySelector('.status_content')
        divContentStatus.style.transform = `translateX(-${currentStatus * 100}%)`

        const divAllStatus = document.querySelectorAll('.container')
        const maxItem = divAllStatus.length
        const leftButton = document.querySelector('.left_status')
        const rightButton = document.querySelector('.right_status')

        leftButton.addEventListener('click', ()=>{
            if (currentStatus == 0) {
            currentStatus = maxItem - 1 
            }else{
            currentStatus--
            }
            divContentStatus.style.transform = `translateX(-${currentStatus * 100}%)`
            clearInterval(moveStatus)
        })

        rightButton.addEventListener('click', ()=>{
            if (currentStatus == maxItem - 1) {
            currentStatus = 0
            }else{
            currentStatus++
            }
            divContentStatus.style.transform = `translateX(-${currentStatus * 100}%)`
            clearInterval(moveStatus)
        })
    

        // auto move for status
        const newMaxItem = maxItem -1
        function autoMoveStatus() {
            if (start < newMaxItem) {
                currentStatus ++
                start++
                divContentStatus.style.transform = `translateX(-${currentStatus * 100}%)`
            }else{
                clearInterval(moveStatus)
            }
        }

        moveStatus = setInterval(autoMoveStatus, 3000)

        const backgroundStatus = document.querySelector('.background')
        backgroundStatus.style.display = 'block'
    }

    function hiddenOrVisibleDiv(param) {
        const statusDiv = document.querySelector('.status_user_content i')
        const left_status = document.querySelector('.left_status')
        const right_status = document.querySelector('.right_status')

        statusDiv.style.visibility = param
        status_user_content.style.visibility = param
        left_status.style.visibility = param
        right_status.style.visibility = param
    }

    // getting  the data of status of view for show all status of a user

    const carrouselDiv = document.querySelector('.carousel')
    const imgCarrouselLink = carrouselDiv.querySelectorAll('a')
    const carouselContent = document.querySelector('.status_content')
    const status_user_content = document.querySelector('.status_user_content')


    imgCarrouselLink.forEach(link => {
        link.addEventListener('click', (e)=>{
            e.preventDefault()
            const statusDiv = document.querySelector('.status_user_content i')

            // hidden the div of status detail  
            statusDiv.addEventListener('click', ()=> {
                hiddenOrVisibleDiv('hidden')
                const backgroundStatus = document.querySelector('.background')
                backgroundStatus.style.display = 'none'
                clearInterval(moveStatus)
            })
            var linkOfStatusUser =link.getAttribute('data-link').trim()

            // remove leading slash from URL
            if (linkOfStatusUser.startsWith('/')){
                linkOfStatusUser = linkOfStatusUser.slice(1);
            }

            const endpointStatusShow = `${window.location.protocol}//${window.location.host}/status/${linkOfStatusUser}`

            fetch(endpointStatusShow)
            .then(response=>{
                return response.json()
            })
            .then(data=>{
                carouselContent.innerHTML = ''
                
                data.user_status.forEach(user => {
                    const statusContainerDiv = `
                        <div class="container">
                            <div class="user_data">
                                <div class="image_profile">
                                    <img src="${user.profile_image}" alt="">
                                </div>
                                ${user.user}
                            </div>
                            <img src="${user.status_image}" alt="">
                        </div>
                    `

                    carouselContent.insertAdjacentHTML ('beforeend', statusContainerDiv)
                })

                
                // showing  of itens inside of status detail div 
                setupCarousel()
                setInterval(hiddenOrVisibleDiv('visible'),1000)             
                

            })
            .catch(error=>{
                console.log(error)
            })

        })
    })
    // option for delete an friend 

    const buttonDelete = document.querySelectorAll('.all_user_delete')
    const buttonFriendsOpen = document.querySelector('.friends_open')
    const buttonFriendsOpenMobile = document.querySelector('.friends_open_mobile')
    const buttonFriendsClose = document.querySelector('.close')
    const allFriends = document.querySelector('.all_friends')

    function toggleVisibilityFriends() {
        console.log('salve')
        const computedStyle = getComputedStyle(allFriends);
        if (computedStyle.display === 'none') {
            allFriends.style.display = 'flex';
        } else {
            allFriends.style.display = 'none';
        }
    }
    buttonFriendsOpen.addEventListener('click', toggleVisibilityFriends)
    buttonFriendsOpenMobile.addEventListener('click', toggleVisibilityFriends)

    buttonFriendsClose.addEventListener('click', ()=>{
        console.log('salve')
        const computedStyle = getComputedStyle(allFriends);
        if (computedStyle.display === 'none') {
            allFriends.style.display = 'flex';
        } else {
            allFriends.style.display = 'none';
        }

        setInterval(location.reload(), 1000)
    })

    buttonDelete.forEach(button=>{
        button.addEventListener('click', (e)=>{
            e.preventDefault()
            const friendId = e.target.closest('.friend_user')
            const idDiv = friendId.getAttribute('id')
            const deleteEndpoint = `http://${window.location.host}/feed/delete/friend/${idDiv}`;

            fetch(deleteEndpoint)
            
            const divToDelete = document.getElementById(idDiv)

            if (divToDelete){
                divToDelete.remove()
            }

        })
    })

});