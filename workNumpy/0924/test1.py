
import numpy as np

# y = ax + b 예측값 계산
def predict(temp_a_b, study_time):
  return temp_a_b[0] * study_time + temp_a_b[1]

def mse(predict_scores, scores):
  return ((predict_scores - scores) ** 2).mean()

def mse_val(predict_scores, score):
  return mse(np.array(predict_scores), np.array(score))


temp_a_bs = [[2, 75], [1.9, 80.6], [3, 76], [4, 60]]
#그런데 최소제곱법 1.9, 80.6 가장 예측점수가 잘나옴 MSE평균제곱오차도 7.9200작음

for a_b in temp_a_bs:
  print('\n기울기: %2.0f  y절편: %3.0f'%(a_b[0], a_b[1]))
  
  study_time = [2, 4, 6, 8, 10]
  score = [81, 93, 91, 97, 98]
  predict_scores = []

  for i, val in enumerate(study_time):
    p = predict(a_b, val)
    predict_scores.append(p)
    print("공부시간:%2.0f 실제점수:%3.0f, 예측점수:%3.0f"%(val, score[i], p))

  print("MSE값: ", mse_val(predict_scores, score))
  