import { useState } from "react";
import reactLogo from "./assets/react.svg";
import { invoke } from "@tauri-apps/api/core";
import "./App.css";

function App() {

  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState("");

  async function buscarCNPJ() {
      try {
          const resp = await invoke("buscar_cnpj", { cnpj: name});
          setResultado(JSON.parse(resp));
          setErro("");
      } catch(e) {
          setErro("Erro: " + e);
          setResultado(null);
      }
  }

  return (
    <main className="container">
      <div>

      </div>

      <form
        className="row"
        onSubmit={(e) => {
          e.preventDefault();
          buscarCNPJ();
        }}
      >
        <input
          id="pesquisar-input"
          onChange={(e) => setName(e.currentTarget.value)}
          placeholder="Digite um cnpj:"
        />
        <button type="submit">Pesquisar</button>
      </form>
      <p>{greetMsg}</p>
      {erro && <p style={{color: "red"}}>❌ {erro}</p>}
      {resultado && <div style={{marginTop: "20px", padding: "10px", border: "1px solid green", borderRadius: "4px"}}><h3>✅ CNPJ: {resultado.cnpj}</h3><p>Status: {resultado.status}</p></div>}
    </main>
  );
}

export default App;
