test:
	python3 ./grids/npuzzle-gen.py 4 -s > ./grids/g && time python3 ./src/main.py ./grids/g

testu:
	python3 ./grids/npuzzle-gen.py 4 -u > ./grids/g && time python3 ./src/main.py ./grids/g

test3:
	time python3 ./src/main.py ./grids/solvable-3.txt

test4:
	time python3 ./src/main.py ./grids/solvable-4.txt

# checker3:
# 	time python ./src/main.py ./grids/solvable-3.txt | python ./src/checker.py ./grids/solvable-3.txt
#
# checker4:
# 	time python ./src/main.py ./grids/solvable-4.txt | python ./src/checker.py ./grids/solvable-4.txt

.PHONY: test test3 test4 checker3 checker4
