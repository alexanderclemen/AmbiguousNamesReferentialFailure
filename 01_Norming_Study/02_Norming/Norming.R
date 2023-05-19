getwd()
setwd("C:/Users/alexa/Documents/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming")

library(dplyr)
library(purrr)
library(tidyverse) # includes ggplot and tidyr
library(lme4)
library(tibble)# to make the index also a column
library(MASS)

##### reading all files####

VP01 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP01.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP02 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP02.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP03 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP03.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP04 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP04.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP05 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP05.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP06 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP06.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP07 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP07.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP08 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP08.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP09 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP09.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP10 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP10.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP11 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP11.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP12 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP12.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP13 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP13.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP14 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP14.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP15 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP15.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP16 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP16.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP17 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP17.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP18 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP18.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP19 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP19.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP20 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP20.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP21 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP21.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP22 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP22.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP23 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP23.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP24 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP24.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP25 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP25.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP26 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP26.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP27 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP27.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP28 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP28.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP29 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP29.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP30 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP30.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP31 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP31.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP32 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP32.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP33 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP33.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP34 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP34.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')
VP35 <- read.csv2('~/02_study/duesseldorf/BA_Linguistik/09_BBA_Bachelorarbeit/02_daten/01_Norming_Study/02_Norming/VP35.csv', header = T, sep = ';', na.strings = c('NA', 'na', ''), dec = ',')

##### make a list of all VPs and their names ####

# [...]

##### anonymisieren ####

VP01$participant <- "VP01"
VP02$participant <- 'VP02'
VP03$participant <- 'VP03'
VP04$participant <- 'VP04'
VP05$participant <- 'VP05'
VP06$participant <- 'VP06'
VP07$participant <- 'VP07'
VP08$participant <- 'VP08'
VP09$participant <- 'VP09'
VP10$participant <- 'VP10'
VP11$participant <- 'VP11'
VP12$participant <- 'VP12'
VP13$participant <- 'VP13'
VP14$participant <- 'VP14'
VP15$participant <- 'VP15'
VP16$participant <- 'VP16'
VP17$participant <- 'VP17'
VP18$participant <- 'VP18'
VP19$participant <- 'VP19'
VP20$participant <- 'VP20'
VP21$participant <- 'VP21'
VP22$participant <- 'VP22'
VP23$participant <- 'VP23'
VP24$participant <- 'VP24'
VP25$participant <- 'VP25'
VP26$participant <- 'VP26'
VP27$participant <- 'VP27'
VP28$participant <- 'VP28'
VP29$participant <- 'VP29'
VP30$participant <- 'VP30'
VP31$participant <- 'VP31'
VP32$participant <- 'VP32'
VP33$participant <- 'VP33'
VP34$participant <- 'VP34'
VP35$participant <- 'VP35'

