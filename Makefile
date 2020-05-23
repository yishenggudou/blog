.SILENT:
.PHONY: all clean current doc doc-srv serve tox


all:
	echo ""
	echo "  deploy-product			deploy all files"
	echo "  build-static			build all static"


build:
	echo "will build... "
	git pull
	./build.doc.sh
	cp -vf blog.conf /etc/nginx/conf.d/
	service nginx reload