# -*- coding: utf-8 -*-

def main():
  print ''
  print '空欄を0として1行ずつ問題を入力してください。'
  problem = getProblem()
  if validProblem(problem):
    if solve(0, 0, problem):
      print '解けた！'
    else:
      print '解けなかった…orz'
    for y in range(0, 9):
      for x in range(0, 9):
        print problem[y][x],
      print
  else:
    print '不正な問題です。もう１度最初から入力しなおしますか？ (yes/no)'
    if raw_input() == 'yes':
      main()

def getProblem():
  problem = []
  for y in range(0, 9):
    input = raw_input('...')
    while len(input) != 9 or not input.isdigit():
      print '不正な入力です。もう１度同じ行を入力してください。'
      input = raw_input('...')
    problem.append([int(n) for n in input])
  return problem

def validProblem(problem):
  for y in range(0, 9):
    for x in range(0, 9):
      if problem[y][x] != 0:
        if not isValid(x, y, problem):
          return False
  return True

def solve(x, y, workspace):
  if (x, y) == (0, 9):
    return True
  if workspace[y][x] == 0:
    for n in range(1, 10):
      workspace[y][x] = n
      if isValid(x, y, workspace):
        (nx, ny) = nextPoint(x, y)
        if solve(nx, ny, workspace):
          return True
    workspace[y][x] = 0
    return False
  else:
    (nx, ny) = nextPoint(x, y)
    if solve(nx, ny, workspace):
      return True

def isValid(x, y, workspace):
  for yoko in range(0, 9): # 横を見る
    if x != yoko:
      if workspace[y][x] == workspace[y][yoko]:
        return False
  for tate in range(0, 9): # 縦を見る
    if y != tate:
      if workspace[y][x] == workspace[tate][x]:
        return False
  for gy in range(y/3*3, (y/3+1)*3): # 3*3グループを見る
    for gx in range(x/3*3, (x/3+1)*3):
      if (y,x) != (gy, gx):
        if workspace[y][x] == workspace[gy][gx]:
          return False
  return True

def nextPoint(x, y):
  x += 1
  if x > 8:
    x = 0
    y += 1
  return (x, y)

if __name__ == '__main__':
  print '9 * 9 Sudoku Solver by yosida95'
  main()

