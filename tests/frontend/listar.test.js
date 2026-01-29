/**
 * @jest-environment jsdom
 */
import { listar } from "../../web/script.js";

describe("listar()", () => {
  beforeEach(() => {
    document.body.innerHTML = `<ul id="lista"></ul>`;
  });

  test("deve atualizar a lista de arquivos", async () => {
    global.eel = { list_files_exposed: () => () => Promise.resolve(["a.txt", "b.csv"]) };

    await listar();

    const lista = document.querySelectorAll("#lista li");
    expect(lista.length).toBe(2);
    expect(lista[0].textContent).toBe("a.txt");
  });

  test("deve deixar a lista vazia se não houver arquivos", async () => {
    global.eel = { list_files_exposed: () => () => Promise.resolve([]) };

    await listar();

    const lista = document.querySelectorAll("#lista li");
    expect(lista.length).toBe(0);
  });
});
