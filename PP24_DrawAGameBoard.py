def gameBoard(width, height):
	
	horizontal = ' ---'
	vertical = '|'
	middle = '   '

	otherRow = \
		'\n' + vertical + ((middle + vertical) * width) + \
		'\n' + (horizontal * width)

	topRow = (horizontal * width) + otherRow
	
	print (topRow + ((otherRow) * (height - 1)))


if __name__ == '__main__':
	userWidth = int(input('How WIDE would you like the game board to be: '))
	userHeight = int(input('How HIGH would you like the game board to be: '))
	gameBoard(userWidth, userHeight)
