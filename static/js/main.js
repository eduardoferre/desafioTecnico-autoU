function toggleInputFields() {
    var fileType = document.getElementById("fileType").value;
    document.getElementById("pdfUpload").style.display = (fileType === "pdf") ? "block" : "none";
    document.getElementById("txtInput").style.display = (fileType === "txt") ? "block" : "none";
}

window.onload = function () {
    toggleInputFields();
}

document.getElementById("fileUpload").addEventListener("change", function () {
  var file = this.files[0];
  if (!file) {
    this.value = "";
    return;
  }
  var allowedTypes = ["application/pdf", "text/plain"];
  if (!allowedTypes.includes(file.type)) {
    alert("Por favor, selecione um arquivo PDF ou TXT.");
    this.value = ""; 
  }
});



document.querySelector("form").addEventListener("submit", function (event) {
    var fileType = document.getElementById("fileType").value;
    if (fileType === "pdf" && document.getElementById("fileUpload").files.length === 0) {
        alert("Por favor, faça o upload de um arquivo PDF.");
        event.preventDefault();
    } else if (fileType === "txt" && document.getElementById("textInput").value.trim() === "") {
        alert("Por favor, cole o texto no campo de texto.");
        event.preventDefault();
    }
})

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const loader = document.getElementById('loader');
  const submitButton = form.querySelector('input[type="submit"]');

  form.addEventListener('submit', function () {
    // Mostrar loader
    loader.style.display = 'block';

    // Desabilitar botão submit para evitar múltiplos envios
    submitButton.disabled = true;
  });
});
