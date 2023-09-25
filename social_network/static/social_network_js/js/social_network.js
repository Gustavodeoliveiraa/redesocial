document.addEventListener('DOMContentLoaded', function () {
   const img = document.getElementById('select');
   const divHidden = document.querySelector('.modalImga')
   
   img.addEventListener('click', (e) => {
      const styleDiv = window.getComputedStyle(divHidden)
      if (styleDiv.getPropertyValue('display') == 'none') {
         divHidden.style.display = "block"
      }
   })
});