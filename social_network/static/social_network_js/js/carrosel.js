document.addEventListener("DOMContentLoaded", function () {

    let currentItem = 0;

    const divStatus = document.querySelector('.status')
    const carrousel = document.querySelector(".carousel")

    const controls = document.querySelectorAll(".control");
    const item = document.querySelectorAll(".item");
    const larguraItem = item[0].offsetWidth;
  
    const maxItems = item.length - 1;


    if (carrousel.offsetWidth > divStatus.offsetWidth){
      controls.forEach((control) => {
        control.addEventListener("click", (e) => {
          isLeft = e.target.classList.contains("arrow-left");
    
          
  
            if (isLeft) {
              if (currentItem <= 0){
                currentItem = maxItems 
              }
              else {
                currentItem -= 1;
              }
              carrousel.style.transform = `translateX(-${currentItem * larguraItem}px)`
    
            } else {
  
              if (currentItem > maxItems - 1) {
                currentItem = 0
              }
              else {
                currentItem += 1;
              }
              carrousel.style.transform = `translateX(-${currentItem * larguraItem}px)`
    
            }
  
            item.forEach((items)=>items.classList.remove('current-item'))
            item[currentItem].classList.add('current-item')
        });
      });
    }else{
      // If all statuses fit on the screen, the carousel controls do not appear
      item.forEach((items)=>items.classList.add('current-item'))
      controls.forEach((element)=>element.style.display = 'none')
    }
    

    // hiding the status div if it has no status

    const statusDiv = document.querySelector('.status')
    const carouselDiv = document.querySelector('.carousel')
    const numChildDIv = carouselDiv.childElementCount;

    if (numChildDIv === 0) {
      statusDiv.style.height = 0

    }
    else {
      statusDiv.style.height = 250
      
    }


});
