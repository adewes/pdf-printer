UID = $$(id -u)
FLAGS = QTWEBENGINE_CHROMIUM_FLAGS="--disable-logging --no-sandbox --disable-gpu --single-process"
PYCMD = python printer.py example/media example/templates index.html \
				example/context.json example/output/index.pdf
docker-image:
	docker build . --tag pdf-printer:latest

docker-example:
	docker run -v `readlink -e example/templates`:/templates \
			   -v `readlink -e example/context.json`:/context.json \
			   -v `readlink -e example/output`:/output \
			   -v `readlink -e example/media`:/media \
			   --env TARGET_UID=$(UID) \
               pdf-printer:latest

python-example:
	@$(FLAGS) $(PYCMD)
	@echo "Output saved to example/output/index.pdf"

python-example-xvfb:
	@$(FLAGS) xvfb-run $(PYCMD)
	@echo "Output saved to example/output/index.pdf"
