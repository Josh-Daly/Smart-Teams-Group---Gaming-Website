<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tic-Tac-Toe - StarFive Games</title>
  <style>
    
</head>
<body>
  <header>
    <a href="../index.html" class="logo">StarFive Games</a>
    <nav>
      <a href="../index.html">Home</a>
      <a href="../links.html">All Games</a>
      <a href="../contact.html">Contact</a>
    </nav>
  </header>

  <main>
    <div class="game-container">
      <h1>Tic-Tac-Toe</h1>
      <div class="status" id="status">Your turn (X)</div>
      <div class="board" id="board">
        <div class="cell" data-index="0"></div>
        <div class="cell" data-index="1"></div>
        <div class="cell" data-index="2"></div>
        <div class="cell" data-index="3"></div>
        <div class="cell" data-index="4"></div>
        <div class="cell" data-index="5"></div>
        <div class="cell" data-index="6"></div>
        <div class="cell" data-index="7"></div>
        <div class="cell" data-index="8"></div>
      </div>
      <button class="reset-btn" id="resetBtn">Play Again</button>
    </div>
  </main>

  <footer>
    <p>&copy; 2026 StarFive Games. All Rights Reserved</p>
  </footer>

  <script>
    const PLAYER = 'X';
    const COMPUTER = 'O';
    let board = ['', '', '', '', '', '', '', '', ''];
    let gameActive = true;

    const cells = document.querySelectorAll('.cell');
    const status = document.getElementById('status');
    const resetBtn = document.getElementById('resetBtn');

    const winPatterns = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
      [0, 4, 8], [2, 4, 6]             // diagonals
    ];

    function checkWinner() {
      for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
          return { winner: board[a], pattern };
        }
      }
      return board.includes('') ? null : { winner: 'draw', pattern: [] };
    }

    function handleCellClick(e) {
      const index = e.target.dataset.index;
      
      if (!gameActive || board[index] || e.target.classList.contains('taken')) {
        return;
      }

      // Player move
      board[index] = PLAYER;
      e.target.textContent = PLAYER;
      e.target.classList.add('taken', 'x');

      const result = checkWinner();
      if (result) {
        endGame(result);
        return;
      }

      status.textContent = "Computer's turn...";
      gameActive = false;

      // Computer move with delay
      setTimeout(() => {
        computerMove();
        const computerResult = checkWinner();
        if (computerResult) {
          endGame(computerResult);
        } else {
          status.textContent = 'Your turn (X)';
          gameActive = true;
        }
      }, 500);
    }

    function computerMove() {
      const emptyCells = board.map((val, idx) => val === '' ? idx : null).filter(val => val !== null);
      
      if (emptyCells.length > 0) {
        const randomIndex = emptyCells[Math.floor(Math.random() * emptyCells.length)];
        board[randomIndex] = COMPUTER;
        const cell = cells[randomIndex];
        cell.textContent = COMPUTER;
        cell.classList.add('taken', 'o');
      }
    }

    function endGame(result) {
      gameActive = false;
      
      if (result.winner === 'draw') {
        status.textContent = "It's a Draw!";
      } else if (result.winner === PLAYER) {
        status.textContent = 'You Win! 🎉';
        highlightWinner(result.pattern);
      } else {
        status.textContent = 'You Lose! 😔';
        highlightWinner(result.pattern);
      }
    }

    function highlightWinner(pattern) {
      pattern.forEach(index => {
        cells[index].classList.add('winner');
      });
    }

    function resetGame() {
      board = ['', '', '', '', '', '', '', '', ''];
      gameActive = true;
      status.textContent = 'Your turn (X)';
      
      cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('taken', 'x', 'o', 'winner');
      });
    }

    cells.forEach(cell => cell.addEventListener('click', handleCellClick));
    resetBtn.addEventListener('click', resetGame);
  </script>
</body>
</html>