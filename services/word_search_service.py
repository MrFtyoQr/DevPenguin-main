import random

class WordSearchService:
    @staticmethod
    def generate_word_search(topic: str, size: int = 10):
        words = [topic.upper(), topic.upper()[::-1]]
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        answer_positions = []

        for word in words:
            placed = False
            while not placed:
                direction = random.choice(['horizontal', 'vertical', 'diagonal'])
                row = random.randint(0, size - 1)
                col = random.randint(0, size - 1)

                if direction == 'horizontal' and col + len(word) <= size:
                    for i, char in enumerate(word):
                        grid[row][col + i] = char
                    answer_positions.append({
                        "word": word,
                        "start": [row, col],
                        "end": [row, col + len(word) - 1],
                        "direction": "horizontal"
                    })
                    placed = True
                elif direction == 'vertical' and row + len(word) <= size:
                    for i, char in enumerate(word):
                        grid[row + i][col] = char
                    answer_positions.append({
                        "word": word,
                        "start": [row, col],
                        "end": [row + len(word) - 1, col],
                        "direction": "vertical"
                    })
                    placed = True
                elif direction == 'diagonal' and row + len(word) <= size and col + len(word) <= size:
                    for i, char in enumerate(word):
                        grid[row + i][col + i] = char
                    answer_positions.append({
                        "word": word,
                        "start": [row, col],
                        "end": [row + len(word) - 1, col + len(word) - 1],
                        "direction": "diagonal"
                    })
                    placed = True

        for i in range(size):
            for j in range(size):
                if grid[i][j] == ' ':
                    grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        word_search = '\n'.join([' '.join(row) for row in grid])
        return {
            "word_search": word_search,
            "answers": answer_positions
        }
