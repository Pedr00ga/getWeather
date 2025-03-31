import requests

def get_city_coordinates():
    API_KEY = "d835383cb049dcaa78831547190832f0"
    BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

    city_name = input("Digite o nome da cidade: ").strip()
    state_code = input("Digite o código do estado (UF, opcional): ").strip()
    country_code = input("Digite o código do país (ex: BR, opcional): ").strip()

    query_params = {
        "q": f"{city_name},{state_code},{country_code}" if state_code or country_code else city_name,
        "limit": 1,
        "appid": API_KEY
    }

    print(f"\nDEBUG: Parâmetros da query: {query_params}")  # Debug 1

    try:
        response = requests.get(BASE_URL, params=query_params)
        print(f"DEBUG: Status Code: {response.status_code}")  # Debug 2
        print(f"DEBUG: Resposta bruta: {response.text[:200]}...")  # Debug 3
        
        response.raise_for_status()
        data = response.json()
        
        if not data:
            print("Nenhum local encontrado. Verifique os dados.")
            return None, None
            
        location = data[0]
        print(f"\nDEBUG: Dados da localização: {location}")  # Debug 4
        return float(location.get('lat')), float(location.get('lon'))
        
    except Exception as e:
        print(f"Erro ao obter coordenadas: {str(e)}")
        return None, None

def get_weather(lat, lon):
    API_KEY = "d835383cb049dcaa78831547190832f0"
    if lat is None or lon is None:
        print("Coordenadas inválidas.")
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br"
    print(f"\nDEBUG: URL completa: {url}")  # Debug 5

    try:
        response = requests.get(url)
        print(f"DEBUG: Status Code: {response.status_code}")  # Debug 6
        print(f"DEBUG: Resposta bruta: {response.text[:200]}...")  # Debug 7
        
        response.raise_for_status()
        data = response.json()
        print(f"DEBUG: Dados do clima: {data}")  # Debug 8
        return data
            
    except Exception as e:
        print(f"Erro ao obter clima: {str(e)}")
        return None

if __name__ == "__main__":
    print("=== Consulta Climática (Modo Debug) ===")
    lat, lon = get_city_coordinates()
    
    if lat is not None and lon is not None:
        print(f"\nDEBUG: Coordenadas recebidas: lat={lat}, lon={lon}")  # Debug 9
        weather_data = get_weather(lat, lon)
        
        if weather_data:
            print("\nDados Climáticos:")
            print(f"Cidade: {weather_data.get('name', 'N/A')}")
            print(f"Temperatura: {weather_data['main']['temp']}°C")
            print(f"Condição: {weather_data['weather'][0]['description'].capitalize()}")
            print(f"Umidade: {weather_data['main']['humidity']}%")
        else:
            print("\nAVISO: A função get_weather() retornou None")
    else:
        print("\nAVISO: Coordenadas inválidas recebidas")

    input("\nPressione Enter para sair...")