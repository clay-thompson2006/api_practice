import requests
import json

# Ask the user for the book title
title = input("Enter the book you'd like to search: ")

# Encode the title for the URL
title_encoded = requests.utils.quote(title, safe='')

# Construct the URL for the Google Books API
url = f"https://www.googleapis.com/books/v1/volumes?q={title_encoded}"

# Send a GET request to the Google Books API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract the volume, title, published date, and description
for item in data["items"]:
   volume = item["id"]
   title = item["volumeInfo"].get("title", "No Title")
   publishedDate = item["volumeInfo"].get("publishedDate", "No Date")
   description = item["volumeInfo"].get("description", "No Description")

   # Print the results
   print(f"Volume: {volume}")
   print(f"Title: {title}")
   print(f"Published Date: {publishedDate}")
   print(f"Description: {description}\n")

   # Output the results to a .txt file
   with open('output.txt', 'a') as f:
       f.write(f"Volume: {volume}\n")
       f.write(f"Title: {title}\n")
       f.write(f"Published Date: {publishedDate}\n")
       f.write(f"Description: {description}\n\n")