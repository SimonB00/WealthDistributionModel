all:
	clang-format -i ./src/*.cc
	clear
	./src/compile.sh
	./src/compileNew.sh
cpp:
	clang-format -i ./src/*.cc
	clear
root:
	source ../root/bin/thisroot.sh
test:
	clear
	python3 ./main.py
