# knn modelinin dosyaya kayıt edilmesi

import pickle
dosya = "save/model_save/knn"
pickle.dump(knn, open(dosya,'wb'))
knnR = pickle.load(open(dosya,'rb'))

y_pred = knnR.predict(X_test)

print(classification_report(y_test,y_pred))

# Accuracy
knnDogruluk=accuracy_score(y_test,y_pred)
print("Knn Accuracy değeri:",knnDogruluk*100)
