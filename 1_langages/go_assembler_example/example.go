package main

import "fmt"

// normalise modifies the slice in-place by subtracting the mean from every element.
// data: pointer to the first element
// n:    number of elements
//
//go:noescape
func normalise(data *float64, n int)

func main() {
	// Example usage
	values := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
	fmt.Printf("Before: %v\n", values)

	if len(values) > 0 {
		normalise(&values[0], len(values))
	}

	fmt.Printf("After:  %v\n", values)
}
