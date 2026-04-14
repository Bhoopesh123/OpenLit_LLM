# OpenLit_LLM

export GEMINI_API_KEY=xxxx
docker build -t gemini-chat-app:latest .

docker run -p 8080:8080 \
  -e GEMINI_API_KEY=xxxx \
  gemini-chat-app:latest

docker build -t gemini-assistant-2026 .
docker run -it \
  --name gemini-chat-container \
  -e GEMINI_API_KEY="xxx" \
  -p 8080:8080 \
  gemini-assistant-2026

docker login
docker tag gemini-assistant-2026 bhoopeshsharma/gemini-assistant-2026:latest
docker push bhoopeshsharma/gemini-assistant-2026:latest

docker build -t openrouter-chat .
docker tag openrouter-chat bhoopeshsharma/openrouter-chat:latest
docker push bhoopeshsharma/openrouter-chat:latest

k3d image import bhoopeshsharma/gemini-assistant-2026:latest -c bhoopesh
k3d image import bhoopeshsharma/openrouter-chat:latest -c bhoopesh
k port-forward svc/gemini-chat-service 8080:80

curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello from k3d"}'

####### Operator
https://grafana.com/blog/ai-observability-zero-code/?camp=blog&mdm=social&src=li


helm repo add openlit https://openlit.github.io/helm/
helm repo update

# 6. Validate the metrics on Grafana
To Search all of the time series data points grouping by job  in query  

    count({__name__=~".+"}) by (job)