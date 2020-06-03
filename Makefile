.SILENT:
.PHONY: all clean current doc doc-srv serve tox


all:
	echo ""
	echo "  deploy-product			deploy all files"
	echo "  build-static			build all static"

doc:
	echo "will build... "
	git pull
	./build.doc.sh

build:
	echo "will build... "
	git pull
	./build.doc.sh
	cp -vf *.conf /etc/nginx/conf.d/
	service nginx reload

release:
	ssh root@106.53.70.37 'cd /root/apps/blog && make build'