document.addEventListener("DOMContentLoaded", () => {
  // Botão de listar arquivos
  const btnListar = document.getElementById("btnListar");
  btnListar.addEventListener("click", async (event) => {
    event.preventDefault();
    await listar();
  });

  // Botão de upload
  const btnUpload = document.getElementById("btnUpload");
  btnUpload.addEventListener("click", async (event) => {
    event.preventDefault();
    await uploadFile();
  });
});

async function listar() {
  let arquivos = await eel.list_files_exposed(".")();
  let lista = document.getElementById("lista");
  lista.innerHTML = "";
  arquivos.forEach(item => {
    let li = document.createElement("li");
    li.textContent = item;
    li.classList.add("item"); // aplica estilo via class
    lista.appendChild(li);
  });
}

async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  if (!file) {
    alert("Selecione um arquivo!");
    return;
  }

  const reader = new FileReader();
  reader.onload = async function(e) {
    const base64Data = btoa(
      new Uint8Array(e.target.result)
        .reduce((acc, byte) => acc + String.fromCharCode(byte), "")
    );
    const stats = await eel.save_and_analyze(base64Data, file.name)();
    document.getElementById("output").innerText = JSON.stringify(stats, null, 2);
  };
  reader.readAsArrayBuffer(file);
}

// Exporta para testes
export { listar, uploadFile };

