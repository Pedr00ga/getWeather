# 🌤️ Buscador de Clima com OpenWeatherMap

Este é um script Python simples que permite ao usuário buscar informações de **latitude e longitude** de uma cidade, e em seguida consultar o **clima atual** desse local, utilizando a API do [OpenWeatherMap](https://openweathermap.org/api).

## 📋 Funcionalidades

* Solicita ao usuário o nome da cidade, estado (UF) e país.
* Busca as coordenadas geográficas (latitude e longitude) da cidade informada.
* Recupera e exibe as informações de clima atual com base nas coordenadas.

## 🚀 Como usar

### 1. Clone o repositório ou copie o script

```bash
git clone https://github.com/seuusuario/clima-openweathermap.git
```

Ou crie um arquivo `.py` com o código.

### 2. Instale as dependências

Este projeto utiliza a biblioteca `requests`. Para instalá-la:

```bash
pip install requests
```

### 3. Obtenha sua API Key

Cadastre-se em [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) e obtenha uma **API Key gratuita**.

### 4. Edite o código

Substitua `"SUA API KEY"` pela sua chave real em duas partes do código:

```python
API_KEY = "SUA API KEY"
```

### 5. Execute o script

```bash
python nome_do_arquivo.py
```

Você será solicitado a inserir:

* Nome da cidade
* Código do estado (opcional)
* Código do país (ex: `BR`, `US`, `PT`)

## 🧪 Exemplo de uso

```
Digite o nome da cidade: São Paulo
Digite o código do estado (UF): SP
Digite o código do pais (UF): BR

Cidade: São Paulo
País: BR
Coordenadas: Lat -23.5505, Lon -46.6333

Clima atual:
Cidade: São Paulo
Temperatura: 22.3°C
Condição: Céu limpo
Umidade: 64%
```

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca `requests`
* API OpenWeatherMap (Geocoding + Current Weather)

## ⚠️ Observações

* A chave da API tem limites de requisição na versão gratuita.
* O código trata erros comuns, como cidade não encontrada ou falha de conexão.
* O script usa unidades métricas e idioma português brasileiro nos dados do clima.

## 📄 Licença

Este projeto é livre para uso pessoal e educacional. Você pode adaptá-lo conforme suas necessidades.

---
