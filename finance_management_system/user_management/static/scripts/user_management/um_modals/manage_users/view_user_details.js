document.querySelectorAll("#manage_users_table tbody tr").forEach((row) => {
  row.addEventListener("click", function (event) {
    // Prevent action buttons in the last column from triggering the modal
    if (!event.target.closest(".action_buttons")) {
      // Trigger the modal
      const myModal = new bootstrap.Modal(
        document.getElementById("user_details_modal")
      );
      myModal.show();
    }
  });
});
