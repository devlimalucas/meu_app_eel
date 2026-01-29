/**
 * @jest-environment jsdom
 */
import { uploadFile } from "../../web/script.js";

function createFileList(files) {
  return {
    length: files.length,
    item: (index) => files[index],
    ...files
  };
}

describe("uploadFile()", () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <input type="file" id="fileInput">
      <pre id="output"></pre>
    `;
  });

  test("deve alertar se nenhum arquivo for selecionado", async () => {
    const fileInput = document.getElementById("fileInput");
    Object.defineProperty(fileInput, "files", {
      value: createFileList([]),
      writable: false,
    });

    global.alert = jest.fn();

    await uploadFile();

    expect(global.alert).toHaveBeenCalledWith("Selecione um arquivo!");
  });

  test("deve atualizar output com estatísticas mockadas", async () => {
    const fileInput = document.getElementById("fileInput");
    const fakeFile = new File(["conteudo"], "teste.csv", { type: "text/plain" });

    Object.defineProperty(fileInput, "files", {
      value: createFileList([fakeFile]),
      writable: false,
    });

    // Mock de FileReader
    const mockReader = {
      readAsArrayBuffer: jest.fn(function() {
        this.onload({ target: { result: new ArrayBuffer(4) } });
      })
    };
    global.FileReader = jest.fn(() => mockReader);

    // Mock do eel
    global.eel = { save_and_analyze: () => () => Promise.resolve({ linhas: 1, colunas: 2 }) };

    await uploadFile();

    const output = document.getElementById("output").innerText;
    expect(output).toContain('"linhas": 1');
    expect(output).toContain('"colunas": 2');
  });
});
