
# $Id: realtime.py 2126 2012-01-17 22:08:56Z dbankie $

trick.frame_log_off()
real_time.rt_sync.enable()
trick_sys.sched.set_software_frame(0.01)
real_time.itimer.disable()

trick_sys.sched.set_enable_freeze(True)
trick_sys.sched.set_freeze_command(True)

simControlPanel = trick.SimControlPanel()
trick.add_external_application(simControlPanel)

#trick_sys.sched.threads[1].rt_cpu_number   = 1
#trick_sys.sched.threads[1].rt_lock_memory  = Yes
#trick_sys.sched.threads[1].rt_nond_pri     = Yes
#trick_sys.sched.threads[1].rt_priority     = 1
#trick_sys.sched.threads[1].rt_lock_to_cpu  = Yes
