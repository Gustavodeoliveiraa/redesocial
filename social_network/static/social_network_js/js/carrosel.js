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
          inline: "center"
        });
  
        if (maxItems > 1) {
          items[currentItem].classList.remove("current-item");
        }
      });
    });
  });
