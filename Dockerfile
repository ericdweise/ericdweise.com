FROM httpd:2.4

COPY ./site/ /usr/local/apache2/htdocs/
COPY apache/httpd.conf /usr/local/apache2/conf/httpd.conf
