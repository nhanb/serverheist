package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"sort"
)

func main() {
	jsonInput, _ := ioutil.ReadFile("passwords.json")
	var passwords []string
	json.Unmarshal(jsonInput, &passwords)

	for _, password := range passwords {
		if isCorrectPassword(password) {
			fmt.Println("Found it:", password)
			//return
		}
	}
	//fmt.Println("No password found.")
}

func isCorrectPassword(pw string) bool {
	var digits []int
	var letters []rune
	hasVowel := false
	digitsSum := 0

	for _, r := range pw {
		if isDigit(r) {
			digit := int(r - '0')
			digits = append(digits, digit)
			digitsSum += digit
		} else if isLetter(r) {
			letters = append(letters, r)
			if isVowel(r) {
				hasVowel = true
			}
		}
	}

	// Condition #1
	if len(letters) != 3 || len(digits) != 4 {
		return false
	}

	// #2
	if !areFiveCharsApart(letters) {
		return false
	}

	// #3
	isSumEven := (digitsSum%2 == 0)
	if !(isSumEven == hasVowel) {
		return false
	}

	return true
}

func isVowel(r rune) bool {
	// mild yikes
	return r == 'A' || r == 'E' || r == 'I' || r == 'O' || r == 'U'
}

func isDigit(r rune) bool {
	return '0' <= r && r <= '9'
}

func isLetter(r rune) bool {
	return 'A' <= r && r <= 'Z'
}

func distance(r1 rune, r2 rune) int {
	diff := int(r2 - r1)
	if diff < 0 {
		diff += 26
	}
	return diff
}

func areFiveCharsApart(runes []rune) bool {
	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
	count := 0
	if distance(runes[0], runes[1]) == 6 {
		count++
	}
	if distance(runes[1], runes[2]) == 6 {
		count++
	}
	if distance(runes[2], runes[0]) == 6 {
		count++
	}
	return count == 2
}
