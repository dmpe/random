# 2016 USA Presidential debate - Preparition of a sample of tweets

## Goal:

Being a student research assistant for [SAWI](http://www.wi2.fau.de/teaching/master/master-courses/sawi/) course during autumn 2017/2018 at FAU, the task was to prepare `2016 USA Presidential debate` dataset that could have been passed to the students, for their analysis.

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

We have used TWARC from <https://github.com/DocNow/twarc>. 

#### 1.1 Configure

First, get Twitter DEV API Keys from <https://developer.twitter.com/en/apply-for-access>:
Then, place them into:
```
twarc configure
```

After that, 
```
twarc hydrate first-debate.txt > all_first_tweets.jsonl
```

It takes hours...

#### 1.5 Step - Split data into manageble junks

Why? Well, because the original 13.5 GB `jsonl` file will be hard to read in any programm. So dont try R + limited RAM!
You could use for that <https://stedolan.github.io/jq/>. 

**Alternatively**, you could split txt file into multiple files and then apply previous `twarc` command.

Something like

```
split -b 1M -d  first-debate.txt file 
```

### 2. Step - Convert to CSV

Why? Because jsonl files are hard to work with. 

Execute for each file, depending on your PC and twarc itself:

```
python 2jsonl.py xaa.jsonl -o xaa.csv

OR

python3 2jsonl.py xaa.jsonl -o xaa.csv
```

You can also try:

```
python 2csv_original.py xae -o xae.csv
```

CSV delimiter will be ";"

Overall, this will create very large CSV files at around 250 MB. And we still need samples of those.

Again, alternatively, you can take one large JSONL file and convert it to one large CSV file which you can later split.

### 3. Step

Analyse Data in order to understand time when tweets have been published ;)

E.g. 

```
head -n 5 xae.csv
```

The outcome:
```
xaa -> before debate: from 12 PM EST till 18:30 EST

xab -> before debate: from 18:30 EST till 21:00 EST 

(first debate was from 21:00 till 22:35)

xac -> during debate: from 20:47 EST till 22:40 EST

xad -> after  debate: from 22:40 EST till 01:20 AM EST

xae -> after  debate: from 01:20 AM EST till 06:20 AM EST

xaf -> after  debate: from 06:20 AM EST till 09:40 AM EST

xag ->  .... (rest)
```
### 4. Step - Split large CSVs into smaller samples

Use R script `process_data.R` to apply proper formatting.

You can also go faster (but not more reliable), where you would on **Ubuntu** (and in case of xa{a,b}.csv 250MB files), execute:

```
shuf -n 2500 xaa.csv > xaa_sample_2500.csv
shuf -n 2500 xab.csv > xab_sample_2500.csv
```

Having those, only then you use `process_data.R` which contains something along the lines

```
mt <- fread("xaa.csv") # or xaa_sample_2500.csv directly
mt <- mt[sample(.N, 2500)]
fwrite(mt, "xaa_sample_2500.csv", sep = ";")
```

### 5. Step - In any case, you need to combine files from previous R scipt

On **Windows**, type commands like:

```
type xad_sample_1500.csv xae_sample_2500.csv xag_sample_1000.csv> after_sample_5000.csv

type xaa_sample_2500.csv xab_sample_2500.csv > before_random_sample_5000.csv

type after_sample_1000.csv xae_sample_1000.csv xaf_sample_2500.csv xag_sample_2500.csv > after_random_sample_5000.csv
xaf_sample_1500.csv 

# combine 2500*2 tweets from the time before the debate into 5000 pieces
type before_sample_2500_a.csv before_sample_2500_b.csv > before_sample_5000.csv
```

## Some research before

Download tweets manually, looking for tweets that include specific `#hastags`. Then store them in the database from which you can then query them. See that folder and Python Notebooks.




