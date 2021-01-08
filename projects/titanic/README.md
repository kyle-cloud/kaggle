# 1 Baseline

## 1.1 load data
    pd.read_csv()
## 1.2 analise data
    1. train_set.head()
![head](./images/head.png)
    
    2. train_set.info()
![info](./images/info.png)

    3. explore the relationships between all the other features and the target 'Survival'
        e.g. train['Survived'].value_counts()
             sns.barplot(x = 'Pclass', y = 'Survived', data = train)
![survival](./images/survival.png)
![pclass](./images/pclass.png)

## 1.3 process data
    1. create new features
        a. Name -> Surname, Title
        b. Cabin -> Deck
        c. Sibsp + Parch + 1 -> FamilySize
![Title](./images/Title.png)

    2. fill missing values(Age, Embarked and Fare)
        a. Age: (Sex, Title, Parch, Pclass) + RandomForestRegressor -> Age
        b. Embarked(missing two): Groupby(Pclass, Embarked) -> Fare.median -> Embarked
        c. Fare(missing one): (Pclass, Embarked) -> Fare.median
![PclassEmbarked](./images/PclassEmbarked.png)

    3. transform features
        a. select features:
            all_data = all_data[['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Surname', 'Title', 'Deck', 'FamilySize', 'TicketGroup']]
        b. transform features:
            all_data = pd.get_dummies(all_data)
        c. split into train and test

## 1.4 Build Model
    1. optimize parameters: automatically select the optimal parameters using grid search
    2. train model: RandomForestClassifier
    3. estimate model: 10-fold cross validation -> CV Score : Mean - 0.827166 | Std - 0.0396002

## 1.5 Predict Data


# 2 Optimization
