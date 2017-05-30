# example program to demonstrate PuDB debugger; finds insertion point in
# a sorted list

def findinspt(x,xnew):  # returns insertion point of xnew in x
   n = len(x)
   lo = 0
   hi = n-1
   while True:
      mid = int((lo + hi) / 2)
      if xnew > x[mid]: lo = mid + 1
      else: hi = mid
      if xnew == x[mid]: return mid
      if lo == hi: return lo

y = [5,12,13]
print(findinspt(y,3))
print(findinspt(y,8))
print(findinspt(y,12))
print(findinspt(y,30))
