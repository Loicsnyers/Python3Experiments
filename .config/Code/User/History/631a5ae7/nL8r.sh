APIKEY="cisco|BjINCjDNG5SKDF50FaIaZpkxqFJChvTlF2XhKWAR3Cw"
for BOOK in {900..910}
do
    echo $BOOK
    DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
    echo $DELETE_URL
    curl -X DELETE $DELETE_URL -H "accept: application/json" \
    -H "X-API-KEY: $APIKEY" -H "Content-Type: application/json"
done
