FROM python:3.7
RUN pip install Flask==2.0.0 uWSGI==2.0.18 Jinja2==3.0.1 MarkupSafe==2.1.1 requests==2.5.1 
WORKDIR /app
COPY app /app
COPY cmd.sh /
CMD ["/cmd.sh"]






