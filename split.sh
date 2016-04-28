#curl https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyBvMF4EHOR0i03n-a$
#echo $1 >> out.txt
var=$(grep -o '"id": "http[^"]*' out.txt > temp.txt)
#echo $var
data=$(grep -o 'http[^"]*' temp.txt > temp2.txt)
final_data=$(grep -o 'goo.gl[^"]*' temp2.txt)
echo $final_data
rm out.txt
rm temp.txt
