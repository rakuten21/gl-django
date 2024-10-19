$(document).ready(function () {
  // Function to get the CSRF token from the cookies
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie("csrftoken"); // Get CSRF token from cookies

  $("#add_account_modal .red_button").click(function (e) {
    e.preventDefault();

    // Fetch the URL from the button's data-url attribute
    var addAccountUrl = $(this).data("url");

    var formData = {
      account_code: $("#account_code").val(),
      account_description: $("#account_description").val(),
      account_type: $("#account_type").val(),
      nature_of_log: $('input[name="nature_of_log"]:checked').val(),
    };

    $.ajax({
      url: addAccountUrl, // Use the correct URL
      type: "POST",
      headers: { "X-CSRFToken": csrftoken }, // Add CSRF token in request header
      data: formData,
      success: function (response) {
        if (response.success) {
          $("#add_account_modal").modal("hide");
          alert("Account added successfully!");
          location.reload(); // Optional: Reload the page to see the new account
        } else {
          alert("Failed to add account: " + JSON.stringify(response.errors));
        }
      },
      error: function () {
        alert("Something went wrong!");
      },
    });
  });
});
