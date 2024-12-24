FROM public.ecr.aws/lambda/python:3.11

RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl
RUN pip install "numpy<2"

# COPY xception_v4_30_0.891.tflite .
COPY xception_v4_numpy_v2_28_0.894.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]

# Build and run docker image
# docker build -t clothing-model .
# docker run -it --rm -p 8080:8080 clothing-model:latest 

# Create ecr repository
# aws ecr create-repository --repository-name <NAME>

# Login to ecr with docker and push image to ecr
# aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ACCOUNT>.dkr.ecr.<REGION>.amazonaws.com

# ACCOUNT=*************
# REGION=us-east-1
# REGISTRY=clothing-tflite-images
# PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}

# TAG=clothing_model-xception-v4-001
# REMOTE_URI=${PREFIX}:${TAG}

# docker tag clothing-model_v2:latest $REMOTE_URI
# docker push $REMOTE_URI