FROM public.ecr.aws/lambda/python:3.11

RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl
RUN pip install "numpy<2"

# COPY xception_v4_30_0.891.tflite .
COPY xception_v4_numpy_v2_28_0.894.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]


# docker build -t clothing-model .
# docker run -it --rm -p 8080:8080 clothing-model:latest 