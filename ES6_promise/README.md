# ES6 Promises

This project contains exercises and tasks focused on ES6 Promises in JavaScript. It covers fundamental concepts of asynchronous programming using Promises, async/await, and error handling.

## Description

In this project, you'll learn about:
- How to use Promises (then, resolve, catch methods)
- How to use the `then`, `resolve`, and `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an async function

## Requirements

- Ubuntu 18.04 LTS using Node 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest and the command `npm run test`
- Your code will be verified against lint using ESLint
- All of your functions must be exported

## Setup

### Install NodeJS 12.11.x

In your home directory:

```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Verify installation:

```bash
nodejs -v
# v12.11.1
npm -v
# 6.11.3
```

### Install Project Dependencies

In your project directory, install Jest, Babel, and ESLint:

```bash
npm install
```

## Configuration Files

The following configuration files are included in this project:

- `package.json` - Project dependencies and scripts
- `babel.config.js` - Babel transpiler configuration
- `.eslintrc.js` - ESLint linting rules

## Files

| File | Description |
|------|-------------|
| `0-promise.js` | Returns a Promise using the prototype function `getResponseFromAPI()` |
| `1-promise.js` | Returns a promise that resolves or rejects based on a boolean parameter |
| `2-then.js` | Handles promise resolution with `then`, `catch`, and `finally` |
| `3-all.js` | Handles multiple promises using `Promise.all()` |
| `4-user-promise.js` | Returns a resolved promise with user object |
| `5-photo-reject.js` | Returns a rejected promise with an error |
| `6-final-user.js` | Handles multiple promises using `Promise.allSettled()` |
| `7-load_balancer.js` | Returns the value of the first resolved promise using `Promise.race()` |
| `8-try.js` | Throws an error when dividing by zero |
| `9-try.js` | Uses try/catch to handle errors and returns an array of results |
| `100-await.js` | Uses async/await to handle promises |
| `utils.js` | Contains utility functions `uploadPhoto()` and `createUser()` |

## Usage

### Running Tests

To run all tests:

```bash
npm run test
```

To run a specific test file:

```bash
npm run test <test-file>
```

### Linting

To check code style:

```bash
npm run lint [filename]
```

To run full test suite with linting:

```bash
npm run full-test
```

### Running Code

To run any JavaScript file with Babel:

```bash
npm run dev <filename>
```

Example:

```bash
npm run dev 0-main.js
```

## Tasks

### 0. Keep every promise you make and only make promises you can keep

Return a Promise using the function `getResponseFromAPI()`.

### 1. Don't make a promise...if you know you can't keep it

Return a promise. The promise resolves with success status when the boolean is true, or rejects with an error when false.

### 2. Catch me if you can!

Handle promise responses by appending handlers. Log a message when the API returns a response.

### 3. Handle multiple successful promises

Import functions from `utils.js` and use `Promise.all()` to handle multiple promises collectively.

### 4. Simple promise

Return a resolved promise with an object containing `firstName` and `lastName`.

### 5. Reject the promises

Return a rejected promise with an error message.

### 6. Handle multiple promises

Use `Promise.allSettled()` to handle multiple promises and return an array with status and value/reason.

### 7. Load balancer

Use `Promise.race()` to return the value from the promise that resolves first.

### 8. Throw error / try catch

Write a function that throws an error when attempting to divide by zero.

### 9. Throw an error

Use try/catch to handle function execution and return results in an array.

### 10. Await / Async (Advanced)

Use async/await syntax to call multiple functions and handle errors gracefully.

## Author

Holberton School Project

## License

ISC
