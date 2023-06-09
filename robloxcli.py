import curses,traceback,time,sys,colorama,time
try:
    curlevel = int(sys.argv[1])-1
except:
    print('Tip: you can always specify a level you want to be on')
    curlevel = 0
colorama.init()
sys.stdout.write('\33]0;Python platformer\a')
sys.stdout.flush()
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
# Some kinda of level editor
levels = [['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'.................#..................####.......................................',
'..................................#............................................',
'....level.1.....................#..............................................',
'............................###................................................',
'.......###.#..#####..#..###....................................................',
'......###......................................................................',
'#..######................................#....Finish...........................',
'..............................................V................................',
'...............................................................................',
'..............................................!................................',
'...........................................#######.............................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'....level.2....................................................................',
'......spike....................................................................',
'......V..........#####.........................................................',
'......^.........^#.............................................................',
'#..######.####.###.............................................................',
'...............................................................................',
'......................!........................................................',
'......................#........................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'.............................................#.................................',
'.............................................#.................................',
'....level.3..................................#.................................',
'.............................................#.................................',
'.......###.#..#####..#..####################.#.................................',
'......###..................................^.^.................................',
'#..######..................................^.^.................................',
'...........................................^.^.................................',
'...........................................^.^.................................',
'...........................................^!^.................................',
'...........................................###.................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'.............................................#.................................',
'.............................................#.................................',
'....level.4.(level 3 but harder)...............................................',
'.............................................#.................................',
'...........#..#..#.#.#..#####..#..#..#######.#.................................',
'......###..................................^.^.................................',
'#..######..................................^.^.................................',
'...........................................^.^.................................',
'...........................................^.^.................................',
'...........................................^.^.................................',
'...........................................^.^.................................',
'...........................................^.^.................................',
'...........................................^......!............................',
'...........................................^#######............................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'....level.5....................................................................',
'....end.(look.close.at.bottom).................................................',
'...............................................................................',
'...............................................................................',
'.....^^........................................................................',
'#..######......................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'........^!^....................................................................',
'........###....................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'.............#####.............................................................',
'...............................................................................',
'...............................................................................',
'............#.....#............................................................',
'...............................................................................',
'....level.6....................................................................',
'...........#.......#...........................................................',
'.......................#.......................................................',
'.......................#^!^....................................................',
'#..#########........#######....................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'....level.7....................................................................',
'....just.get.to.win............................................................',
'...............................................................................',
'............############^!^....................................................',
'#..#########...................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...........ghost.blocks........................................................',
'...............................................................................',
'...........V...................................................................',
'...............................................................................',
'...........@...................................................................',
'....level.8@...................................................................',
'...........@...................................................................',
'...........@...................................................................',
'...........@.........!.........................................................',
'#..####################........................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...........Remember what i said?...............................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'....level.9....................................................................',
'..........(spam d or skip it)..................................................',
'...............................................................................',
'...............................................................................',
'#..########@@@##@@@##@@@##@@@##################################################',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'..Wait what is the level?......................................................',
'.........level.1?..............................................................',
'#################..............................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'....level.11...................................................................',
'...............................................................................',
'..press d to win...............................................................',
'.!.............................................................................',
'##.............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'........wait aint that a level 1...............................................',
'...............................................................................',
'...............................................................................',
'.................#..................####.......................................',
'..................................#............................................',
'....level.12....................#..............................................',
'............................###................................................',
'.......###.#..#####..#..###....................................................',
'......###......................................................................',
'#..######................................#.....................................',
'...............................................................................',
'...............................................................................',
'..............................................!................................',
'...........................................#######.............................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'....end........................................................................',
'....Press.Q.to.exit............................................................',
'...............................................................................',
'...............................................................................',
'#..######......................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'.!.............................................................................',],

['...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...level.0.....................................................................',
'....How did we get here?.......................................................',
'...............................................................................',
'...............................................................................',
'#..######......................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',
'...............................................................................',],
]

y = 4
x = 0
yvel = 0
screen.nodelay(1)
curses.mousemask(1)
curses.mouseinterval(0)
try:
    while True:
        event = screen.getch()
        if event == ord("q"): break
        for c,i in enumerate(levels[curlevel]):
            screen.addstr(c,0,i)
        screen.addstr(y,x,'0')
        if event == ord("w"):
            try:
                if levels[curlevel][y+1][x] == '#':
                    yvel=3
            except:
                pass
        if event == ord("a"):
            try:
                if not levels[curlevel][y][x-1] == '#':
                    x-=1
            except:
                pass
        if event == ord("d"):
            try:
                if not levels[curlevel][y][x+1] == '#':
                    x+=1
            except:
                pass
        if yvel > 0:
            if not levels[curlevel][y-1][x] == '#':
                y-=yvel
            else:
                y+=1
            yvel-=1
        if not levels[curlevel][y+1][x] == '#':
            y+=1
        if levels[curlevel][y][x] == '!' or levels[curlevel][y][x] == '?':
            curlevel +=1
            y = 4
            x = 0
        elif levels[curlevel][y][x] == '^':
            raise Exception('You died')
        _, mx,my,_,_ = curses.getmouse()
        screen.addstr(my,mx,'<')
        time.sleep(0.0855)
except:
    curses.endwin() # Huston we have a problem
    traceback.print_exc()
curses.endwin()
