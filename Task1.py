# Задание 1: Даны две  независимые выборки. Не соблюдается условие нормальности
# x1 380, 420, 290
# y1 140, 360, 200, 900
# Сделайте вывод по результатам, полученным с помощью функции.

import numpy as np
import scipy.stats as stats

x = np.array([380, 420, 290])
y = np.array([140, 360, 200, 900])

stats.mannwhitneyu(x, y)
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# Т.к. pvalue имеет высокое значение (заведомо выше разумных альфа),
# то верна гипотеза H0, т.е. статистически значимых различий нет.
