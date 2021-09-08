COURSE = cse107
GROUP_NUMBER = 13
ASSIGNMENT = prelab3
TARGETS = gpa.py square.py
zip: $(TARGETS)
	zip $(COURSE)_group$(GROUP_NUMBER)_$(ASSIGNMENT).zip $(TARGETS)