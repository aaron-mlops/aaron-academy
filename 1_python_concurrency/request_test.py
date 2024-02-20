import argparse
import time
import requests
import concurrent.futures


sleep_url = "http://localhost:8000/sleep"
count_url = "http://localhost:8000/count"


def request_sleep():
    start_time = time.time()
    url = sleep_url if args.test_case == "sleep" else count_url
    _ = requests.get(url)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("test_case", type=str, default="sleep")
    parser.add_argument("--num_users", type=int, default=2)
    parser.add_argument("--num_requests", type=int, default=10)
    args = parser.parse_args()

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=args.num_users)

    total_start_time = time.time()

    procs = []
    for i in range(args.num_requests):
        procs.append(pool.submit(request_sleep))

    times = []
    for p in concurrent.futures.as_completed(procs):
        times.append(p.result())

    total_end_time = time.time()

    print(f"num_users: {args.num_users}, num_requests: {args.num_requests}")
    print("total:")
    print(round(total_end_time - total_start_time, 5))
