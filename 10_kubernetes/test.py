import requests

# url = 'http://localhost:9696/predict'
# url = 'http://localhost:8080/predict'
url = 'http://ad65a287e3bd94a0a856e2b40df6e263-922626111.us-east-1.elb.amazonaws.com/predict'
data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)




# ACCOUNT=532819517439
# REGION=us-east-1
# REGISTRY=ml-zoomcamp-images
# PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}

# # TAG=clothing_model-xception-v4-001
# # REMOTE_URI=${PREFIX}:${TAG}

# # docker tag clothing-model_v2:latest $REMOTE_URI
# # docker push $REMOTE_URI

# GATEWAY_LOCAL=zoomcamp-10-gateway:002
# GATEWAY_REMOTE=${PREFIX}:zoomcamp-10-gateway-002
# docker tag $GATEWAY_LOCAL $GATEWAY_REMOTE

# zoomcamp-10-gateway:002

# MODEL_LOCAL=zoomcamp-10-model:xception-v4-001
# MODEL_REMOTE=${PREFIX}:zoomcamp-10-model-xception-v4-001
# docker tag ${MODEL_LOCAL} ${MODEL_REMOTE}


# aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com

# docker push ${GATEWAY_REMOTE}
# docker push ${MODEL_REMOTE}