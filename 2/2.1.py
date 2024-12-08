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

def check_report(report):
	is_incr = True
	is_decr = True
	for i in range(len(report) - 1):
		curr_lvl = report[i]
		next_lvl = report[i + 1]
		is_incr = is_incr and (curr_lvl + 1 == next_lvl or curr_lvl + 2 == next_lvl or curr_lvl + 3 == next_lvl)
		is_decr = is_decr and (curr_lvl - 1 == next_lvl or curr_lvl - 2 == next_lvl or curr_lvl - 3 == next_lvl)
	return is_incr or is_decr

if __name__ == "__main__":
	reports = []
	with open("day2.txt", "r") as file:
		data = file.readlines()
		for line in data:
			reports.append(get_numbers(line))
	
	counter = 0
	for report in reports:
		if check_report(report):
			counter += 1
	
	print(counter)
