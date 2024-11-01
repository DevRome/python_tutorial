# esercizio su come fare il parse di un URL (preso dalle slide del prof di Cyber Security)
import urllib.parse 
url_base = "https://www.example.com/search" 
params = {'query': "Hello, World! This is a test: & should be encoded, as well as % and $."} 
url_encoded = url_base + "?" + urllib.parse.urlencode(params) 
print(url_encoded)

