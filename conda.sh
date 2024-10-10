docker run -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash -c "\
    conda install numpy pandas scikit-learn seaborn jupyter -y --quiet && \
    mkdir -p /opt/notebooks && \
    jupyter notebook \
    --notebook-dir=/opt/notebooks --ip='*' --port=8888 \
    --allow-root"
