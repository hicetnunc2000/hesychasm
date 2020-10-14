# hesychasm

https://hesychasm.herokuapp.com/

infrastructural protocol for making storage deals with filecoin. it's intended to implement a set of microsservices and decentralized oracles for such.

the present repository contains a microsservice which composes it's stack.

powergate service:
https://github.com/hicetnunc2000/powergate-external-adapter

```
docker build -t ipfs-micro:latest .
docker run -d -p 3000:3000 ipfs-micro

heroku container:login
heroku create ipfs-micro
heroku container:push web --app ipfs-micro
heroku container:release web --app ipfs-micro

curl --header "Content-Type: application/json" --request POST --data '{"data": {"title":"title","description":"description"}}' https://hesychasm.herokuapp.com.herokuapp.com/post_json
{"hash":"QmP4Azn85QGrBXxzVkNAfFPS2a7hkE4uTdWxBE4TDErs1F"}

curl --header "Content-Type: application/json" --request POST --data '{"hash":"QmP4Azn85QGrBXxzVkNAfFPS2a7hkE4uTdWxBE4TDErs1F"}' https://hesychasm.herokuapp.com.herokuapp.com/get_json
{"data":{"title":"title","description":"description"}}

curl --header "Content-Type: application/json" --request POST --data '{"list": ["QmP4Azn85QGrBXxzVkNAfFPS2a7hkE4uTdWxBE4TDErs1F", "QmesAfkmnyofDHSudrAYBtYeBTdBkV1Ffi6fpvmaCXdnRV"]}' https://hesychasm.herokuapp.com.herokuapp.com/get_list
{"jsons":[{"data":{"title":"title","description":"description"}},{"data":{"title":"title2","description":"description2"}}]}

curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@umwelt.png" https://hesychasm.herokuapp.com/post_file
{"hash":"QmT9SX2YFqitWQPxPzA1gEZxgJqBRZP1Zc5ZyStaBfY3UW"}
```
