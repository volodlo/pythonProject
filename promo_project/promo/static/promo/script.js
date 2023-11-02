/* promo_project/promo/static/promo/script.js */

// Пример JavaScript-кода
document.addEventListener('DOMContentLoaded', function() {
  // Код, который будет выполнен после полной загрузки DOM страницы
});
function toggleMenu() {
    var menu = document.getElementById("navbarMenu");
    menu.classList.toggle("active");
}

document.addEventListener("DOMContentLoaded", function() {
    var toggler = document.querySelector(".navbar-toggler");
    toggler.addEventListener("click", toggleMenu);
});