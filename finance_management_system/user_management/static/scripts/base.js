document.addEventListener("DOMContentLoaded", () => {
  // Select all submenu items
  const submenuItems = document.querySelectorAll(".submenu_item");

  // Add click event listener to each submenu item
  submenuItems.forEach((item) => {
    item.addEventListener("click", () => {
      // Toggle the submenu visibility
      const submenu = item.nextElementSibling;
      submenu.classList.toggle("show");

      // Rotate the arrow icon
      const arrow = item.querySelector(".arrow-left");
      arrow.classList.toggle("rotate");
    });
  });
});
