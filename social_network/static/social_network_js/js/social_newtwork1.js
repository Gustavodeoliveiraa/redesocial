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
    
    
});