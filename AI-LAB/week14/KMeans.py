
# ------------------- Momina Atif Dar P-18-0030 -----------------------------

import pandas as pd
import random
from math import sqrt 
import numpy as np
from datetime import datetime, timedelta

corpus = pd.read_csv('dataset.csv', encoding='Latin-1')

corpus = corpus.iloc[:,[3,4,5,6]]

mass_mean = corpus['mass'].mean()
height_mean = corpus['height'].mean()

corpus.loc[17] = pd.Series({'mass':mass_mean, 'width':corpus.loc[17]['width'], 'height':height_mean, 'color_score':corpus.loc[17]['color_score']})
corpus.loc[18] = pd.Series({'mass':mass_mean, 'width':corpus.loc[18]['width'], 'height':height_mean, 'color_score':corpus.loc[18]['color_score']})
corpus.loc[19] = pd.Series({'mass':mass_mean, 'width':corpus.loc[19]['width'], 'height':height_mean, 'color_score':corpus.loc[19]['color_score']})
corpus.loc[20] = pd.Series({'mass':mass_mean, 'width':corpus.loc[20]['width'], 'height':height_mean, 'color_score':corpus.loc[20]['color_score']})
corpus.loc[21] = pd.Series({'mass':mass_mean, 'width':corpus.loc[21]['width'], 'height':height_mean, 'color_score':corpus.loc[21]['color_score']})
corpus.loc[22] = pd.Series({'mass':mass_mean, 'width':corpus.loc[22]['width'], 'height':height_mean, 'color_score':corpus.loc[22]['color_score']})
corpus.loc[23] = pd.Series({'mass':mass_mean, 'width':corpus.loc[23]['width'], 'height':height_mean, 'color_score':corpus.loc[23]['color_score']})
corpus.loc[24] = pd.Series({'mass':mass_mean, 'width':corpus.loc[24]['width'], 'height':height_mean, 'color_score':corpus.loc[24]['color_score']})
corpus.loc[25] = pd.Series({'mass':mass_mean, 'width':corpus.loc[25]['width'], 'height':height_mean, 'color_score':corpus.loc[25]['color_score']})


# -------------------------------------------------------------------------------


# Step 2 - Select centroids

def select_centroids(corpus, k, new_centroids):
    
    if new_centroids != []:
        return new_centroids
    
    sc = []
    selected_centroids = []
    
    for i in range(k):
        r = random.randint(0,len(corpus)-1)
        
        if r in sc:
            for i in range(10):
                r2 = random.randint(0, len(corpus)-1)
                if r2 not in sc:
                    sc.append(r2)
                    selected_centroids.append([corpus['mass'][r2], corpus['width'][r2], corpus['height'][r2], corpus['color_score'][r2]])
                    break
        
        else:
            sc.append(r)
            selected_centroids.append([corpus['mass'][r], corpus['width'][r], corpus['height'][r], corpus['color_score'][r]])
    
    return selected_centroids
    

# -------------------------------------------------------------------------------
 
    
# Step 3 - Assign points to closest cluster centroid b calculating Euclidean distance

def assign_points(corpus, selected_centroids):
    cluster1, cluster2, cluster3 = [], [], []
    for i in range(len(corpus)):
        
        row = [corpus['mass'][i], corpus['width'][i], corpus['height'][i], corpus['color_score'][i]]
        
        if row not in selected_centroids:
            
            best_centroid = calc_distance(corpus, selected_centroids, row)
            
            if best_centroid == 0:
                cluster1.append(row)
                
            elif best_centroid == 1:
                cluster2.append(row)
                
            elif best_centroid == 2:
                cluster3.append(row)
                
    return cluster1, cluster2, cluster3
    
  
# calculate euclidean distance between centroids and all points

def calc_distance(corpus, selected_centroids, row):
    clusters = []
    d = float('inf')
    
    for i in range(len(selected_centroids)):
        
        dist = sqrt( pow(np.array(selected_centroids[i][0]-row[0]), 2) + 
        pow(np.array(selected_centroids[i][1]-row[1]), 2) +
        pow(np.array(selected_centroids[i][2]-row[2]), 2) + 
        pow(np.array(selected_centroids[i][3]-row[3]), 2) )
        
        if dist < d:
            d = dist
            b = i
    
    return b
        
    
# -------------------------------------------------------------------------------      
    
    
# Step 4 - Recompute centroids

def recompute_centroids(selected_centroids, cluster1, cluster2, cluster3):
    
    avg_mass, avg_width, avg_height, avg_colorscore = 0, 0, 0, 0
    
    for i in cluster1:
        avg_mass += i[0]
        avg_width += i[1]
        avg_height += i[2]
        avg_colorscore += i[3]
        
    avg_mass = avg_mass/len(cluster1)
    avg_width = avg_width/len(cluster1)
    avg_height = avg_width/len(cluster1)
    avg_colorscore = avg_width/len(cluster1)
    selected_centroids[0] = [avg_mass, avg_width, avg_height, avg_colorscore]

    
    avg_mass, avg_width, avg_height, avg_colorscore = 0, 0, 0, 0
    
    for i in cluster2:
        avg_mass += i[0]
        avg_width += i[1]
        avg_height += i[2]
        avg_colorscore += i[3]
    
    avg_mass = avg_mass/len(cluster2)
    avg_width = avg_width/len(cluster2)
    avg_height = avg_width/len(cluster2)
    avg_colorscore = avg_width/len(cluster2)    
    selected_centroids[1] = [avg_mass, avg_width, avg_height, avg_colorscore]
        
        
    avg_mass, avg_width, avg_height, avg_colorscore = 0, 0, 0, 0

    for i in cluster3:
        avg_mass += i[0]
        avg_width += i[1]
        avg_height += i[2]
        avg_colorscore += i[3]
        
    avg_mass = avg_mass/len(cluster3)
    avg_width = avg_width/len(cluster3)
    avg_height = avg_width/len(cluster3)
    avg_colorscore = avg_width/len(cluster3)
    selected_centroids[2] = [avg_mass, avg_width, avg_height, avg_colorscore]
    
    return selected_centroids
        
        
# -------------------------------------------------------------------------------        


def KMeans(corpus, k):
    
    print('Please wait, the algorithm is running for 3 seconds.')
    
    end_time = datetime.now() + timedelta(seconds=3)
    
    new_centroids = []
    
    while datetime.now() < end_time:
        
        selected_centroids = select_centroids(corpus, k, new_centroids) 
    
        cluster1, cluster2, cluster3 = assign_points(corpus, selected_centroids)
    
        new_centroids = recompute_centroids(selected_centroids, cluster1, cluster2, cluster3)    
            
        
    return cluster1, cluster2, cluster3
    
    
# -------------------------------------------------------------------------------
    
    
if __name__ == '__main__':

    k = 3
    
    c1, c2, c3 = KMeans(corpus,k)
    print('Cluster 1:',c1,sep='\n')
    print('---------------')
    print('Cluster 2:',c2,sep='\n')
    print('---------------')
    print('Cluster 3:',c3,sep='\n')
    
    
    


