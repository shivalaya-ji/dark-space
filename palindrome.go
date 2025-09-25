package main

import (
	"fmt"
	"strings"
)

func isPalindrome(s string) bool {
	// Convert to lowercase and remove spaces
	s = strings.ToLower(strings.ReplaceAll(s, " ", ""))

	// Compare characters from start and end
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	// Test cases
	testStrings := []string{
		"A man a plan a canal Panama",
		"race a car",
		"Was it a car or a cat I saw",
	}

	for _, str := range testStrings {
		fmt.Printf("%q is palindrome: %v\n", str, isPalindrome(str))
	}
}
