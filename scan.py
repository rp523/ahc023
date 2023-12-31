import subprocess
from tqdm import tqdm
def main():
	ini_cmd = "cargo build --release && cp target/release/start scan"
	#ini_cmd = "cargo build && cp target/debug/start scan"
	print(subprocess.getoutput(ini_cmd))
	score_header = "Score = "
	score_sum = 0
	score_norm = 0
	score_min = 9999999999
	score_min_idx = 0
	score_max = -1
	score_max_idx = 0
	seed_num = 2000
	for i in tqdm(range(seed_num)):
		cmd = "./scan scoring < tools/in/{0:04d}.txt > tools/out/{0:04d}.txt".format(i, i)
		_ = subprocess.getoutput(cmd)
		for line in	open("score.txt"):
			score = int(line)
		score_sum += score
		score_norm += 1
		if score_min > score:
			score_min = score
			score_min_idx = i
		if score_max < score:
			score_max = score
			score_max_idx = i
	score_mean = score_sum / score_norm
	print("mean", score_mean)
	print("min", score_min_idx, score_min)
	print("max", score_max_idx, score_max)

if __name__ == "__main__":
	main()