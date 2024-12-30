FROM tensorflow/serving:2.7.0

COPY clothing-model /models/clothing-model/1
ENV MODEL_NAME="clothing-model"

# docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .

# docker run -it --rm \
#     -p 8500:8500 \
#     zoomcamp-10-model:xception-v4-001