import requests


#Cria função para adquirir dados de latitude e longitude com base na cidade, estado e pais
def get_city_coordinates():
    API_KEY = "SUA API KEY" #Chave da API disponibilizada no site
    BASE_URL = "http://api.openweathermap.org/geo/1.0/direct" #url da API

    #Recebe dados do usuário
    city_name = input("Digite o nome da cidade: ").strip()
    state_code = input("Digite o código do estado (UF): ").strip()
    country_code = input("Digite o código do pais (UF) ").strip()

    #Formata os dados para a API
    query_params = {
        "q": f"{city_name}, {state_code}, {country_code}"
        if state_code or country_code else city_name,

        "limit": 1,
        "appid": API_KEY
    }
    #Envia uma requisição HTTP para a API com base no formato montado anteriormente
    response = requests.get(BASE_URL, params=query_params)

    #Verifica se a requisição foi bem-sucedida e trata corretamente
    if response.status_code == 200:
        data = response.json()
        if data:
            
            location = data[0]
            print(f"Cidade: {location.get('name')}")
            print(f"País: {location.get('country')}")
            print(f"Coordenadas: Lat {location.get('lat')}, Lon {location.get('lon')}")
            lat = float(location.get('lat'))
            lon = float(location.get('lon'))
            return lat, lon #retorna latitude e longite
        else:
            print("Nenhum local encontrado. Verifique os dados e tente novamente.")
            return None, None
    else:
        print(f"Erro na requisição: {response.status_code} - {response.text}")
        return None, None


#Cria função para buscar dados do clima com base na latitude e longitude
def get_weather(lat, lon):
    API_KEY = "SUA API KEY" #chave da API
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br" #URL da API

    #Envia uma requisição HTTP para a API com base no URL montado anteriormente
    response = requests.get(url)
    response.raise_for_status()

    #Verifica se a requisição foi bem-sucedida e trata corretamente
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao buscar clima: {response.status_code}")
        return None

#Recebe a requisição em json e formata para as informações do usuario   
if __name__ == "__main__":
    lat, lon = get_city_coordinates()
    if lat is not None and lon is not None:
        weather_data = get_weather(lat, lon)

        if weather_data:
            print("\nClima atual:")
            print(f"Cidade: {weather_data.get('name', 'N/A')}")
            print(f"Temperatura: {weather_data['main']['temp']}°C")
            print(f"Condição: {weather_data['weather'][0]['description'].capitalize()}")
            print(f"Umidade: {weather_data['main']['humidity']}%")
