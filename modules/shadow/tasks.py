import subprocess
import datetime

import psutil
from celery import Celery

celery_app = Celery("shadow")
celery_app.config_from_object("celery_config")


ss_data = {
    "last_start": datetime.datetime.now(),
    "last_refresh": datetime.datetime.now(),
    "refresh_period": datetime.timedelta(hours=1)
}

process = None


def is_process_alive(pid):
    pids = psutil.pids()
    if pid in pids:
        return True
    return False


@celery_app.task
def auto_close_ss():
    if ss_data["last_refresh"] - ss_data["last_start"] > ss_data["refresh_period"]:
        global process
        process.kill()
        process = None


@celery_app.task
def refresh_ss(refresh_timedelta_min):
    ss_data["last_refresh"] = datetime.datetime.now()
    ss_data["refresh_period"] = datetime.timedelta(minutes=refresh_timedelta_min)
    print(refresh_timedelta_min)
    global process
    if process is None or not is_process_alive(process.pid):
        print("Starting shadowsocks server")
        process = subprocess.Popen("exec ssserver -c .shadow.ini", shell=True)
        try:
            # this kills zombie subprocess if starting ssserver fails
            process.wait(1)
        except subprocess.TimeoutExpired:
            pass


@celery_app.task
def status_ss():
    global process
    if process and is_process_alive(process.pid):
        is_alive = True
    else:
        is_alive = False

    result = {"is_alive": is_alive}
    result.update(ss_data)
    result["refresh_period"] = result["refresh_period"].total_seconds()
    return result
