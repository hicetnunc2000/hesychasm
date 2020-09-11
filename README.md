docker build -t ipfs-micro:latest .
docker run -d -p 3000:3000 ipfs-micro

heroku container:login
heroku create ipfs-micro
heroku container:push web --app ipfs-micro
heroku container:release web --app ipfs-micro

http://ipfs-micro.herokuapp.com/