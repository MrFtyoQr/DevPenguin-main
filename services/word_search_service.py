import random

class WordSearchService:
    @staticmethod
    def generate_word_search(topic: str, size: int = 10, word_list: list = None):
        if word_list is None:
            # Lista de palabras relacionadas con el tema
            word_list = [topic.upper(), topic.upper()[::-1]]
        
        # Convertir las palabras a mayúsculas
        words = [word.upper() for word in word_list]
        
        # Crear una cuadrícula vacía
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        answer_positions = []

        for word in words:
            placed = False
            attempts = 0
            while not placed and attempts < 100:
                attempts += 1
                direction = random.choice(['horizontal', 'vertical', 'diagonal'])
                if direction == 'horizontal':
                    row = random.randint(0, size - 1)
                    col = random.randint(0, size - len(word))
                    if all(grid[row][col + i] in (' ', word[i]) for i in range(len(word))):
                        for i, char in enumerate(word):
                            grid[row][col + i] = char
                        answer_positions.append({
                            "word": word,
                            "start": [row, col],
                            "end": [row, col + len(word) - 1],
                            "direction": "horizontal"
                        })
                        placed = True
                elif direction == 'vertical':
                    row = random.randint(0, size - len(word))
                    col = random.randint(0, size - 1)
                    if all(grid[row + i][col] in (' ', word[i]) for i in range(len(word))):
                        for i, char in enumerate(word):
                            grid[row + i][col] = char
                        answer_positions.append({
                            "word": word,
                            "start": [row, col],
                            "end": [row + len(word) - 1, col],
                            "direction": "vertical"
                        })
                        placed = True
                elif direction == 'diagonal':
                    row = random.randint(0, size - len(word))
                    col = random.randint(0, size - len(word))
                    if all(grid[row + i][col + i] in (' ', word[i]) for i in range(len(word))):
                        for i, char in enumerate(word):
                            grid[row + i][col + i] = char
                        answer_positions.append({
                            "word": word,
                            "start": [row, col],
                            "end": [row + len(word) - 1, col + len(word) - 1],
                            "direction": "diagonal"
                        })
                        placed = True

        # Rellenar los espacios vacíos con letras aleatorias
        for i in range(size):
            for j in range(size):
                if grid[i][j] == ' ':
                    grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        word_search = '\n'.join([' '.join(row) for row in grid])
        return {
            "word_search": word_search,
            "answers": answer_positions
        }
