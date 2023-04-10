# Даны 3 группы  учеников плавания.
# В 1 группе время на дистанцию 50 м составляют: 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54

import numpy as np
import scipy.stats as stats

x = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
y = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
z = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

stats.kruskal(x, y, z)
# KruskalResult(statistic=5.465564058257224, pvalue=0.0650380998590494)
# Т.к. pvalue выше стандартной альфа в 5%, то верна гипотеза H0, т.е. статистически значимых различий нет.