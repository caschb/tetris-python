class TextUI:

    def print_grid(self, grid, falling_piece, falling_piece_position):
        printed = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for piece_row in falling_piece.position:
                    if row == falling_piece_position[0] + piece_row[0] and \
                            col == falling_piece_position[1] + piece_row[1]:
                        print('1', end=" ")
                        printed = True
                if not printed:
                    print(grid[row][col], end=" ")
                else:
                    printed = False
            print("")
