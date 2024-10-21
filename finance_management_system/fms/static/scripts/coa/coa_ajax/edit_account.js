$(document).ready(function () {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie("csrftoken");

  // Handle the edit button click and populate modal with existing data
  $(".edit_button").on("click", function () {
    const accountId = $(this).data("account-id");

    // Populate the modal fields with current data using AJAX
    $.ajax({
      url: `/get_account/${accountId}/`,
      type: "GET",
      success: function (response) {
        $("#account_code").val(response.account_code);
        $("#account_description").val(response.account_description);
        $("#account_type").val(response.account_type);
        $(
          "input[name=nature_of_log][value=" + response.nature_of_log + "]"
        ).prop("checked", true);
      },
    });
  });

  // Live validation while editing
  $("#edit_account_modal input, #edit_account_modal select").on(
    "change keyup",
    function () {
      const accountId = $("#edit_account_modal").data("account-id");
      const data = {
        account_code: $("#account_code").val(),
        account_description: $("#account_description").val(),
        account_type: $("#account_type").val(),
        nature_of_log: $("input[name=nature_of_log]:checked").val(),
        live_validation: true,
      };

      $.ajax({
        url: `/edit_account/${accountId}/`,
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        data: data,
        success: function (response) {
          if (!response.success) {
            // Handle live validation errors (e.g., show messages near input fields)
            for (const field in response.errors) {
              $("#" + field + "_error").text(response.errors[field]);
            }
          } else {
            // Clear error messages if validation passes
            $(".error-message").text("");
          }
        },
      });
    }
  );

  // When Save Changes is clicked, show confirmation modal
  $("#save_changes_button").on("click", function () {
    $("#edit_account_confirmation_modal").modal("show");
  });

  // Proceed with editing after confirmation
  $("#edit_account_confirmation_modal .btn-danger").on("click", function () {
    const accountId = $("#edit_account_modal").data("account-id");
    const data = {
      account_code: $("#account_code").val(),
      account_description: $("#account_description").val(),
      account_type: $("#account_type").val(),
      nature_of_log: $("input[name=nature_of_log]:checked").val(),
    };

    $.ajax({
      url: `/edit_account/${accountId}/`,
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      data: data,
      success: function (response) {
        if (response.success) {
          location.reload(); // Reload the page on success
        } else {
          // Show errors if any
          alert("Error: " + response.errors);
        }
      },
    });
  });
});
