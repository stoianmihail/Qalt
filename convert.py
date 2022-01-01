import sys

def main():
  ratio = float(sys.argv[1])
  with open('coords.out', 'w') as g:
    with open('coords.in', 'r') as f:
      for line in f.readlines():
        pattern = 'coords='
        pos1 = line.find(pattern) + len(pattern) + 1
        pos2 = line[pos1:].find('"')
        coords = line[pos1:pos1+pos2]
        ret = list(map(lambda x: round(float(x) * ratio), coords.split(',')))
        tmp = ','.join(map(str, ret))
        g.write(line[:pos1] + tmp + line[pos1+pos2:])
  pass

if __name__ == '__main__':
  main()
