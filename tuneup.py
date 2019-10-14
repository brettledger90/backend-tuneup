__author__ = "Brett"
import cProfile
import pstats
import functools
import timeit
from collections import Counter
def profile(func):
   
   def function_wrapper(x):
       pr = cProfile.Profile()
       pr.enable()
       func(x)
       pr.disable()
       stats = pstats.Stats(pr).sort_stats('cumulative')
       stats.print_stats()
   return function_wrapper
def read_movies(src):
   
   print('Reading file: {}'.format(src))
   with open(src, 'r') as f:
       return f.read().splitlines()
@profile
def find_duplicate_movies(src):

   movie_counter = Counter([x.lower() for x in read_movies(src)])
   duplicates = [k for k, v in movie_counter.items() if v > 1]
   return duplicates
def timeit_helper():
   
   n = 8
   r = 6
   t = timeit.Timer(lambda: find_duplicate_movies('movies.txt'))
   result = t.repeat(repeat=r, number=n)
   result = [x / n for x in result]
   print('Best time across {} repeats of {} runs per repeat: {} sec'.format(
       r, n, min(result)))
def main():
   find_duplicate_movies('movies.txt')
   timeit_helper()

if __name__ == '__main__':
   main()
