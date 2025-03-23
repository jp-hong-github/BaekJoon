const fs = require('fs')
const filePath = process.platform === 'win32' ? '../input.txt' : '/dev/stdin'
const input = fs.readFileSync(filePath).toString().trim().split('\n')

function solution(board) {
	let count = 0

	for (let i = 0; i < 8; i++) {
		for (let j = 0; j < 8; j++) {
			if ((i + j) % 2 === 0 && board[i][j] === 'F') {
				count++
			}
		}
	}

	return count
}

console.log(solution(input))
