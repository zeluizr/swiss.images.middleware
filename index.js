const express = require("express");
const path = require("path");
const app = express();

// Porta em que o servidor estará escutando
const PORT = process.env.PORT || 3000;

// Middleware para servir arquivos estáticos
app.use("/images", express.static(path.join(__dirname, "images")));

// Rota principal que lista as imagens disponíveis (opcional)
app.get("/", (_, res) => {
  const fs = require("fs");
  const imagesFolder = path.join(__dirname, "images");

  fs.readdir(imagesFolder, (err, files) => {
    if (err) {
      return res.status(500).send("Erro ao ler o diretório de imagens");
    }

    res.send(
      files
        .map(
          (file) => `<img src="/images/${file}" style="max-width: 100px;"><br>`
        )
        .join("")
    );
  });
});

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
