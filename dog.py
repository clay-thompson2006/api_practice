import requests
# Makes a request to the Dog API
response = requests.get('https://dog.ceo/api/breeds/image/random')

# Prints the response status
print("Response Status: ", response.status_code)

# Prints the response text
print("Response Text: ", response.text)

# Prints the response headers
print("Response Headers: ", response.headers)

# Prints the request headers
print("Request Headers: ", response.request.headers)
#dog api_key = live_rQcz7IyyEB0gpWN1ZYBrnMvzleO49N3hUdZ47nkhLTdwiZ6Y9sdMYyBNN5vPUKKW
