test:
	python ./grids/npuzzle-gen.py 5 -s > ./grids/g && time python ./src/main.py ./grids/g

test3:
	time python ./src/main.py ./grids/solvable-3.txt

test4:
	time python ./src/main.py ./grids/solvable-4.txt

# checker3:
# 	time python ./src/main.py ./grids/solvable-3.txt | python ./src/checker.py ./grids/solvable-3.txt
#
# checker4:
# 	time python ./src/main.py ./grids/solvable-4.txt | python ./src/checker.py ./grids/solvable-4.txt

.PHONY: test test3 test4 checker3 checker4
