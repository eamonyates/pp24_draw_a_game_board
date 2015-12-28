def gameBoard(width=3, height=3):
	
	horizontal = ' ---'
	vertical = '|'
	middle = '   '

	topRow = \
		(horizontal * width) + \
		'\n' + vertical + ((middle + vertical) * width) + \
		'\n' + (horizontal * width)
	otherRow = \
		'\n' + vertical + ((middle + vertical) * width) + \
		'\n' + (horizontal * width)
	
	print (topRow + ((otherRow) * (height - 1)))


if __name__ == '__main__':
	gameBoard()
