// Função para alternar os campos de upload / texto conforme seleção
function toggleInputFields() {
  var fileType = document.getElementById("fileType").value;
  document.getElementById("pdfUpload").style.display = (fileType === "pdf") ? "block" : "none";
  document.getElementById("txtInput").style.display = (fileType === "txt") ? "block" : "none";
}

// Executa ao carregar a página para ajustar os campos conforme seleção padrão
window.onload = function () {
  toggleInputFields();
};

// Validação do tipo de arquivo no input file
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

// Evento único para validar formulário e controlar loader no submit
document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const loader = document.getElementById('loader');
  const submitButton = form.querySelector('input[type="submit"]');

  form.addEventListener('submit', function (event) {
    const fileType = document.getElementById('fileType').value;

    // Validações
    if (fileType === 'pdf' && document.getElementById('fileUpload').files.length === 0) {
      alert('Por favor, faça o upload de um arquivo PDF.');
      event.preventDefault();
      return; // Impede que o loader apareça
    }

    if (fileType === 'txt' && document.getElementById('textInput').value.trim() === '') {
      alert('Por favor, cole o texto no campo de texto.');
      event.preventDefault();
      return; // Impede que o loader apareça
    }

    // Se passou nas validações, mostra loader e desabilita botão
    loader.style.display = 'block';
    submitButton.disabled = true;
  });
});
