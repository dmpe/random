# 2016 USA Presidential debate - Preparition of a sample of tweets

## Goal:

Being a student research assistant for [SAWI]() course during autumn 2017/2018 at FAU, the task was to prepare `2016 USA Presidential debate` dataset that could have been passed to the students, for their analysis.

**Data Source in question:** <https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FPDI7IN>

**Specifically**, the first presidential debate in the USA that was held in 2016.
<https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/PDI7IN/AGYMSC&version=3.0>. See its `Readme` file as well.

### Note for myself 
See that [MEGA folder](https://mega.nz/#F!qxNThASR) for the whole twitter dataset (~15 GB; Log file ~ 200 MB). You have to ask me for the key to see files!

## Tasks:

The final idea was to have 5 groups and provide each of them slightly different dataset according to when people have tweeted about it, i.e. wheather it was before, during or after the debate. 

In summary, the objective would be to gather 5 samples, each of 5000 tweets:

- 1 sample **before** the debate has began

- 3 samples **during** the debate

- 1 sample **after** the debate

<http://rpubs.com/F789GH/USAPresidentialTweets> shows some statistics for the final CSV samples. See `RPubs` folder for more.

### 1. Step - Get data

Download tweets because that `.txt` file will just contain the Tweet IDs. Not the whole content of the tweet itself. 

### 2. Step - Convert to CSV

uses ";" as separator

Execute:

```
python 2jsonl.py xaa.jsonl -o xaa.csv
2csv.py xae -o xae.csv
```

### 2 Step
Analyse Data ;)

R' data.table

xaa -> before debate: from 12 PM EST till 18:30 EST

xab -> before debate: from 18:30 EST till 21:00 EST 

(first debate was from 21:00 till 22:35)

head -n5 

xac -> during debate: from 20:47 EST till 22:40 EST

xad -> after  debate: from 22:40 EST till 01:20 AM EST

xae -> after  debate: from 01:20 AM EST till 06:20 AM EST

xaf -> after  debate: from 06:20 AM EST till 09:40 AM EST

xag ->  .... (rest)


### pure (semi-)random sample

**Unix:**

xaa + xab: shuf -n 2500 xab.csv > xab_sample_2500.csv

-------> Merge 2 files

(see process_data.R)

```
mt <- fread("xaa.csv")
mt <- mt[sample(.N, 2500)]
fwrite(mt, "xaa_sample_2500.csv", sep = ";")
```

**Windows OS:** 

type xaa_sample_2500.csv xaa_sample_2500.csv > before_random_sample_5000.csv
type after_sample_1000.csv xae_sample_1000.csv xaf_sample_2500.csv xag_sample_2500.csv > after_random_sample_5000.csv
xaf_sample_1500.csv 

type before_sample_2500_a.csv before_sample_2500_b.csv > before_sample_5000.csv
type xad_sample_1500.csv xae_sample_2500.csv xag_sample_1000.csv> after_sample_5000.csv


### Some research

1. Download tweets manually, looking for tweets that include specific `#hastags`



