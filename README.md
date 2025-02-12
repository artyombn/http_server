# Простой HTTP сервер

## Возможности
- Обработка нескольких параллельных подключений с использованием потоков.
- Обслуживание статических файлов из директории `views`.
- Возвращает ошибку 404, если запрашиваемый файл не найден.

## Запуск сервера
```bash
python main.py
```
   
**Сервер будет работать на localhost и порту 8080.**

## Результаты нагрузки

**Бенчмарк с использованием wrk (тест на нагрузку 30 секунд)**

```bash
wrk -t12 -c400 -d30s http://localhost:8080/index.html
Running 30s test @ http://localhost:8080/index.html
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.66ms    3.49ms  89.24ms   98.36%
    Req/Sec   503.02    127.51   777.00     81.04%
  107381 requests in 30.04s, 44.24MB read
  Socket errors: connect 0, read 452153, write 0, timeout 0
Requests/sec:   3574.34
Transfer/sec:      1.47MB
```

**Бенчмарк с использованием ab (1000 запросов)**
```bash
ab -n 1000 -c 10 http://localhost:8080/index.html
Server Software:        
Server Hostname:        localhost
Server Port:            8080

Document Path:          /index.html
Document Length:        373 bytes

Concurrency Level:      10
Time taken for tests:   0.111 seconds
Complete requests:      1000
Failed requests:        0
Requests per second:    9016.24 [#/sec] (mean)
Transfer rate:          3803.73 [Kbytes/sec] received
```