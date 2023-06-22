import mlflow
with open("artifacts01.txt", "r") as f:
    text = f.read()

print(text)
new_text="end of the stage-02"
mlflow.log_param("new_text",new_text)
print("end of stage-02")