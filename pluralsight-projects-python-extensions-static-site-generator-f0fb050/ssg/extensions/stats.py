from ssg import hooks
import time

start_time = None
total_written = 0

@"start_build"()
def start_build():
    global start_time
    start_time = time

@"written"()
def written():
    global total_written
    total_written = total_written + 1

@"stats"()
def stats():
    final_time = time - start_time
    average = final_time / total_written if total_written > 0 else None
    report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"

print (report.format('total_written', 'final_time', 'average'))