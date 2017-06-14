FROM heroku/heroku:16-build

WORKDIR /app
COPY runtime.txt .

# Uses the Heroku Python buildpack's binaries for parity with production.
RUN PYTHON_VERSION="$(cat runtime.txt)" \
  && curl -sSf "https://lang-python.s3.amazonaws.com/heroku-16/runtimes/$PYTHON_VERSION.tar.gz" | tar -xz -C /usr/local \
  # Work around https://github.com/heroku/heroku-buildpack-python/issues/379
  && rm -rf "/usr/local/lib/python2.7/site-packages/"*

RUN curl -sSf https://bootstrap.pypa.io/get-pip.py | python - --no-cache-dir "pip==9.0.1"

COPY requirements/common.txt requirements/dev.txt requirements/
RUN pip install --no-cache-dir -r requirements/common.txt -r requirements/dev.txt
