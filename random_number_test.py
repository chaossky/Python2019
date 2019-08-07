#두개의 모듈 패키지를 임포트 한다.
import matplotlib.pyplot as plt
import random

#최대 1000번
MAX_NUM = 1000

#범위를 정해준다.
x_values = range(1, MAX_NUM + 1)
values = [random.randint(1, MAX_NUM) for x in x_values]
y_values = [values.count(x) for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title(f"Random Number Occurrences (N = {MAX_NUM})", fontsize=18)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Occurrences", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()