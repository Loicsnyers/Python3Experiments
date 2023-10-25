APIKEY = "cisco|BjINCjDNG5SKDF50FaIaZpkxqFJChvTlF2XhKWAR3Cw"
BOOK = 901
DELETE_URL = "http://library.demo.local/api/v1/books/$BOOK"
echo $DELETE_URL
curl -X DELETE $DELETE_URL -H "accept: application/json" \
-H "X-API-KEY: $APIKEY" -H "content-Type: application/json"