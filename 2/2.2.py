def get_numbers(report_string):
	numbers = []
	number_str = ""
	for i in range(len(report_string) + 1):
		if i == len(report_string) or report_string[i] == " ":
			numbers.append(int(number_str))
			number_str = ""
		else:
			number_str += report_string[i]
	return numbers

def check_report_broken(report):
	bad_incr = 0
	bad_decr = 0
	for i in range(len(report) - 1):
		curr_lvl = report[i]
		next_lvl = report[i + 1]
		if not (curr_lvl + 1 == next_lvl or curr_lvl + 2 == next_lvl or curr_lvl + 3 == next_lvl):
			bad_incr += 1
		if not (curr_lvl - 1 == next_lvl or curr_lvl - 2 == next_lvl or curr_lvl - 3 == next_lvl):
			bad_decr += 1
	return bad_incr <= 1 or bad_decr <= 1

def check_report_broken_2(report):
	is_incr = True
	is_incr_1 = True
	is_decr = True
	is_decr_1 = True
	for i in range(len(report) - 1):
		curr_lvl = report[i]
		next_lvl = report[i + 1]
		is_incr = is_incr and (curr_lvl + 1 == next_lvl or curr_lvl + 2 == next_lvl or curr_lvl + 3 == next_lvl)
		if not is_incr and is_incr_1:
			is_incr = True
			is_incr_1 = False
		is_decr = is_decr and (curr_lvl - 1 == next_lvl or curr_lvl - 2 == next_lvl or curr_lvl - 3 == next_lvl)
		if not is_decr and is_decr_1:
			is_decr = True
			is_decr_1 = False
	return is_incr or is_decr

def check_report(report):
	is_incr = True
	is_decr = True
	for i in range(len(report) - 1):
		curr_lvl = report[i]
		next_lvl = report[i + 1]
		is_incr = is_incr and (curr_lvl + 1 == next_lvl or curr_lvl + 2 == next_lvl or curr_lvl + 3 == next_lvl)
		is_decr = is_decr and (curr_lvl - 1 == next_lvl or curr_lvl - 2 == next_lvl or curr_lvl - 3 == next_lvl)
	return is_incr or is_decr

def check_report_with_delete(report):
	for i in range(len(report)):
		new_report = report.copy()
		new_report.pop(i)
		if check_report(new_report):
			return True

if __name__ == "__main__":
	reports = []
	with open("day2.txt", "r") as file:
		data = file.readlines()
		for line in data:
			reports.append(get_numbers(line))
	
	counter = 0
	for report in reports:
		if check_report(report) or check_report_with_delete(report):
			counter += 1
					
		print(f"{check_report(report)}; {counter}; {report}")
	
	print(counter)
