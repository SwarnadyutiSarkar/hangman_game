const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

const words = ['hangman', 'javascript', 'coding', 'express', 'frontend'];
let currentWord = '';
let guessedLetters = [];
let wrongGuesses = 0;

function getRandomWord() {
    return words[Math.floor(Math.random() * words.length)];
}

app.get('/start', (req, res) => {
    currentWord = getRandomWord().toUpperCase();
    guessedLetters = [];
    wrongGuesses = 0;
    res.json({ currentWord: '_'.repeat(currentWord.length), wrongGuesses });
});

app.post('/guess', (req, res) => {
    const { letter } = req.body;
    if (!letter || letter.length !== 1) {
        return res.status(400).json({ error: 'Invalid letter' });
    }

    letter = letter.toUpperCase();
    if (currentWord.includes(letter)) {
        guessedLetters.push(letter);
    } else {
        wrongGuesses += 1;
    }

    const displayWord = currentWord
        .split('')
        .map(l => (guessedLetters.includes(l) ? l : '_'))
        .join('');

    res.json({ displayWord, wrongGuesses });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
