import requests

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth=authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def deleteBook(book_id, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{book_id}", 
        headers={
            "X-API-Key": apiKey
        }
    )
    if r.status_code == 200:
        print(f"Book with ID {book_id} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delete book with ID {book_id}.")

# Get the Auth Token Key
apiKey = getAuthToken()

# Delete the books you've created
for i in range(900, 910):
    # Delete a book by its ID
    deleteBook(i, apiKey)
