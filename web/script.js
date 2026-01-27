async function mostrarArquivos() {
    // Mostra a pasta configurada
    document.getElementById("pasta").textContent = await eel.get_env_folder()();

    // Chama a função Python exposta
    let arquivos = await eel.listar_arquivos()();
    
    // Atualiza a lista na página
    let lista = document.getElementById("lista");
    lista.innerHTML = "";
    arquivos.forEach(arq => {
        let item = document.createElement("li");
        item.textContent = arq;
        lista.appendChild(item);
    });
}
