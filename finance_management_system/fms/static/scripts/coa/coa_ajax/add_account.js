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

  function updateValidation(field, errorMsg, isSubmit) {
    const inputField = $(`#${field}`);

    if (errorMsg) {
      inputField.removeClass("is-valid").addClass("is-invalid");
      $(`#${field}_error`).text(errorMsg);

      // Add shake effect only on submit
      if (isSubmit) {
        inputField.addClass("shake");
        setTimeout(() => {
          inputField.removeClass("shake");
        }, 300);
      }
    } else {
      inputField.removeClass("is-invalid").addClass("is-valid");
      $(`#${field}_error`).text("");
    }
  }

  function liveValidate(field) {
    const formData = {
      account_code: $("#account_code").val(),
      account_description: $("#account_description").val(),
      account_type: $("#account_type").val(),
      nature_of_log: $('input[name="nature_of_log"]:checked').val(),
      live_validation: true,
    };

    $.ajax({
      url: $("#add_account_modal .red_button").data("url"),
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      data: formData,
      success: function (response) {
        const errors = response.errors || {};

        if (field === "account_code") {
          updateValidation(field, errors.account_code, false);
        }
        if (field === "account_description") {
          updateValidation(field, errors.account_description, false);
        }
        if (field === "account_type") {
          updateValidation(field, errors.account_type, false);
        }
        if (field === "nature_of_log") {
          updateValidation(field, errors.nature_of_log, false);
        }
      },
    });
  }

  // Live validation listeners
  $("#account_code").on("input", function () {
    liveValidate("account_code");
  });

  $("#account_description").on("input", function () {
    liveValidate("account_description");
  });

  $("#account_type").on("change", function () {
    liveValidate("account_type");
  });

  $('input[name="nature_of_log"]').on("change", function () {
    liveValidate("nature_of_log");
  });

  // Form submit logic
  $("#add_account_modal .red_button").click(function (e) {
    e.preventDefault();

    const formData = {
      account_code: $("#account_code").val(),
      account_description: $("#account_description").val(),
      account_type: $("#account_type").val(),
      nature_of_log: $('input[name="nature_of_log"]:checked').val(),
    };

    $.ajax({
      url: $(this).data("url"),
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      data: formData,
      success: function (response) {
        const errors = response.errors || {};

        if (Object.keys(errors).length === 0) {
          // No validation errors, hide modal and show success message
          $("#add_account_modal").modal("hide");
          alert("Account added successfully!");
          location.reload();
        } else {
          // Handle validation errors (shake effect is added on submit)
          updateValidation("account_code", errors.account_code, true);
          updateValidation(
            "account_description",
            errors.account_description,
            true
          );
          updateValidation("account_type", errors.account_type, true);
          updateValidation("nature_of_log", errors.nature_of_log, true);

          // Check for missing "Nature of Log" selection and show error
          if (!$('input[name="nature_of_log"]:checked').val()) {
            updateValidation(
              "nature_of_log",
              "Please select a nature of log",
              true
            );
          }
        }
      },
      error: function () {
        // Display a generic error message
        $("#form_error").text(
          "An unexpected error occurred. Please try again later."
        );
      },
    });
  });
});
