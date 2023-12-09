// Função assíncrona principal que é chamada quando o formulário é submetido
const start = async () => {
  // Obter os valores dos campos de entrada do formulário
  let inputType = document.getElementById("newType").value;
  let inputFixedAcidity = document.getElementById("newFixedAcidity").value;
  let inputVolatileAcidity = document.getElementById("newVolatileAcidity").value;
  let inputCitricAcid = document.getElementById("newCitricAcid").value;
  let inputResidualSugar = document.getElementById("newResidualSugar").value;
  let inputChlorides = document.getElementById("newChlorides").value;
  let inputFreeSulfurDioxide = document.getElementById("newFreeSulfurDioxide").value;
  let inputTotalSulfurDioxide = document.getElementById("newTotalSulfurDioxide").value;
  let inputDensity = document.getElementById("newDensity").value;
  let inputpH = document.getElementById("newpH").value;
  let inputSulphates = document.getElementById("newSulphates").value;
  let inputAlcohol = document.getElementById("newAlcohol").value;

  // Verifique se o tipo e o valor do álcool são válidos antes de adicionar
  if (!["white", "red"].includes(inputType)) {
    alert("O tipo de vinho deve ser 'white' ou 'red'.");
  } else if (isNaN(inputAlcohol)) {
    alert("O campo de álcool deve ser um número.");
  } else {
    try {
      // Chamar a função postItem para enviar os dados para o servidor
      const inputQuality = await postItem(
        inputType,
        inputFixedAcidity,
        inputVolatileAcidity,
        inputCitricAcid,
        inputResidualSugar,
        inputChlorides,
        inputFreeSulfurDioxide,
        inputTotalSulfurDioxide,
        inputDensity,
        inputpH,
        inputSulphates,
        inputAlcohol
      );
      // Atualizar o elemento HTML com a qualidade prevista retornada pelo servidor
      document.getElementById("qualityPrediction").innerText = `${inputQuality}`;
    } catch (error) {
      console.error("Ocorreu um erro:", error);
    }
  }
};

// Função assíncrona que faz uma solicitação POST para o servidor com os dados do vinho
const postItem = async (
  inputType,
  inputFixedAcidity,
  inputVolatileAcidity,
  inputCitricAcid,
  inputResidualSugar,
  inputChlorides,
  inputFreeSulfurDioxide,
  inputTotalSulfurDioxide,
  inputDensity,
  inputpH,
  inputSulphates,
  inputAlcohol
) => {
  // Criar um objeto FormData para enviar os dados como formulário
  const formData = new FormData();
  formData.append("type", inputType);
  formData.append("fixed_acidity", inputFixedAcidity);
  formData.append("volatile_acidity", inputVolatileAcidity);
  formData.append("citric_acid", inputCitricAcid);
  formData.append("residual_sugar", inputResidualSugar);
  formData.append("chlorides", inputChlorides);
  formData.append("free_sulfur_dioxide", inputFreeSulfurDioxide);
  formData.append("total_sulfur_dioxide", inputTotalSulfurDioxide);
  formData.append("density", inputDensity);
  formData.append("pH", inputpH);
  formData.append("sulphates", inputSulphates);
  formData.append("alcohol", inputAlcohol);

  // URL do servidor para enviar a solicitação POST
  let url = "http://127.0.0.1:5000/vinho";

  try {
    // Enviar a solicitação POST usando a função fetch
    const response = await fetch(url, {
      method: "post",
      body: formData,
    });

    // Verificar se a resposta da solicitação é bem-sucedida
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Converter a resposta para JSON
    const data = await response.json();

    // A qualidade (quality) pode ser acessada assim:
    const quality = data.quality;

    // Retornar a qualidade para ser usada na função start
    return quality; 
  } catch (error) {
    // Lidar com erros e registrar no console
    console.error("Error:", error);
    throw error; // Rejeita a promise em caso de erro
  }
};
