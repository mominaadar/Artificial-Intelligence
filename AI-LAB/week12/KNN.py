
# ------------ Momina Atif Dar - P18-0030 --------------

import pandas as pd
from collections import Counter
Counter()


data = pd.read_csv('dataset.csv')


# isolating necessary columns
cols = [0,3,4,5,6]
data = data.iloc[:,cols]


# to fill up empty spaces with mean of the column
mass_mean = data['mass'].mean()
height_mean = data['height'].mean()

# to fill up empty spaces with data
data.loc[17] = pd.Series({'fruit_label':data.loc[17]['fruit_label'], 'mass':mass_mean, 'width':data.loc[17]['width'], 'height':height_mean, 'color_score':data.loc[17]['color_score']})
data.loc[18] = pd.Series({'fruit_label':data.loc[18]['fruit_label'], 'mass':mass_mean, 'width':data.loc[18]['width'], 'height':height_mean, 'color_score':data.loc[18]['color_score']})
data.loc[19] = pd.Series({'fruit_label':data.loc[19]['fruit_label'], 'mass':mass_mean, 'width':data.loc[19]['width'], 'height':height_mean, 'color_score':data.loc[19]['color_score']})
data.loc[20] = pd.Series({'fruit_label':data.loc[20]['fruit_label'], 'mass':mass_mean, 'width':data.loc[20]['width'], 'height':height_mean, 'color_score':data.loc[20]['color_score']})
data.loc[21] = pd.Series({'fruit_label':data.loc[21]['fruit_label'], 'mass':mass_mean, 'width':data.loc[21]['width'], 'height':height_mean, 'color_score':data.loc[21]['color_score']})
data.loc[22] = pd.Series({'fruit_label':data.loc[22]['fruit_label'], 'mass':mass_mean, 'width':data.loc[22]['width'], 'height':height_mean, 'color_score':data.loc[22]['color_score']})
data.loc[23] = pd.Series({'fruit_label':data.loc[23]['fruit_label'], 'mass':mass_mean, 'width':data.loc[23]['width'], 'height':height_mean, 'color_score':data.loc[23]['color_score']})
data.loc[24] = pd.Series({'fruit_label':data.loc[24]['fruit_label'], 'mass':mass_mean, 'width':data.loc[24]['width'], 'height':height_mean, 'color_score':data.loc[24]['color_score']})
data.loc[25] = pd.Series({'fruit_label':data.loc[25]['fruit_label'], 'mass':mass_mean, 'width':data.loc[25]['width'], 'height':height_mean, 'color_score':data.loc[25]['color_score']})


# to shuffle rows and to keep the indexes in order
data = data.sample(frac=1).reset_index(drop=True)



def KNN(data, k):
    
    distances = []
    predicted_labels = []
    
    for j in range(50,60):
        dist = {}
        for i in range(0,50):
            
            # calculating Euclidean distance
            ans = pow(data.loc[i]['mass']-data.loc[j]['mass'],2) + pow(data.loc[i]['width']-data.loc[j]['width'],2) + pow(data.loc[i]['height']-data.loc[j]['height'],2) + pow(data.loc[i]['color_score']-data.loc[j]['color_score'],2)
            
            dist[i] = [ans, data.loc[i]['fruit_label']]
        
        # sorted dataset to get K elements
        sorted_dist = sorted(dist.items(), key=lambda x: x[1], reverse=False)
        distances.append(sorted_dist[0:k])
        
        
    print(*distances,sep='\n')
    

    # counting labels of test data
    for i in range(0,len(distances)):
        labels = []
        for j in range(0,k):
            labels.append(distances[i][j][1][1])
            
        lst = Counter(labels)
        predicted_labels.append(lst.most_common()[0][0])
    
    print('Preicted labels:',predicted_labels)
    
    
if __name__ == '__main__':

    KNN(data, 3)
        

