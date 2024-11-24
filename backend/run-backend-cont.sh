docker run -it \
  --name mrosz-backend-container \
  -p 8000:8000 \
  -v $(pwd)/app:/code/app \
  mrosz-backend \
  bash
