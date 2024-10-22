// MONKEY PATCHING


/* 
comando do console
desativa todos triggers de clique de mouse
*/

document.addEventListener('click', function(event) {
    event.stopPropagation();
    event.preventDefault();
}, true);
  
/*
comando do console
substitui o evento setTimeout por um que não faz nada
*/

window.setTimeout = function(fn, delay) {
    console.log('SetTimeout foi bloqueado.');
    return -1;  // Retorna um ID de temporizador inválido
};
  
/*
para reavivar, recarregar a página
*/


// Salvar referência aos comportamentos originais do documento e setTimeout
var originalClickListener = document.addEventListener;
var originalSetTimeout = window.setTimeout;

// Desativar os eventos de clique
document.addEventListener = function(type, listener, useCapture) {
  if (type === 'click') {
    return;
  }
  return originalClickListener.call(this, type, listener, useCapture);
};

// Substituir comportamento do setTimeout
window.setTimeout = function() {
  console.log('SetTimeout foi bloqueado.');
  return -1;  // Retorna um ID de temporizador inválido
};


/*
comando do console
desativar o onmouseout de todo mundo
*/


// Obter todos os elementos do documento
var allElements = document.querySelectorAll('*');

// Iterar sobre todos os elementos e anular o evento onMouseOut
allElements.forEach(function(element) {
  element.onmouseout = null;
});
