document.addEventListener("DOMContentLoaded", function () {
    const controls = document.querySelectorAll(".control");
    let currentItem = 0;
    const items = document.querySelectorAll(".item");
    const maxItems = items.length;
  
    if (maxItems == 1) {
      items[currentItem].classList.remove("current-item");
    }
    controls.forEach((control) => {
      control.addEventListener("click", (e) => {
        isLeft = e.target.classList.contains("arrow-left");
  
        if (isLeft) {
          currentItem -= 1;
        } else {
          currentItem += 1;
        }
  
        if (currentItem >= maxItems) {
          currentItem = 0;
        }
  
        if (currentItem < 0) {
          currentItem = maxItems - 1;
        }
  
        items.forEach((item) => item.classList.remove("current-item"));

        items[currentItem].scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
  
        if (maxItems > 1) {
          items[currentItem].classList.remove("current-item");
        }
      });
    });

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
