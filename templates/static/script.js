const searchInput = document.getElementById("searchInput");
const statusFilter = document.getElementById("statusFilter");
const rows = document.querySelectorAll("#guestTable tr");

function filterTable() {
  const searchValue = searchInput.value.toLowerCase();
  const filterValue = statusFilter.value;

  rows.forEach(row => {
    const name = row.querySelector(".guest-name")?.textContent.toLowerCase();
    const status = row.querySelector(".status")?.classList[1];
    let match = true;

    if (searchValue && !name.includes(searchValue)) match = false;
    if (filterValue && status !== filterValue) match = false;

    row.style.display = match ? "" : "none";
  });
}

let debounceTimer;
searchInput.addEventListener("keyup", () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(filterTable, 300);
});
statusFilter.addEventListener("change", filterTable);

// SweetAlert2 for delete confirmation
document.querySelectorAll(".delete-btn").forEach(btn => {
  btn.addEventListener("click", function(e) {
    e.preventDefault();
    Swal.fire({
      title: 'Delete Guest?',
      text: "This action cannot be undone.",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Yes, delete'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = this.href;
      }
    });
  });
});

// Toast on guest add (optional: use query param like ?added=true)
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('added') === 'true') {
  Swal.fire({
    toast: true,
    position: 'top-end',
    icon: 'success',
    title: 'Guest added successfully!',
    showConfirmButton: false,
    timer: 2000
  });
}