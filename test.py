from datasets import load_dataset
ds = load_dataset("BEE-spoke-data/consumer-finance-complaints", "default")
print(ds['train'][5])