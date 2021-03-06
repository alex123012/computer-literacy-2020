#!/home/alexmakh/miniconda3/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patheffects as path_effects

# Создаю фигуру
fig = plt.figure()

# Дабавляю один список axes
ax = fig.add_subplot(111)

# Привожу в похожий вид саму фигуру:
# Название графика
ax.set_title('BMF plotting', fontsize=60,
             fontweight='bold', color='g', pad=170,
             path_effects=[path_effects.withSimplePatchShadow()])

# Обозначения осей
ax.set_xlabel(r'$lg \ R_{e}$', fontsize=25, color='darkviolet')
ax.text(2.35, 1.13, r'$lg \ (100\varphi)$', style='oblique', color='purple',
        fontweight='normal', fontsize=25)

# Какой-то рандомный текст, который был в образце под названием графика
ax.text(4.2, 1.05, 'kek lol arbidol\nlol kek cheburek',
        style='oblique', color='w', fontweight='normal',
        fontsize=35,  # Текст с "оберткой":
        bbox={'facecolor': 'red', 'alpha': 1, 'pad': 10,
              'path_effects': [path_effects.withSimplePatchShadow()]},
        path_effects=[path_effects.withSimplePatchShadow()])
ax.text(2.7, 1.25, r'OMG its PyPlot:', style='oblique', color='y',
        fontweight='bold', fontsize=35)

# Область определения функции
ax.text(4.1, 1.25, r'$4000<Re<80\frac{d}{\Delta}$', color='red', fontsize=35)

# Функция, которые также были под названием
ax.text(5.4, 1.25, r'$\varphi=f(R_{e})$', color='darkviolet', fontsize=35,
        path_effects=[path_effects.withSimplePatchShadow()])

# Текст внутри графика
ax.text(3, 0.48, r'$E=mc^2$', fontsize=15,
        bbox={'facecolor': 'w', 'alpha': 1, 'pad': 5})
ax.text(3.5, 0.7, r'$S=vt$', fontsize=15,
        bbox={'facecolor': 'w', 'alpha': 1, 'pad': 5})
ax.text(4, 0.59, r'$F=ma$', fontsize=15,
        bbox={'facecolor': 'w', 'alpha': 1, 'pad': 5})

# Звиздочка гы-гы-гы
ax.text(2.5, 1.2325, r'$\star$', fontsize=80, color='purple')

# Основные прямые
ax.plot([3.3, 3.3], [0.2, 1.1], linewidth=3, color='red', dashes=[10, 4])
ax.plot([3.3, 5.1], [0.68, 0.2], linewidth=9, color='orange', alpha=1)
ax.plot([2.7, 3.4], [1.1, 0.37], linewidth=9, color='green', alpha=1)

# К сожалению, я не знаю, что за формулы у оставшихся графов, поэтому
# сделал их ввиде прямых

# Основные прямые
las = [0.3, 0.37, 0.44, 0.51, 0.58]
col = ['r', 'b', 'g', 'c', 'm']
j = 0
for i in las:
    x = np.linspace((1.56-i)*15/4, 5.95, 50)
    y = np.linspace(i, i+0.35, 50)
    yer = y + 0.01 * np.random.normal(size=x.shape)
    ax.plot(x, y, '{}'.format(col[j]), linewidth=4)
    ax.plot(x, yer, '{}o'.format(col[j]),
            markeredgecolor='black', markersize=10)
    j += 1

# Перемычка
x = np.linspace(3.3, 3.675, 6)
y = [0.28*i - 0.449 for i in x]
yer = y + 0.01 * np.random.normal(size=x.shape)
ax.plot(x, y, linewidth=4, color='m')
ax.plot(x, yer, 'mo', markeredgecolor='black', markersize=10)
for j in col:
    x = np.linspace(3.3, 3.675, 4)
    y = [0.28*i - 0.449 for i in x]
    yer = y + 0.01 * np.random.normal(size=x.shape)
    ax.plot(x, yer, '{}o'.format(j), markeredgecolor='black', markersize=10)

# На зеленой линии точки
i = 0
for j in col:
    x = np.linspace(3, 3.3, 2+2*i)
    y = [-1.043*i + 3.93 for i in x]
    yer = y + 0.01 * np.random.normal(size=x.shape)
    ax.plot(x, yer, '{}o'.format(j), markeredgecolor='black', markersize=10)
    i += 1

# На оранжевой линии точки
ind = 0
for j in col:
    x = np.linspace(3.675, (1.56-las[ind])*15/4, 20-3*ind)
    y = np.linspace(0.28*3.675-0.449, las[ind], 20-3*ind)
    yer = y + 0.01 * np.random.normal(size=x.shape)
    ax.plot(x, yer, '{}o'.format(j), markeredgecolor='black', markersize=10)
    ind += 1

# Какие-то циферки справа
c = [252, 126, 60, 30.6, 1.5]
j = 0
for i in las:
    ax.text(6.05, i+0.35, r'{}'.format(c[j]), color='r', fontsize=20)
    j += 1

# Тики для оси абсцисс
xticks = np.arange(2.6, 6.2, 0.2)
xtickla = ['' for i in range(len(xticks))]
j = 2
for i in range(3, 7):
    xtickla[j] = '%1.1f' % i
    j += 5
ax.xaxis.set_ticks(xticks)
ax.xaxis.set_ticklabels(xtickla, fontsize=20, color='darkred')

# Тики для оси ординат
yticks = np.arange(0.2, 1.1, 0.1)
ytickla = ['' for i in range(len(yticks))]
j = 0
for i in range(2, 12, 2):
    ytickla[j] = i/10
    j += 2
ax.yaxis.set_ticks(yticks)
ax.yaxis.set_ticklabels(ytickla, fontsize=20, color='darkred')

# Размер фигуры
fig.set_figwidth(15)
fig.set_figheight(10)

# Фоновое изображение
fn = r'fon.jpg'
im = plt.imread(fn)
ax.figure.figimage(im,
                   ax.bbox.xmax//2 - im.shape[0]*0.4,
                   ax.bbox.ymax//2 - im.shape[1]//3,
                   alpha=.15, zorder=1)

# Сеточка
ax.grid(axis='both', color='black', linewidth=2)

# Размер осей
ax.axis([2.6, 6.0, 0.2, 1.1])

# Поехали!
plt.show()
