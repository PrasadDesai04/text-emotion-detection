from transformers import pipeline

emotion_detector = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

text = input("Enter your text: ")
results = emotion_detector(text)

print("\nEmotion probabilities:")
for emotion in results[0]:
    print(f"{emotion['label']} : {emotion['score']:.3f}")
