package main
	
import (
    "fmt"
    "os"
		"strings"
)

func main() {

	// Read in file
	dat, err := os.ReadFile("/Users/cmiao/Projects/adventofcode/2023/day01/input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")

	// todo
	fmt.Println(lines)

}
