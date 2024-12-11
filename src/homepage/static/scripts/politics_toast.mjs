document.addEventListener("DOMContentLoaded", () => {
  const toast = document.getElementById("bottom-toast");

  // close dialog when clicked
  const close = () => toast.style.display = "none";
  toast.addEventListener("click", close);

  // alternatively, also close dialog after 20 seconds
  setTimeout(close, 15 * 1000);
});
