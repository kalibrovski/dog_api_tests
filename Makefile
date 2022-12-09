app_host=""

env:
	rm -f .env; echo PYTHONPATH=`pwd` >> .env
	echo APP_HOST=$(app_host) >> .env