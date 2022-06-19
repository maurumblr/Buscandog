const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".header-menu-items");

navToggle.addEventListener("click", () => {
  navMenu.classList.toggle("header-menu-items_visible");

  if (navMenu.classList.contains("nav-menu_visible")) {
    navToggle.setAttribute("aria-label", "Cerrar menú");
  } else {
    navToggle.setAttribute("aria-label", "Abrir menú");
  }
});