# fill missing data i.e. VPs sex, gender, Age and Muttersprache
VP01 <- fill(VP01, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP02 <- fill(VP02, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP03 <- fill(VP03, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP04 <- fill(VP04, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP05 <- fill(VP05, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP06 <- fill(VP06, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP07 <- fill(VP07, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP08 <- fill(VP08, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP09 <- fill(VP09, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP10 <- fill(VP10, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP11 <- fill(VP11, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP12 <- fill(VP12, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP13 <- fill(VP13, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP14 <- fill(VP14, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP15 <- fill(VP15, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP16 <- fill(VP16, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP17 <- fill(VP17, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP18 <- fill(VP18, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP19 <- fill(VP19, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP20 <- fill(VP20, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP21 <- fill(VP21, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP22 <- fill(VP22, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP23 <- fill(VP23, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP24 <- fill(VP24, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP25 <- fill(VP25, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP26 <- fill(VP26, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP27 <- fill(VP27, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP28 <- fill(VP28, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP29 <- fill(VP29, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP30 <- fill(VP30, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP31 <- fill(VP31, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP32 <- fill(VP32, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP33 <- fill(VP33, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP34 <- fill(VP34, c(slider_biologicalSex_response, slider_response), .direction = c('up'))
VP35 <- fill(VP35, c(slider_biologicalSex_response, slider_response), .direction = c('up'))

VP01 <- fill(VP01, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP02 <- fill(VP02, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP03 <- fill(VP03, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP04 <- fill(VP04, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP05 <- fill(VP05, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP06 <- fill(VP06, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP07 <- fill(VP07, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP08 <- fill(VP08, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP09 <- fill(VP09, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP10 <- fill(VP10, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP11 <- fill(VP11, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP12 <- fill(VP12, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP13 <- fill(VP13, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP14 <- fill(VP14, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP15 <- fill(VP15, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP16 <- fill(VP16, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP17 <- fill(VP17, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP18 <- fill(VP18, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP19 <- fill(VP19, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP20 <- fill(VP20, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP21 <- fill(VP21, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP22 <- fill(VP22, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP23 <- fill(VP23, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP24 <- fill(VP24, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP25 <- fill(VP25, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP26 <- fill(VP26, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP27 <- fill(VP27, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP28 <- fill(VP28, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP29 <- fill(VP29, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP30 <- fill(VP30, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP31 <- fill(VP31, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP32 <- fill(VP32, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP33 <- fill(VP33, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP34 <- fill(VP34, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))
VP35 <- fill(VP35, c(slider_Age_response, slider_Muttersprache_response), .direction = c('down'))


#appending 
rawdf <- rbind(VP01, VP02, VP03, VP04, VP05, VP06, VP07, VP08, VP09, VP10, VP11, VP12, VP13, VP14, VP15, VP16, VP17, VP18, VP19, VP20, VP21, VP22, VP23, VP24, VP25, VP26, VP27, VP28, VP29, VP30, VP31, VP32, VP33, VP34, VP35)
dim(rawdf)
# View(rawdf)

#############################
##### clean the data set ####
#############################

# delete unnecessary columns
glimpse(rawdf)
refdf1 <- rawdf[,-c(1:4,6:8,10:21,28:35,38:39,42,44:46,48:50)]

# renaming header
glimpse(refdf1)

refdf2 <- rename(refdf1, 
                     Age = slider_Age_response, 
                     L1 = slider_Muttersprache_response,
                     VP = participant,
                     BiologicalSex = slider_biologicalSex_response,
                     GenderIdentity = slider_response,
                     ID = Column1,
                     RT = slider_Trial_rt,
                     Response = slider_Trial_response,
                     Trials_ID = trials_thisN,
                     PsychoPy_ID = trials_thisIndex
                     )
glimpse(refdf2)





#change the order of the variables in the data set
refdf2 <- refdf2 %>% 
  select(ID, PsychoPy_ID, Trials_ID, Name, Response, expectedSex, expectedSex2, RT, Freq, VP, Age, L1, BiologicalSex, GenderIdentity)
glimpse(refdf2)

# change the class of a variable

refdf2$expectedSex <- as.factor(refdf2$expectedSex)
refdf2$expectedSex2 <- as.factor(refdf2$expectedSex2)
refdf2$VP <- as.factor(refdf2$VP)
refdf2$BiologicalSex <- as.factor(refdf2$BiologicalSex)
refdf2$GenderIdentity <- as.factor(refdf2$GenderIdentity)

refdf2$Response <- as.numeric(refdf2$Response)
refdf2$Age <- as.numeric(refdf2$Age)

glimpse(refdf2)

#delete buffer (Gudrun, Uwe, and Alex)
dim(refdf2)
refdf3 <- refdf2[!(refdf2$Name=="Gudrun" | refdf2$Name=="Uwe" | refdf2$Name=="Alex"),]
dim(refdf3)

# delete NA rows
refdf4<-refdf3[-which(apply(refdf3,1,function(x)all(is.na(x)))),]

# adjusting age
refdf4$Age <- refdf4$Age+16

# if all is cleaned up this is the final dataframe
df <- refdf4

# change "d" to "n"
levels(df$expectedSex)
df$expectedSex<-recode_factor(df$expectedSex, d = "n")

#playing around with standard deviations

df$RT > (mean(df$RT)+14.07749)
           
sd(df$RT)*3

summary(df)

unique(df$Name)

# 
####### play zone ###########
#############################

#### reshape data from long to wide ####

mean(df$Age)
range(df$Age)

glimpse(df)
order(df)
df <- df[order(df$ID),]

glimpse(df)
data_Name_by_Response <- df[,c("VP", "Name", "Response")]

wide_df <- data_Name_by_Response %>% 
  pivot_wider(names_from = Name, values_from = Response)


# View(wide_df)
glimpse(wide_df)
# mean(wide_df$Mia)
MeanResponse<-colMeans(wide_df[-1])
MeanResponse<-as.data.frame(MeanResponse)

MedianResponse<-apply(wide_df[-1], 2, median)
MedianResponse<-as.data.frame(MedianResponse)


MeanResponse <- tibble::rownames_to_column(MeanResponse, "Name")
MedianResponse <- tibble::rownames_to_column(MedianResponse, "Name")

MeanResponse <- rename(MeanResponse, 
                       Mean = MeanResponse)
MedianResponse <- rename(MedianResponse, 
                       Median = MedianResponse)

glimpse(MeanResponse)

## add the means to the main dataframe

sort(MeanResponse$Name)
sort(MedianResponse$Name)
df$Rating_Mean <- rep(MeanResponse$Mean, each = length(unique(df$VP)))
df$Rating_Median <- rep(MedianResponse$Median, each = length(unique(df$VP)))

## do the same with SDs


#create standard deviations
SDs <-wide_df[-1] %>% summarise_if(is.numeric, sd)
SDs<-t(SDs)
SDs<-(as.data.frame(SDs))

#rename
SDs <- rename(SDs, 
                 Norm.SDs = V1) 

#append
df$Rating_SD <- rep(SDs$Norm.SDs, each = length(unique(df$VP)))



## lets ggplot the new data


#this fixes the illustration such that the order is m n f
df$expectedSex <- factor(df$expectedSex,
                         levels = c("m", "n", "f"))

ggplot(data = df,mapping = aes(x = Rating_Mean,y = Response, color = expectedSex, alpha = 0.95))+
  geom_jitter(height  = .25)+
  facet_wrap(~VP)+
  theme_bw()+
  labs(x="Names sorted by Rating Mean",
       y="Subject Rating")

ggsave("jitter_VPResponse_Norming.pdf", width = 20, height = 15, units = "cm")


# i will add now the gender to the df
expectedSex <- c(rep("n", times = 41),
                    rep("f", times = 50),
                    rep("m", times = 52))
MeanResponse$expectedSex <- expectedSex
MeanResponse$expectedSex <- as.factor(MeanResponse$expectedSex)

glimpse(MeanResponse)

#make background and rectangles
data_background1 <- df[,c("Name", "Rating_Mean", "Rating_Median")]
rectM <- subset(df, expectedSex == "m")
rectN <- subset(df, expectedSex == "n")
rectF <- subset(df, expectedSex == "f")

ggplot(data = df, aes(x = Rating_Mean, fill = expectedSex))+
  geom_histogram(data = data_background1, fill = "lightgrey", binwidth = 0.2)+
  geom_histogram(binwidth = 0.2)+
  geom_rect(data = rectM, aes(xmin=1, xmax=2, ymin=0, ymax=Inf, fill=expectedSex), alpha=0.006) +
  geom_rect(data = rectN, aes(xmin=3, xmax=5, ymin=0, ymax=Inf, fill=expectedSex), alpha=0.003) +
  geom_rect(data = rectF, aes(xmin=6, xmax=7, ymin=0, ymax=Inf, fill=expectedSex), alpha=0.006) +
  facet_wrap(~expectedSex)+
  labs(x = "Rating Means, Facets by expected Gender", y = "Count")+
  xlim(1,7)+
  theme_bw()+
  theme(legend.position = "none")

ggsave("histogram_VPResponse_Norming.pdf", width = 20, height = 10, units = "cm")


## also with the median


ggplot(data = df, aes(x = Rating_Median, fill = expectedSex))+
  geom_histogram(data = data_background1, fill = "lightgrey", binwidth = 0.2)+
  geom_histogram(binwidth = 0.2)+
  geom_rect(data = rectM, aes(xmin=1, xmax=2, ymin=0, ymax=Inf, fill=expectedSex), alpha=0.006) +
  geom_rect(data = rectN, aes(xmin=3, xmax=5, ymin=0, ymax=Inf, fill=expectedSex), alpha=0.003) +
  geom_rect(data = rectF, aes(xmin=6, xmax=7, ymin=0, ymax=Inf, fill=expectedSex), alpha=0.006) +
  facet_wrap(~expectedSex)+
  labs(x = "Rating Median, Facets by expected Gender", y = "Count")+
  xlim(0.8,7.2)+
  theme_bw()+
  theme(legend.position = "none")


ggsave("histogram_VPResponse_Norming_Median.pdf", width = 20, height = 10, units = "cm")


# frequency plot is not as good as the histogram plot
# ggplot(MeanResponse,
#        mapping = aes(x = Mean,
#                      color = expectedSex))+
#   geom_freqpoly(binwidth = .2,
#                 size = 1,
#                 alpha = .6)


## area plot does not seeem too good fir this research ###

# ggplot(MeanResponse,
#        mapping = aes(x = Mean,
#                      fill = expectedSex))+
#   geom_area(stat = "bin",
#             binwidth = .1,
#             size=1,
#             alpha = .5)


### Make groups now ####
# variables have to pass both Rating_Mean and Rating_Median

Names_m1 <- subset(df, Rating_Mean < 3
                   & Rating_Median < 3.1
                   )
#only interesting columns
Names_m1<-Names_m1[,c("Name", "Rating_Mean", "Rating_SD", "Rating_Median")]
#eliminate duplicates
Names_m1<-distinct(Names_m1)
# rearante list
Names_m1<-arrange(Names_m1, Rating_Mean, Rating_SD)
#add a Name_Class column
Names_m1$Name_Class<-"m"
dim(Names_m1)

## neutral names
Names_n1 <- subset(df, 
                   (Rating_Mean > 2.5) & (Rating_Mean < 5.5) & 
                     ((Rating_Median > 2.9) & (Rating_Median < 5.1))
                   )
#only interesting columns
Names_n1<-Names_n1[,c("Name", "Rating_Mean", "Rating_SD", "Rating_Median")]
#eliminate duplicates
Names_n1<-distinct(Names_n1)
# rearante list
Names_n1<-arrange(Names_n1, Rating_Mean, Rating_SD)
#add a Name_Class column
Names_n1$Name_Class<-"n"
dim(Names_n1)

##female list
Names_f1 <- subset(df, Rating_Mean > 5
                     & Rating_Median > 5.9)
Names_f1<-Names_f1[,c("Name", "Rating_Mean", "Rating_SD", "Rating_Median")]
Names_f1<-distinct(Names_f1)
Names_f1<-arrange(Names_f1, -Rating_Mean, Rating_SD)
#add a Name_Class column
Names_f1$Name_Class<-"f"
dim(Names_f1)

##### output ####
write.csv2(Names_m1, file = "Norming_Names_m.txt")
write.csv2(Names_n1, file = "Norming_Names_n.txt")
write.csv2(Names_f1, file = "Norming_Names_f.txt")


# enough of this i will now use the full dataframe

  Norming_Names_df<-df[,c("Name", "expectedSex", "Rating_Mean", "Rating_SD", "Rating_Median")]
  Norming_Names_df<-distinct(Norming_Names_df)
  Norming_Names_df<-arrange(Norming_Names_df, Rating_Mean, Rating_SD)

write.csv2(Norming_Names_df, file = "Norming_Names_df.txt")

# make a figure like in Kennison & Troofe 2003: 360
df$Rating_SD
df$Rating_Mean
df$Name
df$expectedSex

ggplot(df, aes(x = Rating_Mean, y = Rating_SD))+
  geom_rect(data = df, aes(xmin=1, xmax=2, ymin=0, ymax=Inf, fill = "blue"), alpha=0.006) +
  geom_rect(data = df, aes(xmin=3, xmax=5, ymin=0, ymax=Inf, fill = "green"), alpha=0.003) +
  geom_rect(data = df, aes(xmin=6, xmax=7, ymin=0, ymax=Inf, fill = "red"), alpha=0.006)+
  geom_point(aes(color = expectedSex, shape = expectedSex)) +
  scale_x_continuous("Mean Rating", labels = c(1,2,3,4,5,6,7), breaks = c(1,2,3,4,5,6,7))+
  scale_y_continuous("Standard Deviation of Rating")+
  theme_bw()

ggsave("point_meanBySd_Norming.pdf", width = 20, height = 10, units = "cm")
