#KNN
# k-fold sonucunu dosyaya kaydediyorum
import pickle
dosya = "dosya_yolu/save/kfold_save/knn_cv"
pickle.dump( accMeanKNN , open(dosya,'wb'))
accMeanKNN = pickle.load(open(dosya,'rb'))

print( accMeanKNN )