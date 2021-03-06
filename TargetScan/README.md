### Так как работа над статьей продолжается - создано две ветки: _before_noexp_ - ветка, созданная для сдачи дз (точно рабочая =D), _master_ - текущая версия работы
# Анализ предсказанных сайтов связывания микроРНК по miRDB v6.0 и TargetScan v7.2 у семи коронавирусов: SARS-CoV-2, SARS-CoV, MERS-CoV, HCoV-OC43, HCoV-HKU1, HCoV-229E, HCoV-NL63
## Данные о последовательностях и белках получены с сайта ncbi.nlm.nih.gov (Базы данных GenBank, Nucleotide и Genome)
## Предсказания выполнены с помощью Custom Mode miRDB и Perl скриптов TargetScan
# Файлы:
1. Results - основная папка с результатами сравнения (пересечения трех датафреймов и анализ сайтов связывания)
2. _With_lungs_comparison.ipynb_ - основной ноутбук с анализом четырех выравненных и трех невыравненных геномов
3. _Without_expression.ipynb_ - сравнивание предикшенов семи невыравненных геномов без учета экспрессии в легких человека
4. _For_St_Results_noexp.ipynb_ - оценка консервативности микроРНК, полученных из ноутбука _Without_expression.ipynb_
5. _Predictions.py_ - файл с аннотированными функциями (используется как модуль)
6. _lungs_expression.txt_ - таблица экспрессии микроРНК в легких человека (из TCGA-LUAD project с log-трансформацией RPM). Содержит 47 столбцов: первый - название микроРНК, остальные соотносятся с 46 нормальными легкими человека и экспрессией микроРНК в них
7. _TargetScan_Predict.txt_ - Предсказания TargetScan по выравненным последовательностям для четырех коронавирусов (SARS-CoV-2, SARS-CoV, MERS-CoV, HCOV-OC43)  
8. _TargetScan_predictions_ - педсказания TargetScan для семи невыравненных геномов коронавирусов
(выдержка из Readme_TargetScan по столбцам:  
_The sample output file has a headers that names each column  
	GeneID - name/ID of gene (from UTR input file)  
	miRNA_family_ID - name/ID of miRNA family (from miRNA input file)  
	species_ID - name/ID of species (from UTR input file)  
	MSA_start - starting position of site in aligned UTR (counting gaps)  
	MSA_end - ending position of site in aligned UTR (counting gaps)  
	UTR_start - starting position of site in UTR (not counting gaps)  
	UTR_end - ending position of site in UTR (not counting gaps)  
	Group_ID - ID (number) of site(s) (same gene, same miRNA) that overlap  
	Site_type - type of site in this species (m8 [7mer-m8], 1a [7mer-1A], or m8:1a  [8mer])  
	miRNA in this species - if "x", then this miRNA has been annotated in this species  
	Group_type - type of this group of sites; if 'Site_type' in a 'Group_ID' is  heterogeneous, "weakest" type of the group is used  
	Species_in_this_group - list of species names/IDs in which this site is found  
	Species_in_this_group_with_this_site_type - for hetergeneous groups only  
	ORF_overlap - If site in the UTR sequence is lowercase (indicating ORF overlap),  this will be set to 1.  Typical UTR sites have a value of 0._)  
9. _miRDB/*_ - отдельные предсказания по каждому из семи вирусов (_столбцы: порядковый номер в топе, Название микроРНК, TargetScore,_)
10. _Graphs/*_ - отдельные скрипты для графиков и сохраненные картинки для них
11. _Intermediate_results/*_ - промежуточные результаты, отсортированные по экспрессии или TargetScore
12. _Proteins/*_ - Данные о расположении генов белков
13. _TargetScan_7/*_ - perl-скрипт, а также входные файлы, для предсказывания при помощи TargetScan 

### Данный анализ выполнен в рамках написания статьи "A potential role of host miRNAs in host-virus interplay during coronavirus infection"
