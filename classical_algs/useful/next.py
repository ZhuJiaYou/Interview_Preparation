def getnext(s):
    n = [0] * len(s)
    j = -1
    n[0] = -1
    for i in range(1, len(s)):
        while s[j+1]!=s[i] and j!=-1:  #一定要先回退
            j = n[j]
        if s[j+1] == s[i]:#再判断相等
            n[i] = j+1
        j = n[i]
    return n


def gen_pnext(substring):
  """
  构造临时数组pnext
  """
  index, m = 0, len(substring)
  pnext = [0]*m
  i = 1
  while i < m:
    if (substring[i] == substring[index]):
      pnext[i] = index + 1
      index += 1
      i += 1
    elif (index!=0):
      index = pnext[index-1]
    else:
      pnext[i] = 0
      i += 1
  return pnext


if __name__ == '__main__':
    print(gen_pnext('BBABBCAC'))