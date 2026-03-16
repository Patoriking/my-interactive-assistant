async function enviar() {

    const nome = document.getElementById("nome").value;

    const resposta = await window.pywebview.api.hello(nome);

    document.getElementById("saida").innerText = resposta;
}