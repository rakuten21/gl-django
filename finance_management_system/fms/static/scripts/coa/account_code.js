document.getElementById("account_code").addEventListener("input", function () {
  var accountCode = this.value;
  var accountTypeDropdown = document.getElementById("account_type");

  var firstDigit = accountCode.charAt(0);

  switch (firstDigit) {
    case "1":
      accountTypeDropdown.value = "Asset";
      break;
    case "2":
      accountTypeDropdown.value = "Liability";
      break;
    case "3":
      accountTypeDropdown.value = "Equity";
      break;
    case "4":
      accountTypeDropdown.value = "Revenue";
      break;
    case "5":
      accountTypeDropdown.value = "Expense";
      break;
    default:
      accountTypeDropdown.value = "Choose account type"; // No selection
      break;
  }
});
