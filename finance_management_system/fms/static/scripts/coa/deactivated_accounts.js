new DataTable("#list_of_deactivated_table", {
  layout: {
    top9Start: {
      pageLength: {
        menu: [10, 25, 50, 100],
      },
    },
    top9End: null,
    bottomEnd: {
      paging: {
        className: "paging_custom",
        buttons: 4,
      },
    },

    topStart: {
      buttons: [
        {
          extend: "copy",
          className: "custom_button",
          text: "Copy",
        },
        {
          extend: "csv",
          className: "custom_button",
          text: "CSV",
        },
        {
          extend: "excel",
          className: "custom_button",
          text: "Excel",
        },
        {
          extend: "pdf",
          className: "custom_button",
          text: "PDF",
        },
        {
          extend: "print",
          className: "custom_button",
          text: "Print",
        },
      ],
    },
    topEnd: {
      search: {
        placeholder: "Search...",
      },
    },
  },
  language: {
    lengthMenu: "Show _MENU_ entries per page",
    search: "Filter:",
  },
});
