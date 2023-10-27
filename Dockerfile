# 使用 Python 3.10 镜像作为基础镜像
FROM python:3.8.18-slim-bullseye 

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && apt-get update --fix-missing && apt-get install -y --fix-missing \
    build-essential \
    vim \
    git \
    && rm -rf /var/lib/apt/lists/*
    # todo install sqlite

# 设置工作目录
WORKDIR /app

COPY ./src/requirements.txt /app

# RUN pip install --no-cache-dir -r requirements.txt
# If you want to use Tencent Cloud mirroring, use the following command
RUN pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple \
    && rm -rf $(pip cache dir)/* 

# Copy all files in the current directory to /app
COPY . /app

# 运行脚本
# CMD ["bash", "-c", "memoflow/cmd/run.sh"]
CMD ["tail", "-f", "/dev/null"]

