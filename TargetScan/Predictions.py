#! /home/alexmakh/miniconda3/bin/python3

"""
            Functions for investgations

its a few funcs to solve some problems with comparison
    prediction datasets from TargetScan and miRDB
                with some features

"""

import pandas as pd
import numpy as np
import re

if __name__ != '__main__':
    # Функция для удаления приставки 'hsa-'
    # из названия микроРНК в датафрейме экспрессии
    def hsa_l(object):
        # Замена новым названием
        for ind in object.index:
            object.loc[ind, 'miRNA'] = object.loc[
                ind, 'miRNA'].replace("hsa-", "")

    # Функция для выделения из датафрейма TargetScan
    # соеденинных названий микроРНК
    # (пример работы:
    # 'let-7-5p/98-5p' -> ['let-7-5p', 'miR-98-5p'])
    def Target_remake(tar):
        target_convert = pd.DataFrame(
            columns=['miRNA', 'Site_type'])  # новый датафрейм на выход
        ind = 0
        cat = np.unique(tar['miRNA'].values)  # список всех названий микроРНК
        for i in cat:
            i = str(i)
            temp = np.unique(tar[tar['miRNA'] == i]['Site_type'])
            # используя регулярное выражение делим строку
            for j in re.split('/', i):
                # И добавляем к ней "miR-" (стандарт названий)
                if 'miR-' not in j:
                    if 'let-' not in j:
                        j = 'miR-' + j
                # Занаосим в новый датафрейм
                target_convert.loc[ind] = [j, temp]
                ind += 1
        return(target_convert)

    # Функция для удаления приставки 'hsa-'
    # из названия микроРНК в датафрейме miRDB

    # Переделать
    def hsa_m(mirdb):
        for ind in mirdb.index:
            # Замена новым названием
            mirdb.loc[ind, 'miRNA Name'] = mirdb.loc[
                ind, 'miRNA Name'].replace("hsa-", "")

    # Функция для создания датафрейма из пересечений
    # предикшенов TargetScan и miRDB
    def comparasion_full(tar, mirdb):
        ind = 0
        comparasion = pd.DataFrame(
            columns=['miRNA', 'miRDB score', 'site type'])  # новый дата фрейм
        for i in np.unique(tar['miRNA'].values):
            if i in mirdb['miRNA Name'].values:  # Сравнение имен микроРНК
                # Заносим в датафрейм, если удовлетворяет условию
                comparasion.loc[ind] = [i, mirdb[
                    mirdb['miRNA Name'] == i]['Target Score'].values[0], list(
                    tar[tar['miRNA'] == i]['Site_type'].values)[0].tolist()]
                ind += 1
        return(comparasion)

    # Функция создает дополнительный столбец под среднее значение
    # экспрессии для датафрейма из прошлой функции, также удаляет строки
    # с микроРНК, которых нет в датафрейме экспрессии
    def comparasion_exp(tar, lung):
        tar['average'] = ''  # дополнительный столбец
        for i in tar['miRNA'].values:
            # если нет такой микроРНК, удаляем строку
            if i not in lung['miRNA'].values:
                tar.drop([tar.index[tar['miRNA'] == i][0]],
                         axis=0, inplace=True)
            else:  # если есть - оставляем
                tar.loc[[tar.index[tar['miRNA'] == i][0]], 'average'] = lung[
                    lung['miRNA'] == i]['average'].values[0]

    # Сохранение датафрейма в файл
    def save_top(vid, file='top_miRNAs'):
        with open('{}.txt'.format(file), 'w') as f:
            vid.to_csv(f, sep='\t', index=False)

    # Удаляем строки с TargetScore < 75
    def top_score(data):
        data.drop(np.where(data['miRDB score'] < 75)[0], inplace=True)

    # Функция, которая объединяет все предыдущие функции
    def all_score(mirdb, tar, lungs, file='filename'):
        hsa_l(lungs)  # Убираем "miR-" из названий микроРНК
        hsa_m(mirdb)  # Убираем "miR-" из названий микроРНК
        tar_con = Target_remake(tar)  # Разделяем некоторые слипшиеся микроРНК
        # Сравниваем предикшены miRDB и TargetScore
        comparasion = comparasion_full(tar_con, mirdb)
        # Сравниваем пересечения из прошлой функции с таблицей экспрессии
        comparasion_exp(comparasion, lungs)
        # сортировка по TargetScore
        comparasion.sort_values('miRDB score',
                                ascending=False, inplace=True)
        save_top(comparasion, file)  # Сохраняем в файл

    def all_exp(mirdb, tar, lungs, file='filename'):
        hsa_m(mirdb)  # Убираем "miR-" из названий микроРНК
        # Разделяем некоторые "слипшиеся" микроРНК
        tar_con = Target_remake(tar)
        # Сравниваем предикшены miRDB и TargetScore
        comparasion = comparasion_full(tar_con, mirdb)
        # Сравниваем пересечения из прошлой функции с таблицей экспрессии
        comparasion_exp(comparasion, lungs)
        # сортировка по TargetScore
        comparasion.sort_values('average',
                                ascending=False, inplace=True)
        save_top(comparasion, file)  # Сохраняем в файл

    # Получение пересечений TargetScan и miRDB с TargetScore > 75
    def without_exp(mirdb, tar, file='filename'):
        hsa_m(mirdb)  # Убираем "miR-" из названий микроРНК
        tar_con = Target_remake(tar)  # Разделяем некоторые слипшиеся микроРНК
        # Сравниваем предикшены miRDB и TargetScore
        comparasion = comparasion_full(tar_con, mirdb)
        top_score(comparasion)  # оставляем только с TargetScore >= 75
        # сортировка по TargetScore
        comparasion.sort_values('miRDB score',
                                ascending=False, inplace=True)
        save_top(comparasion, file)  # Сохраняем в файл

    # Функция, которая сравнивает топ-25% предикшенов по all_score
    # и топ-10% по экспрессии
    def first_result(ded, file, lung):
        lung.sort_values('average', ascending=False, inplace=True)
        # Лучших 10% микроРНК по экспрессии
        v = int(lung.shape[0] * 0.1)

        # Получаем датафрейм только с 25% лучших по TargetScore микроРНК
        data = pd.DataFrame(pd.read_csv('{}.txt'.format(ded), sep='\t'))
        data = data.head(int(0.25 * data.shape[0]))

        # Сравниваем два полученных выше датафрейма
        for i in data['miRNA'].tolist():
            if i not in lung.head(v)['miRNA'].tolist():
                data.drop(data[data['miRNA'] == i].index.tolist(),
                          inplace=True, axis=0)
        # сортировка по TargetScore полученного датафрейма
        data.sort_values('miRDB score', ascending=False, inplace=True)
        save_top(data, file)  # Сохранение

    def locus(corona, string, protein):
        data_res = pd.DataFrame(pd.read_csv(
            'Results/{}.txt'.format(string),
                                sep='\t'))  # Подгрузка результатов
        data_res.drop('site type', axis=1, inplace=True)
        data = pd.DataFrame.copy(corona)  # Подгрузка изначального датасета

        # Получение названия всех микроРНК
        names = ', '.join(data['miRNA'].tolist())
        ind = 1  # из изначального датасета
        # максимальный индекс в изначальном датасете
        in_max = data.index.tolist()[-1]
        for i in data_res['miRNA'].tolist():
            # Замена для поиска (из-за функции Target_remake)
            subs = re.sub('miR-', '', i)
            find = re.search(r'\S*{}\S*'.format(subs),
                             names).group().replace(',', '')
            # все строки с этой микроРНК
            indexes = data[data['miRNA'] == find].index.tolist()
            for j in indexes:
                data.loc[in_max + ind] = data.loc[j].tolist()
                data.loc[in_max + ind, 'miRNA'] = i
                ind += 1
        # Выделение только нужных микроРНК из полученного датафрейма
        data = data[data['miRNA'].isin(data_res['miRNA'].tolist())]
        data = data.merge(data_res, how='outer')
        data.sort_values(['miRDB score', 'miRNA'], inplace=True,
                         ascending=False)

        print(np.unique(data.isnull()))  # Смотрим, все ли строки заполнены
        data_proteins = pd.DataFrame(pd.read_csv(
            'Proteins/{}_proteins.csv'.format(protein), sep=','
        ))

        # Значения стартового и последнего нуклеотида сайта связывания
        start = data['UTR_start'].tolist()
        stop = data['UTR_end'].tolist()

        # loc_gene = data_proteins['Locus'].tolist()
        # loc_prot = data_proteins['Protein Name'].tolist()
        # Добавляем новые столбцы
        data['Locus_start'] = ''
        data['Locus_end'] = ''
        data['Protein_start'] = ''
        data['Protein_end'] = ''

        # for i in range(len(start)):
        #     print(start[i], stop[i], loc_prot[i], loc_gene[i])
        #     data.loc[np.where(data['UTR_start'].isin(
        #         range(start[i], stop[i] + 1)))[0], [
        #             'Locus_start', 'Protein_start']] = [
        #                 loc_gene[i], loc_prot[i]]
        #     data.loc[np.where(data['UTR_end'].isin(
        #         range(start[i], stop[i] + 1)))[0], [
        #             'Locus_end', 'Protein_end']] = [
        #                 loc_gene[i], loc_prot[i]]

        for i in start:  # Смотрим первый нуклеотид сайта связывания
            ind = data[data['UTR_start'] == i].index.tolist()
            for k in ind:
                for j in range(len(data_proteins)):  # Для каждого индекса
                    sta = data_proteins.loc[j, 'Start']
                    end = data_proteins.loc[j, 'Stop']
                    if i in range(sta, end + 1):
                        data.loc[k, 'Locus_start'] = data_proteins.loc[
                            j, 'Locus']
                        data.loc[k, 'Protein_start'] = data_proteins.loc[
                            j, 'Protein Name']

        for i in stop:  # Смотрим последний нуклеотид сайта связывания
            ind = data[data['UTR_end'] == i].index.tolist()
            for k in ind:
                for j in range(len(data_proteins)):  # Для каждого индекса
                    sta = data_proteins.loc[j, 'Start']
                    end = data_proteins.loc[j, 'Stop']
                    if i in range(sta, end + 1):
                        data.loc[k, 'Locus_end'] = data_proteins.loc[
                            j, 'Locus']
                        data.loc[k, 'Protein_end'] = data_proteins.loc[
                            j, 'Protein Name']

        save_top(data, "Results/locus_{}".format(string))  # Сохраняем
