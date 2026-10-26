const button = document.getElementById('calculateBtn'); // Найти кнопку по ее айди

button.addEventListener('click', function() { //При нажатии на кнопку происходит button.classList.add('pressed');
    button.classList.add('pressed');
    setTimeout(function() {
        button.classList.remove('pressed'); // Убрать класс через 300 миллисекунд
    }, 300);
});