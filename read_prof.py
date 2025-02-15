import pstats

p = pstats.Stats('main.prof')

with open('main_prof.txt', 'w+', encoding='utf-8') as f:
    f.write(p.sort_stats('calls').print_stats())