# ES6 Data Manipulation

This project contains exercises for practicing ES6 data manipulation using modern JavaScript array methods, typed arrays, Sets, Maps, and WeakMaps.

## Project Structure

### Tasks

#### Task 0: Get list of students
**File:** `0-get_list_students.js`
- Returns an array of student objects with id, firstName, and location

#### Task 1: Get list of student IDs
**File:** `1-get_list_student_ids.js`
- Uses `map()` to extract student IDs from an array of student objects
- Returns empty array if argument is not an array

#### Task 2: Get students by location
**File:** `2-get_students_by_loc.js`
- Uses `filter()` to return students located in a specific city

#### Task 3: Get sum of student IDs
**File:** `3-get_ids_sum.js`
- Uses `reduce()` to calculate the sum of all student IDs

#### Task 4: Update student grades by city
**File:** `4-update_grade_by_city.js`
- Combines `filter()` and `map()` to update grades for students in a specific city
- Returns grade as 'N/A' if no grade is found

#### Task 5: Typed Arrays
**File:** `5-typed_arrays.js`
- Creates an Int8 typed array using ArrayBuffer and DataView
- Throws error if position is outside range

#### Task 6: Set from array
**File:** `6-set.js`
- Creates a Set from an array to get unique values

#### Task 7: Check array values in set
**File:** `7-has_array_values.js`
- Uses `every()` to check if all array elements exist in a Set

#### Task 8: Clean set
**File:** `8-clean_set.js`
- Returns a string of Set values that start with a specific string
- Removes the prefix and joins with dash separator

#### Task 9: Groceries list (Map)
**File:** `9-groceries_list.js`
- Creates a Map with grocery items and quantities

#### Task 10: Update unique items
**File:** `10-update_uniq_items.js`
- Updates Map values from 1 to 100
- Throws error if argument is not a Map

#### Task 100: Weak map (Advanced)
**File:** `100-weak.js`
- Uses WeakMap to track API endpoint query counts
- Throws error when endpoint is queried 5 or more times

## Testing

Run individual test files using babel-node:

```bash
npm run dev 0-main.js
npm run dev 1-main.js
# etc...
```

Or directly:

```bash
npx babel-node ES6_data_manipulation/0-main.js
```

## Requirements

- Node.js
- Babel (for ES6 transpilation)
- ESLint (for code linting)

## Key Concepts Covered

- Array methods: `map()`, `filter()`, `reduce()`, `every()`, `find()`
- Typed Arrays and DataView
- Set data structure
- Map data structure
- WeakMap data structure
- ES6 arrow functions
- Spread operator
- Method chaining

## Author

Gerald D. Carrasquillo
Holberton School
