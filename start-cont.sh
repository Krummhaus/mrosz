docker start mrosz-backend-container && \
until docker inspect -f '{{.State.Running}}' mrosz-backend-container | grep -q "true"; do \
  sleep 1; \
done && \
docker exec -it mrosz-backend-container /bin/bash

