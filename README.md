# hesychasm

https://hesychasm.herokuapp.com

IPFS Flask API as serverless infrastructure 

### docker build
```
docker build -t ipfs-sls:latest .
docker run -d -p 5000:5000 ipfs-sls

curl --header "Content-Type: application/json" --request POST --data '{"data": {"title":"title","description":"description"}}' https://hesychasm.herokuapp.com/post_json
{"hash":"QmP4Azn85QGrBXxzVkNAfFPS2a7hkE4uTdWxBE4TDErs1F"}

curl --header "Content-Type: application/json" --request POST --data '{"cid":"QmP4Azn85QGrBXxzVkNAfFPS2a7hkE4uTdWxBE4TDErs1F"}' https://hesychasm.herokuapp.com/read_cid
{"data":{"title":"title","description":"description"}}

curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@umwelt.png" https://hesychasm.herokuapp.com/post_file
{"hash":"QmT9SX2YFqitWQPxPzA1gEZxgJqBRZP1Zc5ZyStaBfY3UW"}
```

```MIT License```
