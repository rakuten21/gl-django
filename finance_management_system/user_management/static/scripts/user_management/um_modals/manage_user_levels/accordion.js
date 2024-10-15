document
  .getElementById("custom_access")
  .addEventListener("change", function () {
    document
      .getElementById("custom_access_accordion")
      .classList.remove("d-none");
  });

document.getElementById("full_access").addEventListener("change", function () {
  document.getElementById("custom_access_accordion").classList.add("d-none");
});
