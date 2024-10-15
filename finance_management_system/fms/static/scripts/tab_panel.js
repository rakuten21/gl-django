// Listen for Bootstrap tab change
document.querySelectorAll('button[data-bs-toggle="tab"]').forEach((el) => {
  el.addEventListener("shown.bs.tab", () => {
    DataTable.tables({ visible: true, api: true }).columns.adjust();
  });
});
