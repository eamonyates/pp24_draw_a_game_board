def gameBoard(width=3, height=3):
	
	horizontal = ' ---'
	vertical = '|'
	middle = '   '

	otherRow = \
		'\n' + vertical + ((middle + vertical) * width) + \
		'\n' + (horizontal * width)

	topRow = (horizontal * width) + otherRow
	
	print (topRow + ((otherRow) * (height - 1)))


if __name__ == '__main__':
	gameBoard()
