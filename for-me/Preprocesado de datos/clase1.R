### Importar bibliotecas 
# packages <- c("magrittr", "tidyverse", "readr")
# lapply(packages, library, character.only = TRUE)

library(magrittr)
library(tidyverse)
library(readr)

### Importar datos
dataset <- read_csv("Preprocesado de datos/Data.csv")

### Sustituir NA por la media de la columna
dataset <- dataset %>% transform(Age = ifelse(is.na(Age), mean(Age,na.rm = T), Age),
                                 Salary = ifelse(is.na(Salary), mean(Salary, na.rm = T), Salary))

## Categoricas a factores 

dataset <- dataset %>% transform(Country = factor(Country, levels = c("France", "Spain", "Germany"), labels = c(1,2,3)), 
                                 Purchased = factor(Purchased, levels = c("No", "Yes"), labels = c(0,1)))


## Split train y test

smp_siz <-  floor(0.8*nrow(dataset))
set.seed(123)
train_sample <-  sample(seq_len(nrow(dataset)), size = smp_siz)
train  <- dataset[train_sample,]
test <- dataset[-train_sample,]

## Escalado de variables 

train[,2:3] <- scale(train[,2:3])
test[,2:3] <- scale(test[,2:3])



