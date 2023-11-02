/* promo_project/promo/static/promo/script.js */

// Пример JavaScript-кода
document.addEventListener('DOMContentLoaded', function() {
  // Код, который будет выполнен после полной загрузки DOM страницы
});
function toggleMenu() {
    var navbarMenu = document.getElementById("navbarMenu");
    navbarMenu.classList.toggle("show");
}


document.addEventListener("DOMContentLoaded", function() {
    var toggler = document.querySelector(".navbar-toggler");
    toggler.addEventListener("click", toggleMenu);
});