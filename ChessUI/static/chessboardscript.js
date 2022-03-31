
window.addEventListener('load', function ()
{ 
    boardElement = document.getElementById('board');
    size = document.getElementById('size').value;
    boardElement.style.width = size*80;
    boardElement.style.height = size*80;
    boardElement.style.margin = 20 ;
    boardElement.style.border = "25px solid #333" ;


});