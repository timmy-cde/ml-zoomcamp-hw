FROM continuumio/anaconda3

WORKDIR /ml-zoomcamp

EXPOSE 8888

COPY . .

RUN conda create -n ml-zoomcamp python=3.11 

SHELL ["conda", "run", "-n", "ml-zoomcamp", "&&", \
       "conda", "install", "numpy", "pandas", "scikit-learn", "seaborn", "jupyter", "/bin/bash", "-c"]

ENTRYPOINT [ "jupyter", "lab", "--no-browser", "--allow-root"]