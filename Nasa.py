import os
import requests
import shutil


def download_image(url):
   response = requests.get(url, stream=True)
   file_name = url.split("/")[-1]
   file_path = f"./images/{file_name}"
   
   # Create the image directory if it doesn't exist
   if not os.path.exists("./images"):
       os.makedirs("./images")
       
   with open(file_path, 'wb') as out_file:
       shutil.copyfileobj(response.raw, out_file)
   del response

def main():
   # Replace 'curiosity' with the name of any other rover
   base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
   
   # Set parameters for the request
   params = {
       "api_key": "<3XxzjlVUmgFbTyFaAFGypj65R3VlQ2xXomicnvMp>",
       "page": 1,
       "per_page": 3
   }
   
   response = requests.get(base_url, params=params)
   data = response.json()
   
   # Get URLs of the three images
   urls = [photo['img_src'] for photo in data['images']]
   
   # Download each image
   for url in urls:
       download_image(url)

if __name__ == "__main__":
   main()