// $(document).ready(function () {
//   function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== "") {
//       const cookies = document.cookie.split(";");
//       for (let i = 0; i < cookies.length; i++) {
//         const cookie = cookies[i].trim();
//         if (cookie.substring(0, name.length + 1) === name + "=") {
//           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//           break;
//         }
//       }
//     }
//     return cookieValue;
//   }

//   const csrftoken = getCookie("csrftoken");

//   $(document).on("click", ".deactivate_button", function () {
//     var accountCode = $(this).data("account-code");
//     $("#deactivate_account_modal").data("account-code", accountCode);
//   });

//   $("#deactivate_account_modal .red_button").click(function (e) {
//     e.preventDefault();

//     var accountCode = $("#deactivate_account_modal").data("account-code");
//     var deactivateUrl = "/deactivate_account/" + accountCode + "/";

//     $.ajax({
//       url: deactivateUrl,
//       type: "POST",
//       headers: { "X-CSRFToken": csrftoken },
//       success: function (response) {
//         if (response.success) {
//           $("#deactivate_account_modal").modal("hide");
//           alert("Account deactivated successfully!");
//           location.reload();
//         } else {
//           alert("Failed to deactivate account.");
//         }
//       },
//       error: function () {
//         alert("Something went wrong!");
//       },
//     });
//   });
// });
