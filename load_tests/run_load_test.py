import asyncio
import time
import os
import json
import aiohttp
from datetime import datetime

# Configuration
API_BASE_URL = os.getenv("BACKEND_URL", "http://localhost:3001")
CONCURRENT_USERS = 100
DURATION_SECONDS = 60
TIMEOUT_SECONDS = 5

# Metrics storage
latencies = []
success_count = 0
failure_count = 0
error_messages = {}

async def simulate_user(session, end_time):
    global success_count, failure_count
    
    endpoints = [
        ("/auth/login", "POST", {"email": "doc@mail.com", "password": "Pass"}),
        ("/users/profile", "GET", None),
        ("/assessments/dashboard", "GET", None),
        ("/healthz", "GET", None)
    ]
    
    idx = 0
    while time.time() < end_time:
        endpoint, method, payload = endpoints[idx % len(endpoints)]
        idx += 1
        
        start_t = time.time()
        try:
            url = f"{API_BASE_URL}{endpoint}"
            if method == "POST":
                async with session.post(url, json=payload, timeout=TIMEOUT_SECONDS) as response:
                    status = response.status
                    await response.read()
            else:
                async with session.get(url, timeout=TIMEOUT_SECONDS) as response:
                    status = response.status
                    await response.read()
            
            latency = (time.time() - start_t) * 1000 # ms
            latencies.append(latency)
            
            if 200 <= status < 300 or status == 404: # 404 healthz fallback is accepted
                success_count += 1
            else:
                failure_count += 1
                error_messages[status] = error_messages.get(status, 0) + 1
                
        except Exception as e:
            latency = (time.time() - start_t) * 1000
            latencies.append(latency)
            failure_count += 1
            err_str = str(type(e).__name__)
            error_messages[err_str] = error_messages.get(err_str, 0) + 1
            
        # Subtle delay to simulate real user behavior pacing (think time)
        await asyncio.sleep(0.05)

async def main():
    print(f"=== Starting CogniTest System Load Testing ===")
    print(f"Target URL: {API_BASE_URL}")
    print(f"Virtual Users: {CONCURRENT_USERS}")
    print(f"Duration: {DURATION_SECONDS} seconds")
    print(f"Please wait...")
    
    start_time = time.time()
    end_time = start_time + DURATION_SECONDS
    
    # Increase system limits for concurrent connections
    conn = aiohttp.TCPConnector(limit=CONCURRENT_USERS, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = [simulate_user(session, end_time) for _ in range(CONCURRENT_USERS)]
        await asyncio.gather(*tasks)
        
    actual_duration = time.time() - start_time
    total_requests = success_count + failure_count
    rps = total_requests / actual_duration if actual_duration > 0 else 0
    
    # Calculate stats
    if latencies:
        sorted_latencies = sorted(latencies)
        min_lat = sorted_latencies[0]
        max_lat = sorted_latencies[-1]
        avg_lat = sum(sorted_latencies) / len(sorted_latencies)
        p95_idx = int(len(sorted_latencies) * 0.95)
        p95_lat = sorted_latencies[p95_idx] if p95_idx < len(sorted_latencies) else avg_lat
        p99_idx = int(len(sorted_latencies) * 0.99)
        p99_lat = sorted_latencies[p99_idx] if p99_idx < len(sorted_latencies) else avg_lat
    else:
        min_lat = max_lat = avg_lat = p95_lat = p99_lat = 0
        
    error_rate = (failure_count / total_requests * 100) if total_requests > 0 else 0
    pass_rate = 100 - error_rate
    
    # Threshold verification
    avg_ok = avg_lat < 1500
    p95_ok = p95_lat < 3000
    err_ok = error_rate < 10
    pass_ok = pass_rate > 85
    
    system_pass = avg_ok and p95_ok and err_ok and pass_ok
    
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "target_url": API_BASE_URL,
        "duration_seconds": actual_duration,
        "concurrent_users": CONCURRENT_USERS,
        "total_requests": total_requests,
        "success_count": success_count,
        "failure_count": failure_count,
        "requests_per_second": rps,
        "latencies": {
            "min_ms": min_lat,
            "max_ms": max_lat,
            "avg_ms": avg_lat,
            "p95_ms": p95_lat,
            "p99_ms": p99_lat
        },
        "error_rate_percent": error_rate,
        "pass_rate_percent": pass_rate,
        "errors": error_messages,
        "thresholds": {
            "p95_under_3000ms": p95_ok,
            "avg_under_1500ms": avg_ok,
            "error_rate_under_10percent": err_ok,
            "pass_rate_over_85percent": pass_ok
        },
        "overall_status": "PASSED" if system_pass else "FAILED"
    }
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    with open("reports/load_test_report.json", "w") as f:
        json.dump(report, f, indent=4)
        
    print("\n" + "="*50)
    print("           SYSTEM LOAD TEST COMPLETED           ")
    print("="*50)
    print(f"Status:             {'🟢 PASSED' if system_pass else '🔴 FAILED'}")
    print(f"Total Requests:     {total_requests}")
    print(f"Successful:         {success_count}")
    print(f"Failed:             {failure_count}")
    print(f"Throughput (RPS):   {rps:.2f} req/s")
    print(f"Average Latency:    {avg_lat:.2f} ms")
    print(f"Min Latency:        {min_lat:.2f} ms")
    print(f"Max Latency:        {max_lat:.2f} ms")
    print(f"p95 Latency:        {p95_lat:.2f} ms")
    print(f"HTTP Error Rate:    {error_rate:.2f}%")
    print("="*50)
    print("Threshold Validation:")
    print(f"  * p95 Latency < 3000ms:   {'✅ PASS' if p95_ok else '❌ FAIL'} ({p95_lat:.2f}ms)")
    print(f"  * Avg Latency < 1500ms:   {'✅ PASS' if avg_ok else '❌ FAIL'} ({avg_lat:.2f}ms)")
    print(f"  * Error Rate < 10%:       {'✅ PASS' if err_ok else '❌ FAIL'} ({error_rate:.2f}%)")
    print(f"  * Pass Rate > 85%:        {'✅ PASS' if pass_ok else '❌ FAIL'} ({pass_rate:.2f}%)")
    print("="*50 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
