import subprocess
from tqdm import tqdm

def main():
	ini_cmd = "cargo build --release && cp target/release/start scan"
	print(subprocess.getoutput(ini_cmd))
	score_header = "Score = "
	score_sum = 0
	score_norm = 0
	score_min = -1
	score_min_idx = 0
	seed_num = 2000
	for i in tqdm(range(seed_num)):
		cmd = "./scan < tools/in/{0:04d}.txt > tools/out/{0:04d}.txt".format(i, i)
		ret = subprocess.getoutput(cmd)
		cmd = "./vis tools/in/{0:04d}.txt tools/out/{0:04d}.txt".format(i, i)
		ret = subprocess.getoutput(cmd)
		score = int(ret[len(score_header):])
		score_sum += score
		score_norm += 1
		if score_min < 0:
			score_min = score
			score_min_idx = i
		elif score_min > score:
			score_min = score
			score_min_idx = i
	score_mean = score_sum / score_norm
	print("mean", score_mean)
	print("min", score_min_idx, score_min)

if __name__ == "__main__":
	main()