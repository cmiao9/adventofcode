package main
	
import (
    "fmt"
    "os"
		"strings"
)

func check(grid[]rune) {
	grid[0:3]
}

func main() {

	// Read in file
	dat, err := os.ReadFile("/Users/cmiao/Projects/adventofcode/2023/day03/test.txt")
	if err != nil {
		panic(err)
	}
	fmt.Print(string(dat))

	// Split into lines
	lines := strings.Split(string(dat), "\n")

	// Build 2d array
	var grid[]string
	for i, line := range lines {
		for j, char := range line {
			// Check if char is a symbol
			if char != '.' && !(char >= '0' && char <= '9') {
				// do something
			}

			if char >= '0' && char <= '9' {
				// do something
			}
		}
	}

}
