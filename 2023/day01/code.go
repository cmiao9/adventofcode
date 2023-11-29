package main
	
import (
    "fmt"
    "os"
		"strings"
		"strconv"
)

func main() {

	// Read in file
	dat, err := os.ReadFile("/Users/cmiao/Projects/adventofcode/2023/day01/input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")

	// Replace spelled out numbers with digits - PART 2
	formatted_lines := []string{}
	for _, line := range lines {
			line = line + " "
			for i, _ := range line {
				line = strings.Replace(line[0:i], "one", "o1e", 1) + line[i:]
				line = strings.Replace(line[0:i], "two", "t2o", 1) + line[i:]
				line = strings.Replace(line[0:i], "three",  "t3  e", 1) + line[i:]
				line = strings.Replace(line[0:i], "four", "4   ", 1) + line[i:]
				line = strings.Replace(line[0:i], "five", "5  e", 1) + line[i:]
				line = strings.Replace(line[0:i], "six", "6  ", 1) + line[i:]
				line = strings.Replace(line[0:i], "seven", "7   n", 1) + line[i:]
				line = strings.Replace(line[0:i], "eight", "e8  t", 1) + line[i:]
				line = strings.Replace(line[0:i], "nine", "n9 e", 1) + line[i:]
			}
			line = strings.Replace(line, " ", "", -1)
		formatted_lines = append(formatted_lines, line)
	}

	// Loop over lines
	total := 0
	for _, line := range formatted_lines {
		first := ""
		last := ""

		// Get calibration value
		for _, char := range line {
			if char >= '0' && char <= '9' {
				last = string(char)
				if first == "" {
					first = string(char)
				}
			}
		}
		calibration_value, _ := strconv.Atoi(first+last)
		total += calibration_value
		fmt.Println(line, calibration_value)
	}
	fmt.Println(total)

}
