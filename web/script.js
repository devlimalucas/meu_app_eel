async function listar() {
  let arquivos = await eel.list_files_exposed(".")();
  let lista = document.getElementById("lista");
  lista.innerHTML = "";
  arquivos.forEach(item => {
    let li = document.createElement("li");
    li.textContent = item;
    lista.appendChild(li);
  });

  console.log("Xablau");
  
}
