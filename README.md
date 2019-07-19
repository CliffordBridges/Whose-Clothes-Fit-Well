# Whose-Clothes-Fit-Well
## Team members: [Clifford Bridges](https://github.com/CliffordBridges) and [Allan Kim](https://github.com/allankim4)

## Executive summary:

The goal of this project is to perform tests and identify statistical significance on the datasets acquire. 
Listed below are the companies where data was indirectly taken from. 
(Data sets were retreived from kaggle) 

![Rent_The_Runway logo](images/rtr_logo.jpeg)
![ModCloth logo](images/modcloth.png)

## Contents

- [Introduction](#Introduction)
    - [Problem statement](#Problem-statement)
    - [Dataset](#Dataset)
- [Analysis](#Analysis)
    - [Data Cleaning](#Data-Cleaning)
    - [Exploratory Data Analysis](#Exploratory-Data-Analysis)
    - [Statistical Tests](#Statistical-Test)
- [Responsibilties](#Responsibilities)
- [Summary of Files](#Files-summary)


## Introduction

### Dataset
Downloaded user review data from [kaggle](https://www.kaggle.com/rmisra/clothing-fit-dataset-for-size-recommendation). 
This data includes [Rent The Runway](https://www.renttherunway.com/) data and [ModCloth](https://www.modcloth.com/) data on user reviews, each in a separate file.

Rent The Runway (RTR) data includes reviews from November 3, 2010 through January 8, 2018. 
We do not have dates of reviews for ModCloth, but the reviews are from before August 21, 2018, when the dataset was uploaded to kaggle. 
We take these data to be a sample of the population of all reviews on the respective sites.


## Analysis

### Data Cleaning

The data encompasses reviews of garments on either site. 
These reviews were submitted by registered users of the site, and therefore have metrics associated with the user who submitted the review. 
Because of this, there is often small percentages of ```NaN``` values for characteristics of the reviewers. 
For example, in RTR file, less than 2\% of values from the columns explored were ```NaN``` types. 

These sites primarily focus on users who identify as a woman, therefore features like bra size are common. 
From independent experience with the site, it is not impossible that a user who identifies as a man reviewed a garment which would likely create an data point inconsistent with otherwise similarly grouped users. 
For example, a user's weight may be very different from other users with the same height. 
We feel comfortable using this data, as it still reflects the population of users at large.

There were several features engineering steps, however. 
For example, the values in the RTR data column, ```bust size```, were strings, from which we created two columns ```band_size``` and ```cup_size``` where ```band_size``` values were ints and ```cup_size``` values were strings. 
Also, the ModCloth data contained ```waist``` and ```hip``` data, but not waist-to-hip ratio, so we created a new column with this information. 
All cleaning and feature engineering is described in the RTR_DataCleaning notebook.


### Exploratory Data Analysis

The [Technical Notebook](Technical_Notebook.ipynb) contains all of the analysis for both data sets. 
Note that the technical notebook comments out the code used to save the figures to a separate file. 
The reader can uncomment to save the figure locally.

We aim to be clear when desribing the _reviewers_ on either site, who may be different from the population of _users_ on either site. 
It may be possible that users who review are inherently different different from users who do not review. 
We make no claims about users who have not submitted a review. 


Several characterisitcs of the data stood out during EDA. 
We chose to focus on height and waist to hip ratio of ModCloth reviewers, and body type for RTR reviewers. 
All of these features are self-identified by the user, and in particular, may not match what is expected based on other user features such as weight or bra size. 
As an example, our the technical notebook shows that users who self-identified as "full bust" who also self-identified as wearing a A cup had a lower average rating on garments. 
On the other hand, users who self-identified as "straight and narrow" who also self-identified as wearing a DDD/E cup had a higher average rating on garments. 
Although we currently do not attempt to analyze these differences, we acknowledge that self-identification may affect our results.


### Statistical Tests

In the Modcloth data set, we classified "high" reviews as those which gave ratings of 4 or 5 (out of 5), rated the fit as "fit" (instead of "small" or "large") and rated the length as "just right" (instead of "slightly long", or "slightly short"). 
We hypothesized that the average height of reviewers with high reviews is different than the average height of all reviewers. 
The high review ratings were not normally distributed, so we used bootstrapping to create a normally distributed sampling distribution. 
We conducted a two-tailed Welch's $t$-tests with null hypothesis that the two average heights are equal, and alternative hypothesis that they were not equal. 
We found significant evidence to reject the null hypothesis with alpha set to 0.05.

We also tested wether hip-to-waist ratio has an effect on high reviews. 
We partitioned the waist-to-hip ratio based on the table found on this [MedicalNewsToday article](https://www.medicalnewstoday.com/articles/319439.php). 
We adjusted the table as follows: 

|Health Risk|Men|Women|
|---|---|---|
|Low|lower than 0.96|lower than 0.80|
|Moderate|0.96 - 1.0|0.80 - 0.85|
|High|higher than 1.0|higher than 0.85|

The data in each case were not normally distributed, so we used bootstrapping to create sampling distributions that were closer to normal. 
We then used a two-tailed Welch's $t$-test with an alpha of 0.05 in each of three cases where the null hypothesis was the average review ratings for reviewers with the given health risk indicator are the same as those general population, and the alternative hypothesis was the average review ratings for reviewers with the given health risk indicator are not the same as those general population. 
In each case we failed to reject the null hypothesis.

In the RTR data set, we classified "high" reviews as those which gave ratings or 9 or 10 (out of 10). 
We hypothesized that users with certain body types would have different proportions of high reviews than average depending on the dress they were reviewing. 
More specifically, we hypothesized that users who self-identified as "petite" have a higher than average proportion of high ratings than average for dress 174086, and that users who self-identified as "apple" have a lower than average proportion of high ratings than average for dress 126335. 
We used a proportions test for both hypotheses. 
Our null hypotheses that the stated proportions were equal, and alternative hypotheses that the proportions were as stated above. 
At an alpha level of 0.05, we found significant evidence to reject the null hypothesis in both cases.

We also tested whether users who self-identify as "hourglass" rate dresses differently than users who self-identify as "athletic". 
We identified the dresses with the top 5 highest number of reviews, and for each dress tested the null hypothesis that athletic body type reviewers have the same average rating as hourglass body type reviewers. 
The data in each case were not normally distributed, so we used bootstrapping to create sampling distributions that were closer to normal. 
We then used a two-tailed Welch's $t$-test with an alpha of 0.05, and in four out of the five dress found significant evidence to reject the null hypothesis.

## Responsibilities

With two datasets for this project, We decided to assign each a dataset and conduct our own test and exploration. 
Throughout the testing and exploration of the data, the workloads were similar aside from subject matter expert advise/insight burden was given to Clifford.

The presentation file was a joint combined effort.

## Summary of Files

The cleaned files ([cleaned RTR data](rtr_clean.csv) and [cleaned ModCloth data](modcloth_finaldata.json)) were the final data sets used for analysis.

Images folder contains images used for the presentation pdf. 
Images of graphs were created during EDA to help understand what the data represented, or after anaylsis to highlight statisticlly significant findings.

RTR_DataCleaning notebook entails the process of cleaning the data.
