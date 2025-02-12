start_sh:
	ab -n 1000 -c 10 http://localhost:8080/index.html

start_wrk:
	wrk -t12 -c400 -d30s http://localhost:8080/index.html
