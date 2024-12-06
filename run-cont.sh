docker run -d \
  --name mrosz-backend-container \
  -p 8000:8000 \
  -p 80:80 \
  -v $(pwd)/backend/app:/code/app \
  -v $(pwd)/frontend:/usr/share/nginx/html \
  mrosz-backend 
